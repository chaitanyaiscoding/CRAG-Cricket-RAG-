from .embeddings import embed_query
from .vector_store import VectorStore
from .prompt import build_prompt
from .llm import generate_response


def run_rag(question, vector_store):
    try:
        print("[DEBUG] Question:", question)
        # 1. Embed query
        query_vector = embed_query(question)
        print("[DEBUG] Query vector:", query_vector)

        # 2. Retrieve
        retrieved_chunks = vector_store.search(query_vector, top_k=3)
        print("[DEBUG] Retrieved chunks:", retrieved_chunks)

        # 3. Build context
        context = "\n\n".join([chunk["content"] for chunk in retrieved_chunks])
        print("[DEBUG] Context:", context)

        # 4. Build prompt
        try:
            prompt = build_prompt(retrieved_chunks, question)
            print("[DEBUG] Prompt:", prompt)
        except Exception as e:
            print("[ERROR] Exception in build_prompt:", e)
            return {"error": f"build_prompt error: {str(e)}"}

        # 5. Generate answer
        try:
            answer = generate_response(prompt)
            print("[DEBUG] Answer:", answer)
        except Exception as e:
            print("[ERROR] Exception in generate_response:", e)
            return {"error": f"generate_response error: {str(e)}"}

        return {
            "answer": answer,
            "retrieved": retrieved_chunks
        }
    except Exception as e:
        print("[ERROR] Exception in run_rag:", e)
        return {"error": str(e)}