import time
import os
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from langchain_huggingface import HuggingFaceEmbeddings
from app.core.config import get_settings

settings = get_settings()

embeddings = None
vectorStore = None

#if in future you want to use any other models you can use
embedding_dimensions = {
    "sentence-transformers/all-minilm-l6-v2": 384
}

def get_embedding_dimensions(model_name: str | None = None) -> int:
    name = (model_name or settings.EMBEDDING_MODEL or "").strip()
    if not name:
        raise RuntimeError("Embedding Model is not configured")

    normalized = name.lower()

    if normalized in embedding_dimensions:
       return embedding_dimensions[normalized]

    raise ValueError(
        f"Unsuported embedding model '{model_name or settings.EMBEDDING_MODEL}' for Pinecone."
        "Add the matching dimension to embedding_dimensions"
    )

def get_embeddings():
    global embeddings
    if embeddings is None:
        if not settings.HUGGINGFACEHUB_API_TOKEN:
            raise RuntimeError("HUGGINGFACEHUB_API_TOKEN is missing")
        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2",
            encode_kwargs={"normalize_embeddings": True},
        ) 
    return embeddings


def create_index():
    if not settings.PINECONE_API_KEY:
        raise RuntimeError("PINECONE_API_KEY is missing")

    desired_dimension = get_embedding_dimensions()

    pc = Pinecone(api_key=settings.PINECONE_API_KEY)
    names = [x['name'] for x in pc.list_indexes()]

    if settings.PINECONE_INDEX_NAME in names:
        index_info = pc.describe_index(settings.PINECONE_INDEX_NAME)
        current_dimension = getattr(index_info, "dimension", None)
        if current_dimension is None and isinstance(index_info, dict):
            current_dimension = index_info.get("dimension")

        if current_dimension is not None and current_dimension != desired_dimension:
            pc.delete_index(name=settings.PINECONE_INDEX_NAME)
            while settings.PINECONE_INDEX_NAME in [x["name"] for x in pc.list_indexes()]:
                time.sleep(1)

    if settings.PINECONE_INDEX_NAME not in [x["name"] for x in pc.list_indexes()]:
        pc.create_index(
            name=settings.PINECONE_INDEX_NAME,
            dimension=desired_dimension,
            metric="cosine",
            spec=ServerlessSpec(cloud="aws", region="us-east-1"),
        )
        while not pc.describe_index(settings.PINECONE_INDEX_NAME).status["ready"]:
            time.sleep(1)

    return pc.Index(settings.PINECONE_INDEX_NAME)


def get_vectorstore():
    global vectorStore
    if vectorStore is None:
        index = create_index()
        vectorStore = PineconeVectorStore(
            index=index,
            embedding=get_embeddings(),
            namespace=settings.PINECONE_NAMESPACE,
        )
    return vectorStore


def get_retriever():
    retriever = get_vectorstore().as_retriever(
        search_kwargs={
            "k": 4,
            "namespace": settings.PINECONE_NAMESPACE,
        }
    )
    return retriever

def add_docs(chunks):
    store = get_vectorstore()
    return store.add_documents(chunks)