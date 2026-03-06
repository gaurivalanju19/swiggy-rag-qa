import streamlit as st
from rag_pipeline import ask_question

st.title("Swiggy Annual Report QA System")

query = st.text_input("Ask a question about Swiggy")

if query:
    answer = ask_question(query)
    st.write(answer)