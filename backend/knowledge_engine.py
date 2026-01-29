def answer_knowledge(question, store, embed_model, llm,memory_text):
    combined=memory_text + " " + question
    q_emb = embed_model.encode([combined])
    retrieved = store.search(q_emb)

    context = " ".join(retrieved)[:800]

    prompt = f"""
Answer using only the context below.

Chat History:
{memory_text}

Context:
{context}

Question:
{question}
"""

    return llm(prompt)[0]["generated_text"]
