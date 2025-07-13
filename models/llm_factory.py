from dotenv import load_dotenv
from langchain_community.chat_models import ChatTongyi
import os
load_dotenv()
def generate_llm(model_name: str = None, temperature: float = 0.0, max_tokens: int = 1024):
    """生成一LLM模型"""
    if type(model_name) is None:
        model_name = os.getenv("MODEL")
    return ChatTongyi(model=model_name, temperature=temperature, max_tokens=max_tokens)