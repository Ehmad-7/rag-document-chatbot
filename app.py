import streamlit as st
import os
from rag.loader import load_pdfs
from rag.chunker import clean_text, chunk_text
from rag.embedder import embed_texts, model
from rag.retriever import VectorStore
from backend.resume_engine import parse_resume, answer_resume
from backend.knowledge_engine import answer_knowledge
from backend.router import route
from backend.smalltalk import handle_small_talk
from transformers import pipeline

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

st.set_page_config(page_title="AI PDF Assistant", layout="wide")
st.title("📄🤖 AI Document Assistant")

# ===== Upload PDFs =====
st.sidebar.header("Upload Documents")

knowledge_files = st.sidebar.file_uploader(
    "Upload knowledge PDFs", type=["pdf"], accept_multiple_files=True
)

resume_file = st.sidebar.file_uploader("Upload resume PDF", type=["pdf"])

# ===== Save Uploaded Files =====
def save_files(files, folder):
    paths = []
    for f in files:
        path = os.path.join(folder, f.name)
        with open(path, "wb") as out:
            out.write(f.read())
        paths.append(path)
    return paths


# ===== Process Knowledge Docs =====
if knowledge_files:
    save_files(knowledge_files, UPLOAD_DIR)

    docs = load_pdfs(UPLOAD_DIR)
    chunks = []
    for d in docs:
        d = clean_text(d)
        chunks.extend(chunk_text(d))

    embeddings = embed_texts(chunks)
    knowledge_store = VectorStore(embeddings, chunks)

    st.success("Knowledge documents processed!")

# ===== Process Resume =====
resume_fields = None

if resume_file:
    path = os.path.join(UPLOAD_DIR, resume_file.name)
    with open(path, "wb") as out:
        out.write(resume_file.read())

    resume_text = clean_text(" ".join(load_pdfs(UPLOAD_DIR)))
    resume_fields = parse_resume(resume_text)
    st.success("Resume processed!")

# ===== AUTO SUMMARY =====
llm = pipeline("text2text-generation", model="google/flan-t5-base", max_length=200)

if knowledge_files:
    preview = " ".join(chunks[:5])

    summary_prompt = f"""
Summarize what this document is about in 4 bullet points.

Text:
{preview}
"""

    summary = llm(summary_prompt)[0]["generated_text"]
    st.subheader("📌 Document Summary")
    st.write(summary)

    st.subheader("💡 Suggested Questions")
    st.write("- Who is mentioned in the document?")
    st.write("- What are the main topics?")
    st.write("- Summarize key ideas")

# ===== MODE SELECTION =====
mode = st.radio("Choose Mode:", ["Ask about Documents", "Ask about Resume"])

# ===== CHAT INTERFACE =====
st.subheader("💬 Chat")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

question = st.text_input("Ask your question:")

if st.button("Send") and question:

    small = handle_small_talk(question)
    if small:
        answer = small
    else:
        if mode == "Ask about Resume" and resume_fields:
            answer = answer_resume(question, resume_fields)
        else:
            # Check if knowledge_store is initialized
            if 'knowledge_store' in locals():
                 answer = answer_knowledge(question, knowledge_store, model, llm)
            else:
                answer = "Please upload knowledge documents first."

    st.session_state.chat_history.append(("You", question))
    st.session_state.chat_history.append(("Assistant", answer))

# ===== DISPLAY CHAT =====
for speaker, msg in st.session_state.chat_history:
    if speaker == "You":
        st.markdown(f"**You:** {msg}")
    else:
        st.markdown(f"**Assistant:** {msg}")
