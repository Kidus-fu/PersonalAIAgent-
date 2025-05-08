import webbrowser
import pyttsx3

engine = pyttsx3.init()

def voice(message: str) -> any:
    engine.say(message)
    engine.setProperty('rate', 120)
    engine.runAndWait()

if __name__ == "__main__":
    while True:
        message = input("Say world: ").strip()
        if message:
            voice(message)

