# (PDF + OCR + Parsing)

import pdfplumber
from PIL import Image
import pytesseract

from .chunking import chunk_text
from .vector_store import add_chunks
from .extraction import extract_refund_policy, extract_bank_transactions


def extract_text(file):
    if file.type == "application/pdf":
        with pdfplumber.open(file) as pdf:
            return "\n".join(page.extract_text() or "" for page in pdf.pages)

    if file.type.startswith("image"):
        image = Image.open(file)
        return pytesseract.image_to_string(image)

    return file.read().decode("utf-8")


def ingest_files(files):
    structured_outputs = []

    for f in files:
        text = extract_text(f)

        policy = extract_refund_policy(text)
        transactions = extract_bank_transactions(text)

        structured_outputs.append({
            "file_name": f.name,
            "refund_policy": policy,
            "transactions": transactions
        })

        chunks = chunk_text(text)
        add_chunks(chunks, f.name)

    return structured_outputs
