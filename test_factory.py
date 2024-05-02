from src.communication import CommsProtocol
from src.sensors import AnalogueSensor


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

# def test_sensor_create_analog():

    # sensor = SensorFactory(sensor_config)
    # assert type(sensor) ==


s = AnalogueSensor('A', CommsStub('A', 1, 1))
print(type(s))
