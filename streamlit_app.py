import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

st.title("PDF Question Answering Chatbot")

@st.cache_resource
def load_vectorstore():
    loader = PyPDFLoader("notes.pdf")
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    docs = splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    return FAISS.from_documents(docs, embeddings)

vectorstore = load_vectorstore()

query = st.text_input("Ask a question from the PDF")

if query:
    results = vectorstore.similarity_search_with_score(query, k=1)

    if not results:
        st.error("Not found in document")
    else:
        document, score = results[0]

        if score > 1.0:
            st.error("Not found in document")
        else:
            st.success(document.page_content)