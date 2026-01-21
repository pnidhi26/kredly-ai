# kredly-ai
### Klaro — powered by Kredly Document Intelligence

---
## Project Structure
```bash
klaro-ai/
│
├── app/
│   ├── __init__.py
│   ├── main.py                # Streamlit entry point
│   ├── ui.py                  # UI layout and components
│   ├── rag_pipeline.py        # Core RAG logic
│   ├── ingestion.py           # File ingestion + OCR
│   ├── chunking.py            # Text chunking logic
│   ├── embeddings.py          # Embedding model wrapper
│   ├── vector_store.py        # Chroma DB logic
│   └── prompts.py             # RAG prompts
│
├── data/
│   ├── uploads/               # Uploaded raw files
│   └── chroma/                # Local vector DB
│
├── models/
│   └── README.md              # Model choices and notes
│
├── scripts/
│   └── reset_db.py            # Utility to reset vector DB
│
├── requirements.txt
├── README.md
├── .gitignore
└── run.sh

```
---
## Overview
A free, open-source document intelligence system using Retrieval Augmented Generation (RAG).

### Features
- OCR for PDFs and images
- Semantic search using vector embeddings
- Grounded question answering
- Local-first, no paid APIs

### Workflow
Document → OCR → Chunking → Embeddings → Vector DB → Retrieval → Prompt Injection → LLM Answer

### Tech Stack
- Python
- Streamlit
- Sentence Transformers
- ChromaDB
- HuggingFace Transformers

### Run
source venv/bin/activate
pip install -r requirements.txt
streamlit run main.py

--- 
## Author
**Prakash Nidhi Verma**