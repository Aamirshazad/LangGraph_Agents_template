from langgraph.prebuilt import create_react_agent
from langchain.chat_models import init_chat_model
from src.email_assistant.tools.default.email_tools import search_files


model = init_chat_model("openai:gpt-4.1")

system_prompt = """You are a helpful assistant that can search for files."""

graph = create_react_agent(
    model=model,
    tools=[search_files],
    prompt=system_prompt

)
