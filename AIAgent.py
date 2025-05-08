from Components import StartChatCom, StartDouckSearch

import asyncio
from rich.console import Console

console = Console()

def main():
    """
    The main function serves as the entry point for the AI application.

    It provides a user interface using the rich.console module to display options and take user input.

    Functionality:
    1. Displays a welcome message and menu options.
    2. Allows the user to choose between chatting or searching (future feature).
    3. Handles user input and calls the appropriate functions:
       - Option 1: Initiates a chat session using StartChatCom.startChat().
       - Option 2: Initiates a search using StartDouckSearch.newSeacrh() (future feature).
    4. Exits the application if the user inputs specific stop commands ("buy", "exit", "stop").

    Note: The function runs in an infinite loop until the user chooses to exit.
    """
    while True:
        console.print("""[bold magenta]
         ===========================
         =    Welcom To My AI     =
         ===========================
        Choose 1) to chat more 2) to search futures is comeing soon
         [/bold magenta]""")

        userChoose = int(console.input("[bold cyan]Choose: [/bold cyan]").strip())

        stopApp = ["buy", "exit", "stop"]

        if userChoose in stopApp:
            console.print("[bold red]By Panda, I see you soon! [/bold red]")
            return False

        if userChoose == 1 :
            console.clear()
            asyncio.run(StartChatCom.startChat())
        elif userChoose == 2:
            console.clear()
            StartDouckSearch.newSeacrh()

if __name__ == "__main__":
    main()