from dotenv import load_dotenv
from openai import OpenAI
import os
load_dotenv()

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("OPENAI_API_KEY")
)
