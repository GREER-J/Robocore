from typing import Protocol, NoReturn


class CommsProtocol(Protocol):
    def send_command(self, command: str) -> NoReturn:
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
