from Components.StartChatCom import startChat

import asyncio
from rich.console import Console

console = Console()

def main():
    while True:
        console.print("""[bold magenta]
         ===========================
         =    Welcom To My AI     =
         ===========================
        Choose 1 to chat more futures is comeing soon
         [/bold magenta]""")

        userChoose = int(console.input("[bold cyan]Choose: [/bold cyan]").strip())

        stopApp = ["buy", "exit", "stop"]

        if userChoose in stopApp:
            console.print("[bold red]By Panda, I see you soon! [/bold red]")
            return False

        if userChoose == 1 :
            
            console.clear()
            asyncio.run(startChat())


if __name__ == "__main__":
    main()