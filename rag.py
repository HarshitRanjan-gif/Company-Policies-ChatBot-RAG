# Import
import faiss
import pickle
import os
import streamlit as st

from sentence_transformers import SentenceTransformer

from groq import Groq

from dotenv import load_dotenv

# Load .env Groq KEY

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# Load FAISS

@st.cache_resource
def load_faiss():
    return faiss.read_index("faiss_index.bin")

index = load_faiss()

# Load Chunks

@st.cache_resource
def load_chunks():

    with open("chunks.pkl", "rb") as f:

        return pickle.load(f)

chunks = load_chunks()

# Load Embedding Model

@st.cache_resource
def load_embedding_model():
    return SentenceTransformer("BAAI/bge-m3")

embedding_model = load_embedding_model()

# retrieve_context()

def retrieve_context(query, k=3):

    query_embedding = embedding_model.encode(
        [query],
        convert_to_numpy=True
    )

    distances, indices = index.search(
        query_embedding,
        k
    )

    context = ""

    for idx in indices[0]:

        context += chunks[idx]

        context += "\n\n"

    return context

# ask_rag()

def ask_rag(query):

    context = retrieve_context(query)

    prompt = f"""
You are an AI HR Policy Assistant.

Answer ONLY using the provided context.

If the answer is not found in the context,
say:

"I couldn't find this information in the company policies."

Provide a detailed answer.

Context:
{context}

Question:
{query}
"""

    response = client.chat.completions.create(

        model="llama-3.1-8b-instant",

        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ],

        temperature=0.2,

        max_tokens=500

    )

    return response.choices[0].message.content, context
