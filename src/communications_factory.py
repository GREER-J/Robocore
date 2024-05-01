from src.communication import CommsProtocol

class CommsFactory:
    def __init__(self, comms_dict: dict[str: CommsProtocol]) -> None:
        self._known_connections = comms_dict

    def create_comms(self, type:str, **kwargs) -> CommsProtocol:
        connection_constructor = self._known_connections[type]
        conn = connection_constructor(**kwargs)
        return conn