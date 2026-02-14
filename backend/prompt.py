def build_prompt(context_chunks, user_question):
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
