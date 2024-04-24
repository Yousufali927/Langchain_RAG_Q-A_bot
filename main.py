import os 
import numpy as np
import streamlit as st
import pickle
import time
import langchain
from langchain import OpenAI
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.chains.qa_with_sources.loading import load_qa_with_sources_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import UnstructuredURLLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

from dotenv import load_dotenv
load_dotenv()

class SessionState:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

def get_session_state():
    return SessionState(
        vectorstore_openai=None
    )

st.title("Learning_AI_using_GenAI")
st.sidebar.title("Enter the Article URLs for Reference")
st.sidebar.text("Make sure to use official documentations as much as possible ")

urls = []
for i in range(3):
    url = st.sidebar.text_input(f"URL {i+1}")
    urls.append(url)

process_url_clicked = st.sidebar.button("Process the URLs")
file_path = "faiss_index_data.dat"

main_placeholder = st.empty()
llm = OpenAI(model="gpt-3.5-turbo-instruct", temperature=0.3, max_tokens=500)


# Create a session state object to store the vectorstore_openai 
session_state = get_session_state()

if process_url_clicked:
    # loading data
    loader = UnstructuredURLLoader(urls=urls)
    main_placeholder.text("Data Loading...Started...")
    data = loader.load()
    #splitting data
    text_splitter = RecursiveCharacterTextSplitter(
        separators= ["\n\n", "\n", " "],
        chunk_size = 200
    )

    main_placeholder.text("Text Splitter...Started...")
    docs = text_splitter.split_documents(data)
    # create embeddings and saving to FAISS index
    embeddings = OpenAIEmbeddings()
    vectorstore_openai = FAISS.from_documents(docs, embeddings)
    main_placeholder.text("Embedding vector started building...")
    time.sleep(2)

    # Save vectorstore_openai in session state
    session_state.vectorstore_openai = vectorstore_openai
    st.write("Vector store saved in session state:")
    # debugging step st.write("Vector store saved in session state:",vectorstore_openai)

    # now saving the vector-index
    # Serialize the FAISS index to bytes
    serialized_bytes = vectorstore_openai.serialize_to_bytes()

    # Save the serialized bytes to a file
    with open(file_path, "wb") as file:
        file.write(serialized_bytes)

    # Update session state to indicate processing is done
    session_state.processed = True



query = main_placeholder.text_input("Question: ")
if query:
    st.write("Vector store retrieved from session state:")
    if os.path.exists(file_path):
        if session_state.vectorstore_openai is None:
            st.error("Vector store is None. Please process URLs again.")
        else:
            # Read the serialized bytes from the file
            with open("faiss_index_data.dat", "rb") as file:
                serialized_bytes = file.read()

        # Deserialize the bytes back into the FAISS index object
        
        reconstructed_vectorIndex = session_state.vectorstore_openai.deserialize_from_bytes(serialized_bytes, embeddings)
        chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever = reconstructed_vectorIndex.as_retriever())
        result = chain({"question":query}, return_only_outputs=True)

        st.header("Answer")
        st.subheader(result["answer"])

        # displaying the sources 
        sources = result.get("sources","")
        if sources:
            st.subheader("Sources:")
            sources_list = sources.split("\n")
            for source in sources_list:
                st.write(source)

