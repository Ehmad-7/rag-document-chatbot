# AI Document Assistant — RAG-Based GenAI System

This project is a learning-focused Generative AI application that allows users to upload PDF documents and ask questions about them using a Retrieval-Augmented Generation (RAG) pipeline. It also supports structured question answering from a resume PDF using rule-based information extraction.

The main goal of this project is to understand and implement core AI engineering concepts such as document retrieval, embeddings, routing, prompt design, and multi-pipeline system architecture — not to build a production-ready system.

---

## Features

### Document Question Answering (RAG)
- Upload one or more PDF documents
- Text extraction and cleaning
- Chunking of document text
- Embedding-based semantic retrieval
- LLM-based answer generation from retrieved chunks

### Resume Question Answering
- Upload resume PDF
- Rule-based extraction of structured fields:
  - Education
  - Skills
  - Experience
- Accurate answers to profile-related questions without LLM hallucination

### Intelligent Query Routing
- Automatically decides whether the question is about:
  - Document knowledge
  - Resume/profile information
- Prevents mixing of unrelated information

### Web-Based Chat Interface
- Built using Streamlit
- Mode selection: Document QA or Resume QA
- Simple chat history display

---

## Concepts Implemented

This project implements and experiments with the following AI/ML concepts:

- Retrieval-Augmented Generation (RAG)
- Sentence Embeddings
- Vector Similarity Search
- Chunking Strategies
- Prompt Engineering
- Rule-Based Information Extraction
- Query Routing Logic
- Multi-Pipeline AI System Design
- LLM Limitations and Failure Modes

---

## Tech Stack

- Python
- SentenceTransformers (for embeddings)
- HuggingFace Transformers (FLAN-T5)
- PyTorch
- Streamlit (web UI)
- PyPDF2 (PDF text extraction)
- Scikit-learn (similarity utilities)

---

## Project Structure

.
├── app.py # Streamlit UI
├── backend/
│ ├── router.py
│ ├── smalltalk.py
│ ├── resume_engine.py
│ └── knowledge_engine.py
├── rag/
│ ├── loader.py
│ ├── chunker.py
│ ├── embedder.py
│ └── retriever.py
├── uploads/ # Uploaded PDFs
└── requirements.txt

---

## How to Run Locally

### 1. Install dependencies

```bash
pip install -r requirements.txt

streamlit run app.py

http://localhost:8501

## Tech Stack

- This project is intended for learning and experimentation:
- No persistent vector database (indexes rebuilt on each run)
- Uses lightweight local LLM (not optimized for complex reasoning)
- Resume parsing is heuristic-based and depends on PDF formatting
- No authentication or user sessions
- Not optimized for large documents or concurrent users
- No automatic evaluation of answer quality

## Learning Objectives

- This project was built to learn and practice:
- How RAG systems work internally
- Why retrieval can fail even with correct documents
- How chunking strategies affect answer quality
- How routing improves multi-document QA systems
- When LLMs should and should not be used
- How to design modular AI pipelines
- How AI product behavior differs from simple chatbots