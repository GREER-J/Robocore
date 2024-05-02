from typing import Protocol

class ConfigReaderProtocol(Protocol):
    def read_config(self, config_path: str) -> dict:
        pass