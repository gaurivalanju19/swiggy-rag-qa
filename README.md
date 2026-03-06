
# Swiggy Annual Report RAG QA System

## Project Overview

This project implements a **Retrieval-Augmented Generation (RAG)** based Question Answering system that allows users to ask questions about the **Swiggy Annual Report** and receive answers grounded strictly in the document.

The system retrieves relevant sections from the report and uses a language model to generate accurate answers based only on the retrieved content.

This prevents hallucination and ensures that responses are **document-backed and context-aware**.

---

## Architecture

User Query
↓
Retriever (FAISS Vector Search)
↓
Relevant Document Chunks
↓
LLM (Llama3 via Ollama)
↓
Final Answer

---

## Tech Stack

* Python
* LangChain
* FAISS (Vector Database)
* Sentence Transformers (Embeddings)
* Streamlit (User Interface)
* Llama3 via Ollama (Local LLM)

---

## Project Structure

```
Swiggy-RAG-Project
│
├── data/
│   └── Swiggy-Annual-Report.pdf
│
├── ingest.py
├── rag_pipeline.py
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## How to Run the Project

### 1. Clone the Repository

```
git clone https://github.com/gaurivalanju19/swiggy-rag-qa.git
cd swiggy-rag-qa
```

---

### 2. Create Virtual Environment

```
python -m venv venv
```

Activate it:

Windows

```
venv\Scripts\activate
```

Mac/Linux

```
source venv/bin/activate
```

---

### 3. Install Dependencies

```
pip install -r requirements.txt
```

---

### 4. Install Ollama

Download Ollama:

https://ollama.com

Then download the Llama3 model:

```
ollama run llama3
```

---

### 5. Create the Vector Database

Run the ingestion script to process the Swiggy Annual Report.

```
python ingest.py
```

This will create the FAISS vector database.

---

### 6. Start the Application

```
streamlit run app.py
```

---

### 7. Open the Web Interface

Open the following URL in your browser:

```
http://localhost:8501
```

---

## Example Queries

Try asking questions such as:

* What services does Swiggy provide?
* What are Swiggy's main business segments?
* What risks are mentioned in the annual report?
* What strategies does Swiggy use for business growth?

---

## Features

* Retrieval-Augmented Generation (RAG)
* Semantic search using embeddings
* Local LLM inference using Llama3
* Document-grounded answers
* Simple interactive UI using Streamlit

---

## Author

Gauri Valanju

---
