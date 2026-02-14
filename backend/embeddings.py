from sentence_transformers import SentenceTransformer
import numpy as np

# Load model once (global)
model = SentenceTransformer("BAAI/bge-small-en")


def embed_texts(texts):
    """
    Takes list of strings
    Returns numpy array of embeddings
    """
    embeddings = model.encode(
        texts,
        normalize_embeddings=True
    )
    return np.array(embeddings)


def embed_query(query):
    """
    Embed single query
    """
    embedding = model.encode(
        query,
        normalize_embeddings=True
    )
    return np.array(embedding)
