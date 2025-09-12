from langgraph.prebuilt import create_react_agent
from langchain.chat_models import init_chat_model

model = init_chat_model("anthropic:claude-3-5-sonnet-20241022")

system_prompt = """You are a helpful assistant that can answer questions and have conversations. 
You are friendly, concise, and helpful."""

graph = create_react_agent(
    model=model,
    tools=[],
    prompt=system_prompt
)