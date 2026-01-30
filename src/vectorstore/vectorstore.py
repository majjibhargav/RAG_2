from typing import List
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.documents import Document

class VectorStore:

    def __init__(self):
        # ✅ FREE local embeddings (no API key needed)
        self.embedding = HuggingFaceEmbeddings(
            model_name="all-MiniLM-L6-v2"
        )

        self.vectorstore = None
        self.retriever = None

    def create_vectorstore(self, documents: List[Document]):
        self.vectorstore = FAISS.from_documents(documents, self.embedding)
        self.retriever = self.vectorstore.as_retriever(search_kwargs={"k": 4})

    def get_retriever(self):
        if self.retriever is None:
            raise ValueError("Vector store not initialized.")
        return self.retriever

    def retrieve(self, query: str, k: int = 4) -> List[Document]:
        if self.retriever is None:
            raise ValueError("Vector store not initialized.")
        return self.retriever.invoke(query)
