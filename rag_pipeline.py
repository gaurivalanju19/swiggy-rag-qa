from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain_community.llms import Ollama


embeddings = HuggingFaceEmbeddings()

vectorstore = FAISS.load_local(
    "vector_db",
    embeddings,
    allow_dangerous_deserialization=True
)

retriever = vectorstore.as_retriever()

llm = Ollama(model="llama3")

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever
)

def ask_question(query):
    return qa_chain.run(query)