from langchain.agents import AgentExecutor, create_react_agent
from tools import generate_tools
from models import generate_llm
from prompts import generate_prompt
from utils import get_current_local_datetime


def exec_agent(user_input, debug_info, chat_history):
    tools = generate_tools()
    llm = generate_llm()
    current_time = get_current_local_datetime()
    prompt = generate_prompt()
    agent = create_react_agent(llm=llm, tools=tools, prompt=prompt)
    agent_executor = AgentExecutor.from_agent_and_tools(agent=agent, tools=tools, verbose=True)
    agent_executor.invoke({
        "input": user_input,
        "current_time": current_time,
        "chat_history": "\n".join(chat_history)
    })

if __name__ == "__main__":
    exec_agent("请帮我指定一个广东汕头7日双人游的旅游方案", "", [])