from embeddings import embed_query
from vector_store import VectorStore
from prompt import build_prompt
from llm import generate_response


def run_rag(query):
    # Load vector store
    vs = VectorStore(384)
    vs.load()

    # Embed query
    query_vector = embed_query(query)

    # Retrieve
    results = vs.search(query_vector, top_k=3)

    # Build prompt
    prompt = build_prompt(results, query)

    # Generate answer
    answer = generate_response(prompt)

    return answer
