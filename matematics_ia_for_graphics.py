import requests
import json


class MatematicaIAForGraphics:
    def __init__(self):
        self.PROMPT_MESTRE_TEMPLATE = None
        self.OLLAMA_API_URL = "http://localhost:11434/api/generate"

    def configuring_prompt(self, pergunta : str):
        pass

    def run_code(self, code : str):
        pass


