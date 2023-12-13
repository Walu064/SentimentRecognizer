from pydantic import BaseModel

class ConsoleColors:
    BLUE = '\033[94m'
    RESET = '\033[0m'

class TextFromUser(BaseModel):
    textFromUser : str
