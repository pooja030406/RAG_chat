<<<<<<< HEAD
print("Program Started...")

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

try:
    print("Loading PDF...")
    loader = PyPDFLoader("notes.pdf")
    documents = loader.load()
    print(f"PDF Loaded Successfully! Pages: {len(documents)}")

    print("Splitting PDF into chunks...")
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    docs = splitter.split_documents(documents)
    print(f"Created {len(docs)} chunks")

    print("Loading Embedding Model...")
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    print("Creating Vector Database...")
    vectorstore = FAISS.from_documents(docs, embeddings)

    print("\nPDF processed successfully!")
    print("Type 'exit' to quit.")

    while True:
        query = input("\nQuestion: ")

        if query.lower() == "exit":
            print("Goodbye!")
            break

        results = vectorstore.similarity_search_with_score(query, k=1)

        if not results:
            print("Not found in document")
            continue

        document, score = results[0]

        if score > 1.0:
            print("Not found in document")
        else:
            print("\nAnswer:")
            print(document.page_content)

except Exception as e:
    print("\nERROR:")
=======
print("Program Started...")

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

try:
    print("Loading PDF...")
    loader = PyPDFLoader("notes.pdf")
    documents = loader.load()
    print(f"PDF Loaded Successfully! Pages: {len(documents)}")

    print("Splitting PDF into chunks...")
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    docs = splitter.split_documents(documents)
    print(f"Created {len(docs)} chunks")

    print("Loading Embedding Model...")
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    print("Creating Vector Database...")
    vectorstore = FAISS.from_documents(docs, embeddings)

    print("\nPDF processed successfully!")
    print("Type 'exit' to quit.")

    while True:
        query = input("\nQuestion: ")

        if query.lower() == "exit":
            print("Goodbye!")
            break

        results = vectorstore.similarity_search_with_score(query, k=1)

        if not results:
            print("Not found in document")
            continue

        document, score = results[0]

        if score > 1.0:
            print("Not found in document")
        else:
            print("\nAnswer:")
            print(document.page_content)

except Exception as e:
    print("\nERROR:")
>>>>>>> 803011db8ad1f9f373b0df4ff8eb62b4e49e8cae
    print(e)