def rag_prompt(context, question):
    return f"""
Use ONLY the context below to answer the question.
If the answer is not present, say "I don't know".

Context:
{context}

Question:
{question}

Answer:
"""
