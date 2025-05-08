from Duckduckgo.Model.DouckDuckgoModel import Search

def newSeacrh():
    while True:
        try: 
            userpromet = input("Search in Douck: ").lower()
            stopSearch_messages = ["buy", "exit", "stop"]

            if userpromet in stopSearch_messages:
                return False
            if len(userpromet) <= 0:
                continue
            Search(text=userpromet)
        except:
            break