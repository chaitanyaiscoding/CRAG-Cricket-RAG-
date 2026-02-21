from fastapi import FastAPI
from pydantic import BaseModel
from .vector_store import VectorStore
from .rag_pipeline import run_rag

app = FastAPI(title="CRAG - Cricket RAG API")

vector_store = VectorStore(dimension=384)
vector_store.load()

class QueryRequest(BaseModel):
    question: str

@app.get("/")
def health():
    return {"status": "CRAG running"}

@app.post("/ask")
def ask_question(request: QueryRequest):
    try:
        result = run_rag(request.question, vector_store)
        return result
    except Exception as e:
        print("Error:", e)
        return {"error": str(e)}