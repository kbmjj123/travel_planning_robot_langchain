from langchain_core.prompts import PromptTemplate

from prompts.constants import agent_prompt_template
from utils import get_current_local_datetime


def generate_prompt(user_input: str):
    current_time = get_current_local_datetime()
    """生成全局唯一提示词"""
    prompt_template = PromptTemplate.from_template(
        template=agent_prompt_template,
    )
    return prompt_template.format(user_input=user_input, current_time=current_time)

if __name__ == '__main__':
    print(generate_prompt("我要去北京"))