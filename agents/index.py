from langchain.agents import initialize_agent, AgentType
from tools import generate_tools
from models import generate_llm
from prompts import generate_prompt

def exec_agent(user_input, debug_info, chat_history):
    tools = generate_tools()
    llm = generate_llm()
    agent = initialize_agent(
        tools = tools,
        llm = llm,
        agent = AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
        verbose = True
    )
    prompt = generate_prompt(user_input)
    agent.invoke({
        "input": prompt
    })

if __name__ == "__main__":
    exec_agent("我要去北京", "", [])