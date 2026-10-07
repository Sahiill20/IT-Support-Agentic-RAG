from app.services.ingestion import load_file, chunk_documents
from pathlib import Path
from app.rag.vectorStore import add_docs

docs = load_file(Path("data/sample_knowledge_base/service_desk_runbook.md"))
chunks = chunk_documents(docs)

add_docs(chunks)
