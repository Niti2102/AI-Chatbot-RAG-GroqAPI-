

# 🤖 Resume QA Chatbot using Groq + LangChain + FAISS

An interactive AI chatbot built with [Streamlit](https://streamlit.io/) and powered by [Groq's LLaMA3-70B model](https://groq.com/). This chatbot uses **RAG (Retrieval-Augmented Generation)** to answer questions directly from **Nitish's Resume** using vector search.

---

## 🚀 Features

* 📄 Upload and parse PDF resumes
* 🔍 Semantic search using FAISS Vector DB
* 🧠 Ask natural language questions about the resume
* ⚡ Powered by **Groq** LLM (LLaMA3-70B)
* 🔐 API Key securely managed using Streamlit secrets

---

## 🖥️ Demo

> https://t2jfm73mxtjo3d2ghlvenr.streamlit.app/

---

## 🧠 Tech Stack

* **Frontend**: Streamlit
* **Backend**: LangChain + FAISS
* **LLM**: `llama3-70b-8192` via `langchain_groq`
* **Embedding Model**: `sentence-transformers/paraphrase-MiniLM-L6-v2`

---

## 📂 File Structure

```
resume-rag-chatbot/
│
├── app.py / app2.py             # Main Streamlit chatbot app
├── index.faiss                  # FAISS vector store index
├── index.pkl                    # Serialized metadata store
├── Nitish Resume.pdf            # Resume used for QA
├── requirements.txt             # Python dependencies
└── .streamlit/
    └── secrets.toml             # API key configuration
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/resume-rag-chatbot.git
cd resume-rag-chatbot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Add Your Groq API Key

Create `.streamlit/secrets.toml`:

```toml
GROQ_API_KEY = "your_groq_api_key_here"
```

> ❗ Never share or commit your API key to GitHub.

### 4. Run the App

```bash
streamlit run app.py
```

---

## 🤖 How It Works

1. **PDF Parsing**: Resume is loaded using `PyPDFLoader`
2. **Chunking**: Content split into small sections using `RecursiveCharacterTextSplitter`
3. **Embedding**: Chunks converted to vectors using HuggingFace embeddings
4. **Storage**: Vectors stored using FAISS for semantic retrieval
5. **RAG Chain**: Query is answered using Groq’s LLM + retrieved relevant chunks

---

## 🧪 Example Questions

* "What are Nitish's technical skills?"
* "Has he done any internships?"
* "List Nitish’s machine learning projects"
* "What is his educational background?"

---

## ✅ Dependencies

```txt
streamlit
langchain
langchain_groq
langchain_community
python-dotenv
sentence-transformers
faiss-cpu
```

---

## 💡 Future Ideas

* Upload resume dynamically
* Support multiple resumes and switch users
* Add chat history and feedback loop
* Deploy on HuggingFace Spaces / Streamlit Cloud

---

## 📄 License

© All rights reserved: Nitish

---

## 🙌 Acknowledgements

* [Groq AI](https://groq.com/)
* [LangChain](https://www.langchain.com/)
* [Streamlit](https://streamlit.io/)
* [FAISS](https://github.com/facebookresearch/faiss)

---

