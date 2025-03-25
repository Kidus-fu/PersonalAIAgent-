import os 
import json

import uuid
class FileMemory:
    def __init__(self, filename='Chatbot/Data/chat_memory.json'):
        self.filename = filename 
        self.history = self.load_memory()
        
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
        self.history.append({"role": role, "content": content, " response_metadata": response_metadata})
        self.save_memory()

    def clear_memory(self):
        self.history = []
        self.save_memory()

    def get_history(self):
        return self.history
