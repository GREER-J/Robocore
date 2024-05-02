from src.communication import CommsProtocol


class SimConnection(CommsProtocol):
    def __init__(self, command_fun: callable) -> None:
        self._conn = command_fun
        self.buffer = ""

    def convert_to_response_format(self, code: int, time: float, value: float) -> str:
        return f"{code}: {time}, {value}"

    def send_command(self, command: str) -> None:
        rv = self._conn(command)
        self.buffer += rv

    def read_connection(self) -> str:
        buffer = self.buffer
        self.buffer = ""
        return buffer
