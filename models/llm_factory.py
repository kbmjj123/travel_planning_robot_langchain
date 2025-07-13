from langchain.agents import load_agent
from langchain_community.chat_models import ChatTongyi
load_agent()
def generate_llm(model_name: str, temperature: float = 0.0, max_tokens: int = 1024):
    """生成一LLM模型"""
    return ChatTongyi(model=model_name, temperature=temperature, max_tokens=max_tokens)