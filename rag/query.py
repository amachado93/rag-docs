import chromadb
import ollama
from halo import Halo

# connect to DB
chroma_client = chromadb.PersistentClient(
    path="./db"
)
collection = chroma_client.get_collection(name="docs")

def query_docs(question):

    spinner = Halo(text="Thinking...", spinner="dots")
    spinner.start()

    query_embedding = ollama.embeddings(
        model="nomic-embed-text",
        prompt=question
    )["embedding"]

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )

    docs = results["documents"][0]
    sources = results["metadatas"][0] #shows source citations!

    context = "\n\n".join(docs)

    source_files = {s["source"] for s in sources}

    prompt = f"""
Use the following context to answer the question.

Context:
{context}

Question:
{question}
"""

    stream = ollama.generate(
        model="llama3",
        prompt=prompt,
        stream=True
    )

    spinner.stop()
    print()

    for chunk in stream:
        print(chunk["response"], end="", flush=True)

    print("\n")

    print("\nSources:")
    for src in source_files:
        print(f" - {src}")

if __name__ == "__main__":
    while True:
        question = input("\nAsk a question (or 'exit'): ")

        if question == "exit":
            break

        query_docs(question)
