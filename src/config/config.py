import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq   # or ChatOpenAI / ChatOllama depending on your setup

load_dotenv()

class Config:
    # API KEY (Groq example)
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

    # Model
    LLM_MODEL = "llama-3.1-8b-instant"

    # Chunk settings
    CHUNK_SIZE = 500
    CHUNK_OVERLAP = 50

    # ✅ Add default URLs (required by your Streamlit app)
    DEFAULT_URLS = [
        "https://lilianweng.github.io/posts/2023-06-23-agent/",
        "https://lilianweng.github.io/posts/2024-04-12-diffusion-video/"
    ]

    @classmethod
    def get_llm(cls):
        return ChatGroq(
            model=cls.LLM_MODEL,
            temperature=0.2,
            api_key=cls.GROQ_API_KEY
        )
