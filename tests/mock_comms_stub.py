from src.communication import CommsProtocol

class CommsStub(CommsProtocol):
    def __init__(self, expected_code, expected_time, expected_value) -> None:
        self.command_sent = None
        self.code = expected_code
        self.time = expected_time
        self.value = expected_value

    def send_command(self, command: str) -> None:
        self.command_sent = command

    def read_connection(self) -> str:
        return f"{self.code}: {self.time}, {self.value}"