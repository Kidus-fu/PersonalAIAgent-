import asyncio
import json
import os
from getpass import getpass

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from rich.console import Console

from ..store.Store import FileMemory

load_dotenv()

console = Console()
memore = FileMemory()

async def ChatModelStructed(message: str, more: str = "conversation") -> str | bool:
    """ This is a simple LLM Chat model powred by Groq Ai """

    message = message.lower()

    memore.add_message("user", message, {})

    if not os.environ.get("GROQ_API_KEY"):
        os.environ["GROQ_API_KEY"] = getpass("Enter API key for Groq: ")

    stopchat_messages = ["buy", "exit", "stop"]
    
    if message in stopchat_messages:
        console.print("[bold red]By Panda, I see you soon! [/bold red]")
        return False

    clearmessage = ["clearmymessage","clearit"]
    
    if message in clearmessage:
        console.clear()
        memore.clear_memory()
        result = AIMessage("Ok, I cleared your previous data. Ask anything freely.",response_metadata={"status": "OK","status_code":200})
        return result.content
    # Build chat history for context
    messages = []
    for msg in memore.get_history():
        if msg['role'] == 'user':
            messages.append(HumanMessage(content=msg['content']))
        else:
            messages.append(AIMessage(content=msg['content']))

    # System message
    system_message : str = """
    You are a personal AI assistant created to help Panda, a 16-year-old self-taught developer from Ethiopia. 
    Always be supportive, friendly, and help Panda learn code, AI, or solve problems.
    {more}
    """

    prompt_template = ChatPromptTemplate.from_messages([
        ("system", system_message),
        ("user", "{text}")
    ])

    # Format the full message
    formatted_prompt = prompt_template.invoke({"more": more, "text": message})

    # Initialize LLM
    llm = init_chat_model("llama3-8b-8192", model_provider="groq")

    # Add system and prompt to message list
    full_messages = [SystemMessage(content=system_message.format(more=more))] + messages + [HumanMessage(content=message)]

    # AI reply
    result = await llm.ainvoke(full_messages)

    if result.content:
        memore.add_message("assistant", result.content,result.response_metadata)
        return result.content

