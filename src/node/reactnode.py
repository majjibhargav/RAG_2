from typing import List
from src.state.rag_state import RAGState


class RAGNodes:

    def __init__(self, retriever, llm):
        self.retriever = retriever
        self.llm = llm

    def retrieve_docs(self, state: RAGState) -> RAGState:
        docs = self.retriever.invoke(state.question)
        return RAGState(question=state.question, retrieved_docs=docs)

    def generate_answer(self, state: RAGState) -> RAGState:
        # Build context
        context = "\n\n".join([d.page_content for d in state.retrieved_docs[:4]])

        prompt = f"""
You are a helpful AI assistant. Answer the question using ONLY the context.

Context:
{context}

Question: {state.question}
Answer:
"""

        response = self.llm.invoke(prompt)

        return RAGState(
            question=state.question,
            retrieved_docs=state.retrieved_docs,
            answer=response.content
        )
