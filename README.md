# PDF Question Answering Chatbot

This project is a Retrieval-Augmented Generation (RAG) based chatbot that answers questions from a PDF document.

## Features

* Reads and processes PDF documents
* Splits text into chunks for efficient retrieval
* Uses Sentence Transformers for embeddings
* Stores embeddings in FAISS vector database
* Answers questions based on PDF content
* Returns "Not found in document" for unrelated queries

## Technologies Used

* Python
* LangChain
* FAISS
* Sentence Transformers
* Streamlit

## Run the Project

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```
