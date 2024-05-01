from typing import Protocol, NoReturn

class CommsProtocol(Protocol):
    def send_command(self, command:str) -> NoReturn:
        """
        Send received command via connection.

        Returns:
            None
        """
        pass

    def read_connection(self) -> str:
        """
        Read connection buffer and return result.

        Returns:
            str: The entire message buffer as a string
        """
        pass


class CommsFactory:
    def __init__(self, comms_dict: dict[str: CommsProtocol]) -> None:
        self._known_connections = comms_dict

    def create_comms(self, type:str) -> CommsProtocol:
        connection_constructor = self._known_connections[type]
        conn = connection_constructor()
        return conn