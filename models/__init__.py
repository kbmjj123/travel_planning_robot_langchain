"""对外提供的工厂方法，根据model名称来获取对应的llm"""
__ALL__ = [
    "generate_llm"
]
from .llm_factory import generate_llm