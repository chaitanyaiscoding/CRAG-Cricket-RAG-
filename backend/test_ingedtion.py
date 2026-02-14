from ingestion import load_raw_data, convert_to_documents

df = load_raw_data()
docs = convert_to_documents(df)

for doc in docs:
    print(doc)
