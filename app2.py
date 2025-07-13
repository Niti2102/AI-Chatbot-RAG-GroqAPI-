from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings  # ✅ updated import
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA
import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ✅ FIXED: Set up embeddings using HuggingFace with meta tensor workaround
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={
        "device": "cpu",  # ⬅️ force CPU usage
        "trust_remote_code": True  # ⬅️ fixes meta tensor issue in torch 2.3+
    }
)

# Load the FAISS index
vectordb = FAISS.load_local("faissindex", embeddings, allow_dangerous_deserialization=True)

# Set up retriever and LLM (Groq + LLaMA 3)
retriever = vectordb.as_retriever()
llm = ChatGroq(
    groq_api_key=os.environ["GROQ_API_KEY"],
    model_name="llama3-70b-8192"
)

# Build the QA chain
chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

# Streamlit UI setup
st.set_page_config(page_title="Nitish M AI Chatbot")
st.title("🤖 ASK ANYTHING FROM MY RESUME")

query = st.text_input("🔍 Pinch your questions:")

if query:
    with st.spinner("🤔 Thinking..."):
        response = chain.invoke(query)  # ✅ recommended over deprecated `.run()`
        st.success(response)
