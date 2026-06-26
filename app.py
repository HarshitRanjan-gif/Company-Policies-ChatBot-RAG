import streamlit as st
import time

from rag import ask_rag


# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Company Policy Assistant",
    page_icon="📄",
    layout="wide"
)

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("📄 Company Policy Assistant")

st.sidebar.markdown("---")

st.sidebar.write("### Model")
st.sidebar.success("BGE-M3")

st.sidebar.write("### Vector Database")
st.sidebar.success("FAISS")

st.sidebar.write("### LLM")
st.sidebar.success("Groq - Llama 3.1")

st.sidebar.markdown("---")

st.sidebar.write("Ask questions related to the company policy manual.")

st.sidebar.markdown("---")

if st.sidebar.button("🗑 Clear Chat"):
    st.session_state.messages = []
    st.rerun()


# -----------------------------
# Title
# -----------------------------
st.title("📄 Company Policy Assistant")

st.write(
    "Ask any question related to the company policies."
)

st.markdown("---")


# -----------------------------
# Chat History
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

        if message["role"] == "assistant":

            if "time" in message:
                st.caption(f"⏱ Response Time: {message['time']} seconds")

            if "context" in message:
                with st.expander("📚 Retrieved Context"):
                    st.write(message["context"])


# -----------------------------
# User Input
# -----------------------------
question = st.chat_input("Ask your question...")

if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):

        with st.spinner("Searching company policies..."):

            # Start Timer
            start = time.time()

            answer, context = ask_rag(question)

            # End Timer
            end = time.time()

        # Total Time
        elapsed = round(end - start, 2)

        # Display Answer
        st.markdown(answer)

        # Display Response Time
        st.caption(f"⏱ Response Time: {elapsed} seconds")

        # Retrieved Context
        with st.expander("📚 Retrieved Context"):

            st.write(context)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer,
            "time": elapsed,
            "context": context
        }
    )