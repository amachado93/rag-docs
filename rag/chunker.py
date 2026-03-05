from pathlib import Path

def load_documents(docs_path: str):
    docs = []
    for path in Path(docs_path).glob("**/*"):
        if path.suffix in [".md", ".txt"]:
            with open(path, "r", encoding="utf-8") as f:
                docs.append({
                    "text": f.read(),
                    "source": str(path)
                })
    return docs

def chunk_text(text, chunk_size=500, overlap=100):
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start += chunk_size - overlap

    return chunks

def chunk_documents(docs):
    results = []

    for doc in docs:
        chunks = chunk_text(doc["text"])
        for chunk in chunks:
            results.append({
                "text": chunk,
                "source": doc["source"]
            })

    return results
