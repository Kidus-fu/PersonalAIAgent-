from duckduckgo_search import DDGS
import webbrowser
import json
from ..store.douckstore import FileMemory
from rich.console import Console

console = Console()
memory = FileMemory()

def Search(text: str):
    """
    Search(text: str)

    Searches DuckDuckGo for the given text and optionally opens the first result in a web browser.

    Parameters:
        text (str): The search query or a command to clear history.

    Returns:
        bool: Returns False if the history is cleared, otherwise None.

    Behavior:
        - If the input text matches one of the clear history commands, it clears the search history and console.
        - Performs a DuckDuckGo search for the input text and prints the top 5 results in JSON format.
        - Adds the search query to memory.
        - Prompts the user to open the first search result link in their default web browser.
    """
    # Search DuckDuckGo
    clearhistory = ["clearmyHistory","clearit","cls"]
    if text in clearhistory:
        memory.clear_memory()
        console.clear()
        console.print("[green] succesfully clear history\n")
        return False
    with DDGS() as ddgs:
        results = ddgs.text(text, max_results=5)
        result = results[0]
        print(json.dumps(results, indent=4))
        
        # Add the context to memory
        memory.add_history(context=text)

        # Ask user for input to open the first link
        userP = input("Do you want to open the first link? (y/n): ").lower().strip()

        if userP != "y":
            return 
        
        webbrowser.open(result['href'])
        console.print("[green ]Opening the link...")