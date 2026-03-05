import chromadb
import ollama
from chunker import load_documents, chunk_documents

# connect to vector DB
chroma_client = chromadb.PersistentClient(
    path="./db"
)
collection = chroma_client.get_or_create_collection(name="docs")

docs = load_documents("docs")
chunks = chunk_documents(docs)

for i, chunk in enumerate(chunks):
    embedding = ollama.embeddings(
        model="nomic-embed-text",
        prompt=chunk["text"]
    )["embedding"]

    collection.add(
        ids=[str(i)],
        embeddings=[embedding],
        documents=[chunk["text"]],
        metadatas=[{"source": chunk["source"]}]
    )

print(f"Stored {len(chunks)} chunks in vector DB")
