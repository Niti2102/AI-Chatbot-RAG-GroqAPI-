# rag_chatbot.py

# Load Resume and Build Vector Store
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()
embeddings = HuggingFaceBgeEmbeddings(model_name="all-MiniLM-L6-v2")
vectordb = FAISS.load_local("faissindex", embeddings, allow_dangerous_deserialization=True)
retriever = vectordb.as_retriever()
llm = ChatGroq(
    groq_api_key=os.environ["GROQ_API_KEY"],
    model_name="llama3-70b-8192"
)
chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
st.set_page_config(page_title="Nitish M AI Chatbot")
st.title(" ASK ANYTHING FROM MY RESUME")

query = st.text_input("Pinch your questions")

if query:
    with st.spinner("Thinking..."):
        response = chain.run(query)
        st.success(response)
