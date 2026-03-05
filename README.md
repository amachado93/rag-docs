# RAG Docs — Chat With Documentation

A simple Retrieval-Augmented Generation (RAG) system that allows you to ask questions about documentation using a local LLM.

This project demonstrates the core architecture used in many modern AI systems:

documents → chunking → embeddings → vector search → LLM reasoning

The system indexes documentation files, stores embeddings in a vector database, and retrieves relevant context to answer questions.

---

## Features

- Document ingestion and chunking
- Local embeddings generation
- Vector similarity search
- Retrieval-Augmented Generation (RAG)
- Streaming LLM responses
- Source citations for answers
- CLI interface

---

## Tech Stack

- Python
- Ollama (local LLM runtime)
- Chroma (vector database)
- Llama3 (LLM)
- nomic-embed-text (embedding model)

---

## Project Structure
