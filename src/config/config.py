@classmethod
def get_llm(cls):
    if not cls.GROQ_API_KEY:
        raise RuntimeError(
            "GROQ_API_KEY is not set. "
            "Make sure it is configured in Cloud Run environment variables."
        )

    return ChatGroq(
        model=cls.LLM_MODEL,
        temperature=0.2,
        api_key=cls.GROQ_API_KEY
    )
