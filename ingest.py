from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

loader = PyPDFLoader("data/Swiggy-Annual-Report.pdf")
documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

docs = text_splitter.split_documents(documents)

embeddings = HuggingFaceEmbeddings()

vectorstore = FAISS.from_documents(docs, embeddings)

vectorstore.save_local("vector_db")

print("Vector database created!")