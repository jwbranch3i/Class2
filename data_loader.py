# data_loader.py
# Provides functionality for loading and saving data in JSON format.
# SRP: DataLoader class is responsible for converting data between dict and its string representation in JSON format.

import json
from file_handler import FileHandler


# DataLoader is responsible for converting data between dict and its string representation in JSON format.
# SRP is followed here.
class DataLoader:
    """
    A class that facilitates loading and saving of data in JSON format.

    Attributes:
    - file_handler: An instance of FileHandler class.
    """

    def __init__(self, file_handler: FileHandler):
        self.file_handler = file_handler

    def load_data(self) -> dict:
        data_str = self.file_handler.read()
        if not data_str:
            return {}
        try:
            return json.loads(data_str)
        except json.JSONDecodeError:
            return {}

    def save_data(self, data: dict):
        data_str = json.dumps(data, indent=4)
        self.file_handler.write(data_str)
