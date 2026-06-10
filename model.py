from langchain.chat_models import init_chat_model

from dotenv import load_dotenv
import os

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

llm = init_chat_model(

    model="openai/gpt-oss-120b",

    model_provider="groq",

    groq_api_key=GROQ_API_KEY,

    temperature=0.3
)