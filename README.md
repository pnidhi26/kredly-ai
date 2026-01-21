<!--
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
-->

# Kredly AI
### Klaro — powered by Kredly Document Intelligence

## Overview

A free, open-source document intelligence system using Retrieval Augmented Generation (RAG) with OCR, conflict detection, and confidence scoring.

Klaro is a AI-powered Document Intelligence platform that allows users to upload unstructured documents (PDFs, images, text) and ask natural language questions with evidence-backed, explainable answers.

Unlike typical RAG solutions, Klaro App is designed for correctness, transparency, and trust, making it suitable for real enterprise use cases such as compliance, fintech, legal, and risk analysis.


## ✨ Key Features
- 📄 Multi-format document ingestion (PDF, Image, TXT)
- 🔍 Semantic search using vector embeddings (ChromaDB)
- 🧠 Retrieval-Augmented Generation (RAG) with strict grounding
- 📊 Confidence scoring based on semantic distance
- ⚠️ Automatic conflict detection across documents
- 🧾 “Why this answer?” explainability panel
- 📤 Export answers as PDF (enterprise-ready)
- 🎨 SaaS-grade simple UI platform


## 🧠 Why Kredly AI?
Most RAG systems answer confidently even when documents:
- contradict each other
- lack sufficient evidence
- contain ambiguous policies

Kredly AI was built to surface uncertainty instead of hiding it.

## 🏗️ Architecture Overview
```bash
Document → OCR → Chunking → Embeddings → Vector DB → Retrieval → Prompt Injection → LLM Answer

Upload Docs → OCR / Parsing → Chunking → Embeddings
      ↓
Vector Store (ChromaDB)
      ↓
User Question
      ↓
Retrieval → Reasoning → Conflict Detection
      ↓
Answer + Confidence + Sources + Explanation
```

## 🎯 Use Cases
- Fintech & compliance policy analysis
- Customer support knowledge systems
- Legal & contract review
- Fraud & risk document comparison
- Internal enterprise document Q&A

## Project Structure
```bash
klaro-ai/
├── app.py                     # Streamlit entrypoint
├── requirements.txt           # Python dependencies
├── Dockerfile                 # Deployment config (Hugging Face / Docker)
├── run.sh                     # Startup script for Spaces
├── README.md                  # Project documentation
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

### 🚀 Tech Stack
- Frontend: Streamlit (custom dark theme)
- LLM: Open-source Hugging Face models
- Vector DB: ChromaDB
- OCR: Tesseract
- PDF Parsing: pdfplumber
- Explainability: Custom scoring + attribution logic
- Deployment: Hugging Face Spaces

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
## Demo
- Upload a policy document
- Ask natural language questions
- See grounded answers with confidence and sources
- Export answers as PDF

### 📄 Export
Answers can be exported as a PDF including:
- Question
- Answer
- Confidence
- Sources

### 📌 Status
Actively evolving. Built as a learning-by-doing deep dive into RAG systems done right.

## Author
**Prakash Nidhi Verma**
