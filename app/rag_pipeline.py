from transformers import pipeline
from .vector_store import search
from .prompts import rag_prompt

generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-base"
)


def answer_question(question, enabled_files=None):
    docs, distances, metas = search(question)

    filtered = [
        (d, dist, m)
        for d, dist, m in zip(docs, distances, metas)
        if enabled_files is None or m["file"] in enabled_files
    ]

    if not filtered:
        return "I don't know", [], [], []

    docs, distances, metas = zip(*filtered)

    best_idx = distances.index(min(distances))
    context = docs[best_idx]

    prompt = rag_prompt(context, question)
    answer = generator(prompt, max_length=128)[0]["generated_text"].strip()

    if not answer:
        answer = "I don't know"

    return answer, list(docs), list(distances), list(metas)
