from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
import asyncio
from rich.markdown import Markdown
from rich.console import Console
from rich.spinner import Spinner
from rich.live import Live
from Chatbot.Model.ChatModel import ChatModelStructed
from Chatbot.store.Store import FileMemory

history_memore = FileMemory()

commandsWord = history_memore.get_historydata()

commands = WordCompleter(commandsWord, ignore_case=True)
session = PromptSession()

console = Console()

async def startChat():
    while True:
        usermessage = await session.prompt_async("Message: ", completer=commands)

        # usermessage = usermessage.strip().lower()
       
        # Display spinner while waiting
        spinner = Spinner("dots", text="[yellow]Thinking...[/yellow]")
        with Live(spinner, refresh_per_second=10):
            history_memore.add_history(content=usermessage)
            result = await ChatModelStructed(message=usermessage)

        if result:
            # Display the AI response beautifully in markdown and color
            console.print(Markdown(result), end="\n")
        else:
            break

# To run the startChat function properly:
async def main():
    await startChat()

if __name__ == "__main__":
    # Use asyncio.get_event_loop() to run the event loop correctly
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
