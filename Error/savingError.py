

class SavingError(Exception):
    """
    Custom exception for file saving errors.
    """

    def __init__(self, message, code):
        # Call the parent constructor with the message
        super().__init__(message)
        self.message = message
        self.code = code

    def __str__(self):
        # Return a custom string representation of the error
        return f"Error {self.code}: {self.message}"
