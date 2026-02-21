import faiss
import numpy as np
import pickle
import os

INDEX_PATH = os.path.join("data", "processed", "faiss_index.bin")
METADATA_PATH = os.path.join("data", "processed", "chunks.pkl")


class VectorStore:
    def __init__(self, dimension):
        self.dimension = dimension
        self.index = faiss.IndexFlatIP(dimension)  # Inner Product (since normalized)
        self.chunks = []

    def add_embeddings(self, embeddings, chunks):
        self.index.add(embeddings)
        self.chunks.extend(chunks)

    def save(self):
        faiss.write_index(self.index, INDEX_PATH)
        with open(METADATA_PATH, "wb") as f:
            pickle.dump(self.chunks, f)

    def load(self):
        self.index = faiss.read_index(INDEX_PATH)
        with open(METADATA_PATH, "rb") as f:
            self.chunks = pickle.load(f)

    def search(self, query_vector, top_k=3):
        query_vector = np.array([query_vector])
        scores, indices = self.index.search(query_vector, top_k)

        results = []
        for score, idx in zip(scores[0], indices[0]):
            print("Chunk at idx:", idx, "->", self.chunks[idx])
            if idx < len(self.chunks):
                results.append({
                    "score": float(score),
                    "content": self.chunks[idx]["content"],
                    "metadata": self.chunks[idx]["metadata"]
                })

        return results
