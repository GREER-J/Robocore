import json
from src.config_reader import ConfigReaderProtocol

class JsonConfigReader(ConfigReaderProtocol):
    def __init__(self) -> None:
        pass

    def read_config(self, config_path: str) -> dict:
        # Load the JSON data from a file
        with open(config_path, 'r') as file:
            config = json.load(file)
        return config