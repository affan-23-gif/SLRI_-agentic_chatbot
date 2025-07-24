import streamlit as st
import os
from main import main_pipeline

st.set_page_config(page_title="📄 Agentic RAG Chatbot", layout="centered")
st.title("📄 Agentic RAG Chatbot with MCP")

# Initialize session state to keep track of uploaded
if "uploaded" not in st.session_state:
    st.session_state.uploaded = False

# Upload section
st.subheader("📁 Upload your documents")
uploaded_files = st.file_uploader(
    "Choose files (PDF, DOCX, PPTX, TXT, CSV)",
    type=["pdf", "docx", "pptx", "txt", "csv"],
    accept_multiple_files=True
)

if st.button("📤 Upload Documents"):
    if uploaded_files:
        os.makedirs("documents", exist_ok=True)
        for file in uploaded_files:
            with open(os.path.join("documents", file.name), "wb") as f:
                f.write(file.getbuffer())
        st.success("✅ Documents uploaded successfully.")
        st.session_state.uploaded = True
    else:
        st.warning("⚠️ Please select at least one file before uploading.")

# Question input
if st.session_state.uploaded:
    st.subheader("💬 Ask a question based on uploaded documents")
    query = st.text_input("Type your question here:")

    if st.button("🧠 Get Answer") and query:
        with st.spinner("🔍 Processing..."):
            result = main_pipeline(query)
            st.success("✅ Answer generated!")

            st.subheader("📌 Answer")
            st.markdown(result["answer"])

            st.subheader("📚 Source Contexts")
            for i, doc in enumerate(result["sources"], 1):
                st.markdown(f"**Source {i}:**")
                st.code(doc.page_content[:300] + "...", language='text')
