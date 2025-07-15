from langchain_core.prompts import PromptTemplate

from prompts.constants import agent_prompt_template


def generate_prompt():
    """生成全局唯一提示词"""
    prompt_template = PromptTemplate.from_template(
        template=agent_prompt_template,
    )
    return prompt_template

if __name__ == '__main__':
    print(generate_prompt("我要去北京"))