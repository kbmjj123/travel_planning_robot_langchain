from langchain.agents import AgentExecutor, create_react_agent
from tools import generate_tools
from models import generate_llm
from prompts import generate_prompt
from utils import get_current_local_datetime
import logging
logging.basicConfig(level=logging.NOTSET)
def exec_agent(user_input, debug_info, chat_history):
    tools = generate_tools()
    llm = generate_llm("qwen-max")
    llm_with_tools = llm.bind_tools(tools)
    current_time = get_current_local_datetime()
    prompt = generate_prompt()
    agent = create_react_agent(llm=llm_with_tools, tools=tools, prompt=prompt)
    agent_executor = AgentExecutor.from_agent_and_tools(agent=agent, tools=tools, verbose=True, handle_parsing_errors=True)
    for chunk in agent_executor.stream({
        "input": user_input,
        "current_time": current_time,
        "chat_history": "\n".join(chat_history)
    }):
        print(chunk)

if __name__ == "__main__":
    exec_agent("请帮我制定一个汕头市7日双人游的旅游方案", "", [])
