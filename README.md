# 📄 Company Policy Chatbot(RAG)

An AI-powered Company Policy Chatbot that answers employee queries using a company's HR policy document. The chatbot uses semantic search with vector embeddings to retrieve the most relevant information and generates responses using the Groq Llama 3.1 language model.

## 🖥️ Live Demo

https://company-policies-chatbot-d4ntyopwv6yk7tekn5m53g.streamlit.app/

## 🚀 Features

- AI-powered HR policy question answering
- Semantic search using vector embeddings
- FAISS vector database for fast document retrieval
- HuggingFace BAAI/BGE-M3 embedding model
- Groq Llama 3.1 8B for response generation
- Interactive Streamlit interface
- Displays retrieved document context
- Fast and accurate responses

## 🛠️ Tech Stack

- Python
- Streamlit
- FAISS
- HuggingFace Embeddings (BAAI/BGE-M3)
- Groq API (Llama 3.1 8B)
- PyPDF
- Sentence Transformers

## 📂 Project Structure

```
CompanyPolicyRAG_Manual/
│
├── app.py
├── rag.py
├── faiss_index.bin
├── chunks.pkl
├── requirements.txt
└── .env
```

## 💬 Example Questions

- What is the Leave Policy?
- Tell me about the Laptop Policy.
- How many casual leaves are allowed?
- Who is eligible for a company laptop?
- What is the attendance policy?

## 📌 Future Improvements

- Conversational chat history
- Source page citations
- Multi-document support
- Streaming responses
- Advanced retrieval optimization

## 📄 License

This project is developed for learning and portfolio purposes.
