from transformers import pipeline
from .vector_store import search
from .prompts import rag_prompt

generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
    max_length=512
)

def answer_question(question):
    # STEP 4: search now returns docs, distances, metadatas
    docs, distances, metadatas = search(question)

    context = "\n\n".join(docs)

    prompt = rag_prompt(context, question)
    result = generator(prompt)[0]["generated_text"]

    # Return everything UI needs
    return result, docs, distances, metadatas
