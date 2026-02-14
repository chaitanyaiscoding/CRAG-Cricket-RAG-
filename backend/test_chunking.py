from ingestion import load_raw_data, convert_to_documents
from chunking import create_chunks

df = load_raw_data()
docs = convert_to_documents(df)
chunks = create_chunks(docs)

for chunk in chunks:
    print("-----")
    print(chunk["content"])
