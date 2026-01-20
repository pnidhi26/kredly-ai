---
title: Kredly Ai
emoji: 👀
colorFrom: red
colorTo: gray
sdk: docker
pinned: false
license: mit
short_description: Document Intelligence using RAG with OCR, conflict detection
---

# Kredly AI
### Klaro — powered by Kredly Document Intelligence

## Overview
Kredly AI is a SaaS-grad, open-source **Document Intelligence platform** built using Retrieval-Augmented Generation (RAG).

It allows users to upload unstructured documents (PDFs, images, text) and ask natural language questions with **evidence-backed, explainable answers**.

Unlike basic RAG demos, Kredly AI prioritizes:
- correctness over fluency
- explicit uncertainty
- multi-document conflict detection

## Key Features
- 📄 OCR for PDFs and images
- 🔍 Semantic search using vector embeddings
- 🧠 Grounded question answering (RAG)
- 📊 Confidence scoring based on semantic similarity
- ⚠️ Conflict detection across documents
- 🧾 Explainability (“Why this answer?”)
- 📤 Export answers as PDF
- 💻 Fully free and open-source (no paid APIs)

---
## Project Structure
```bash
klaro-ai/
│
├── app/
│   ├── __init__.py
│   ├── ui.py                  # Main UI orchestration
│   ├── ui_components.py       # Reusable UI blocks
│   ├── rag_pipeline.py        # Core RAG logic
│   ├── ingestion.py           # File ingestion + OCR
│   ├── chunking.py            # Text chunking logic
│   ├── extraction.py          # Structured extraction
│   ├── reasoning.py           # Numerical / rule-based reasoning
│   ├── vector_store.py        # ChromaDB integration
│   ├── conflict_detection.py  # Cross-document conflict detection
│   ├── consensus.py           # Multi-document consensus logic
│   ├── export.py              # PDF export
│   ├── prompts.py             # RAG prompts
│   └── styles/
│       └── theme.css          # Dark UI theme
│
├── data/
│   └── chroma/                # Local vector DB
│
├── requirements.txt
├── app.py                     # Streamlit entry point
├── run.sh
├── Dockerfile
└── README.md
```

## System Workflow
```bash
Document Upload
   ↓
OCR / Parsing
   ↓
Chunking + Embeddings
   ↓
Vector Database (ChromaDB)
   ↓
Retrieval
   ↓
Reasoning + Conflict Detection
   ↓
RAG Answer Generation
   ↓
Answer + Confidence + Explanation + Sources

```

### Tech Stack
- Python
- Streamlit
- Hugging Face Transformers
- Sentence Transformers
- ChromaDB
- Tesseract OCR
- pdfplumber

### Workflow
Document → OCR → Chunking → Embeddings → Vector DB → Retrieval → Prompt Injection → LLM Answer

### How to run application:

Run Direct link: 
```bash
https://huggingface.co/spaces/pnidhi26/kredly-ai
```
Run Locally
```bash
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## Author
**Prakash Nidhi Verma**
