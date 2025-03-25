# Chat Model Start Function

from Chatbot.Model.ChatModel import ChatModelStructed

from rich.console import Console

from rich.markdown import Markdown

from rich.spinner import Spinner

from rich.live import Live

console = Console()

async def startChat():
    while True:
        usermessage = console.input("[bold cyan]Message: [/bold cyan]").strip().lower()

        # Display spinner while waiting
        spinner = Spinner("dots", text="[yellow]Thinking...[/yellow]")
        with Live(spinner, refresh_per_second=10):
            result = await ChatModelStructed(message=usermessage)

        if result:
            # Display the AI response beautifully in markdown and color
            console.print(Markdown(f"{result}"),end="\n")
            continue
        break