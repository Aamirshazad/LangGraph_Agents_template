from langgraph.prebuilt import create_react_agent
from langchain.chat_models import init_chat_model

def suma():
    """this is sum tools"""
    pass


model = init_chat_model()

graph = create_react_agent(
    tools=[suma],
    model=model

)