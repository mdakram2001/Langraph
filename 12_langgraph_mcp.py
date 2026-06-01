from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.tools import tool
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
import asyncio

#======================================================================================================

from dotenv import load_dotenv
load_dotenv()

#===============================================  LLM  ================================================

llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-120b",
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)

#===============================================  TOOLS  ===============================================

@tool
def calculator(num1: float, num2: float, operation: str) -> dict:

    """Performs basic arithmetic operations on two numbers."""

    try:
        if operation == "add":
            result = num1 + num2
        elif operation == "subtract":
            result = num1 - num2
        elif operation == "multiply":
            result = num1 * num2
        elif operation == "divide":
            if num2 == 0:
                return {"error": "Cannot divide by zero"}
            result = num1 / num2
        else:
            return {"error": "Invalid operation. Supported operations are: add, subtract, multiply, divide."}
        return {"result": result}
    
    except Exception as e:
        return {"error": str(e)}
    
#===============================================  LLM with Tools  ==========================================

tools = [calculator]
llm_with_tools = model.bind_tools(tools)

#===============================================  STATE  ===================================================

class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

def build_graph():
    chatbot=""
    return chatbot

async def main():
    chatbot = build_graph()