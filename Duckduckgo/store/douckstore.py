import os
import json
from datetime import datetime

class FileMemory:
    """
    A class to manage file-based memory for storing and retrieving search history.

    Attributes:
        filename (str): The path to the file where search history is stored.
        history (list): A list of dictionaries containing search history items.
    """

    def __init__(self, filename="Duckduckgo/Data/searchHistory.json"):
        """
        Initializes the FileMemory instance.

        Args:
            filename (str): The path to the file where search history is stored. Defaults to "Duckduckgo/Data/searchHistory.json".
        """
        self.filename = filename
        self.history = self.load_memory()

    def load_memory(self):
        """
        Loads the search history from the file.

        Returns:
            list: A list of dictionaries containing search history items. Returns an empty list if the file does not exist or is invalid.
        """
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
        """
        Saves the current search history to the file.

        Returns:
            None
        """
        with open(self.filename, "w") as f:
            json.dump(self.history, f, indent=4)

    def add_history(self, context):
        """
        Adds a new search history item with the given context and the current date.

        Args:
            context (str): The context or search term to add to the history.

        Returns:
            None
        """
        self.history.append({"context": context, "date": datetime.now().isoformat()})
        self.save_memory()

    def clear_memory(self):
        """
        Clears the search history and saves an empty list to the file.

        Returns:
            None
        """
        self.history = []
        self.save_memory()
