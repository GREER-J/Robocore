from src.communication import CommsProtocol

class SimConnection(CommsProtocol):
    def __init__(self, commands) -> None:
        self.available_commands = commands
        self.buffer = ""

    def convert_to_response_format(self, code: int, time: float, value: float) -> str:
        return f"{code}: {time}, {value}"

    def send_command(self, command: str) -> None:
        code, fun = self.available_commands[command]
        time, value = fun()

        msg = self.convert_to_response_format(code, time, value)
        
        self.buffer += msg

    def read_connection(self) -> str:
        buffer = self.buffer
        self.buffer = ""
        return buffer
