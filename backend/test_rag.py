from rag_pipeline import run_rag

query = "Who won IPL 2020 final?"
response = run_rag(query)

print(response)
