from embeddings import embed_query
from vector_store import VectorStore

vs = VectorStore(384)
vs.load()

query = "Who won IPL 2020 final?"
query_vector = embed_query(query)

results = vs.search(query_vector, top_k=2)

for r in results:
    print("-----")
    print(r["content"])
