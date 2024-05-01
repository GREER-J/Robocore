from src.actuators import PwmOutput
from src.communication import CommsProtocol
import pytest

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

def test_can_set_current_val():
    dummy_comms = CommsStub('a', 2, 4)
    actuator = PwmOutput(0, 6, 'a', dummy_comms)
    volts = 2
    actuator.set_actuator_command(volts)
    assert actuator.current_val == volts, "Actuator should store the command voltage accurately"

def test_when_voltage_over_max_raises_error():
    dummy_comms = CommsStub('a', 2, 4)
    actuator = PwmOutput(0, 6, 'a', dummy_comms)
    with pytest.raises(ValueError):
        actuator.set_actuator_command(7)

def test_when_voltage_over_min_raises_error():
    dummy_comms = CommsStub('a', 2, 4)
    actuator = PwmOutput(0, 6, 'a', dummy_comms)
    with pytest.raises(ValueError):
        actuator.set_actuator_command(-1)

def test_voltage_type():
    dummy_comms = CommsStub('a', 2, 4)
    actuator = PwmOutput(0, 6, 'a', dummy_comms)
    with pytest.raises(TypeError):
        actuator.set_actuator_command("High")  # Non-numeric input should raise an error

def test_schedule_setpoint():
    pass