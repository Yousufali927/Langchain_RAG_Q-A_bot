# Langchain_RAG_Q-A_bot

1. Project Motivation
2. Project Structure
3. Installation
4. Usage

----------------------------------------------------------------------------------------------------

## 1. Project Motivation
   Ever had trouble reading through official documentation and making sense of complex topics? I have. This Generative AI application
   (Q&A-bot) is an attempt at solving that problem. I was having trouble learning some topics of langchain through documentation, and
   I couldn't find good explanation videos on youtube either, naturally I asked ChatGPT but it was giving me weird responses, so I asked
   a very basic question and this is the response I got.

    Q. What is langchain?

    A. As of my last update in January 2022, "Langchain" doesn't appear to be a widely recognized term or concept. It's possible that it
     could have emerged or gained significance after that time.

    However, based on the term itself, it could potentially refer to a blockchain-based system designed for language-related applications or
    services. Blockchain technology is known for its decentralized and secure nature, and it has been applied to various industries beyond
    finance, including supply chain management, healthcare, and even language-related fields like translation and linguistics.

    If "Langchain" is a specific project, platform, or concept that emerged after 2022, I would need more context to provide accurate
    information about it.

## 🙂🔫
   Eventually I was able to find some videos on youtube that helped, and after learning langchain and RAG, I reallised I could build an
   application that uses Retrieval Augmented System(RAG) with one of OpenAI's model to help summarize or understand any question about any
   technology, or for that matter any topic of any subject by doing web scraping and using that as a database for queries.


## 2. Project Structure
   main.py: The main Streamlit application script.
   requirements.txt: A list of required Python packages for the project
   .env: Configuration file for storing your OpenAI API key.
   fais_index_data_dat: storing data as serialized bytes

## 3. The installation are present in requirements.txt

   1. Install those dependencies using
```
pip install -r requirements.txt
```
  2. Setup OpenAI API key in .env file
```
  OPENAI_API_KEY = "your_api_key_here"
```

## 4. Usage

1. Run the app by executing
```
  streamlit run main.py
```
2. The web app will open in browser
3. Input the site URLS in the sidebar and hit process URLs button to make the reference database for the AI to use, to answer your queries.
   




   




