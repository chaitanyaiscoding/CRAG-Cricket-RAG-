from ingestion import load_raw_data, convert_to_documents
from chunking import create_chunks
from embeddings import embed_texts

df = load_raw_data()
docs = convert_to_documents(df)
chunks = create_chunks(docs)

texts = [chunk["content"] for chunk in chunks]

vectors = embed_texts(texts)

print("Number of chunks:", len(texts))
print("Embedding shape:", vectors.shape)

# for x in vectors:
#     print(x)