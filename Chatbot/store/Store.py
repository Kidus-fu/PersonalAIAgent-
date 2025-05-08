import os
import json
import uuid

class FileMemory:
    def __init__(self, filename='Chatbot/Data/chat_memory.json'):
        self.filename = filename
        self.historydatapath = "Chatbot/Data/history.txt"
        self.history = self.load_memory()
        self.historydataget = self.loadhistorydata()
        
    def load_memory(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                try:
                    data = f.read()
                    if not data.strip():
                        return []
                    return json.loads(data)
                except json.JSONDecodeError:
                    return []
        return []
    
    def save_memory(self):
        with open(self.filename, 'w') as f:
            json.dump(self.history, f, indent=4)

    def add_message(self, role, content, response_metadata):
        self.history.append({"role": role, "content": content, "response_metadata": response_metadata})
        self.save_memory()
        
    def loadhistorydata(self):
        if os.path.exists(self.historydatapath):
            with open(self.historydatapath, 'r') as f:
                data = f.read()
                if not data.strip(): 
                    return []
                splitdata = data.split("\n") 
                return splitdata 
        return []


    def savehistorydata(self):
        with open(self.historydatapath, 'w') as f:
            json.dump(self.historydataget, f, indent=4)
            
    def savehistorydata(self):
        if os.path.exists(self.historydatapath):
            with open(self.historydatapath, 'w') as f:
                for entry in self.historydataget:
                    f.write(entry + "\n")
        else:
            with open(self.historydatapath, 'w') as f:
                defualt_history = ["clearmymessage","clearit","exit","buy","stop"]
                for defualt in defualt_history:
                    f.write(defualt + "\n")
                for entry in self.get_historydata:
                    f.write(entry + "\n")

    def get_historydata(self):
        return self.historydataget

    def add_history(self, content: str):

        self.historydataget.append(content)
        self.savehistorydata()

    def clear_memory(self):
        self.history = []
        self.historydataget = ["clearmymessage","clearit","exit","buy","stop"]
        self.savehistorydata()
        self.save_memory()

    def get_history(self):
        return self.history
