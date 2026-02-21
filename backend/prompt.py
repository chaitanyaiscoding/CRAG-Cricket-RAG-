def build_prompt(context_chunks, user_question):
    print("[DEBUG] build_prompt input context_chunks:", context_chunks)
    print("[DEBUG] build_prompt input user_question:", user_question)
    context_text = "\n\n".join(
        [chunk["content"] for chunk in context_chunks]
    )

    prompt = f"""
You are a professional cricket analyst.

Use ONLY the provided context.
If answer is not present, say you don't know.

Context:
{context_text}

Question:
{user_question}

Answer in this format:
- Summary
- Key Points
- Conclusion
"""

    return prompt.strip()
