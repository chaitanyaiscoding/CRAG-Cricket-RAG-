import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/ask"

st.title("🏏 CRAG - Cricket RAG Assistant")

question = st.text_input("Ask a cricket question:")

if st.button("Ask") and question:
    response = requests.post(API_URL, json={"question": question})

    if response.status_code == 200:
        data = response.json()

        st.subheader("Answer")
        st.write(data["answer"])

        st.subheader("Retrieved Context")
        for chunk in data["retrieved"]:
            st.write("Similarity Score:", chunk["score"])
            st.write(chunk["metadata"])
            st.write(chunk["content"])
            st.divider()
    else:
        st.error("API Error")