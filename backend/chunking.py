def create_chunks(documents):
    chunks = []

    for doc in documents:
        content = f"""
Match: {doc['metadata']['match']}
Tournament: {doc['metadata']['tournament']}
Year: {doc['metadata']['year']}
Stage: {doc['metadata']['stage']}

Summary:
{doc['content']}
"""

        chunk = {
            "content": content.strip(),
            "metadata": doc["metadata"]
        }

        chunks.append(chunk)

    return chunks
