import pytest
from src.actuators import PwmOutput
from src.actuator_events import SetpointActuatorEvent
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
    
def test_setpoint_actuation_creation_no_error():
    dummy_comms = CommsStub('a', 2, 4)
    actuator = PwmOutput(0, 6, 'a', dummy_comms)
    setpoint = 2
    program = SetpointActuatorEvent(actuator, 1, 1, setpoint, 0, 0, 0)
    program.process()
    assert actuator.current_val == setpoint

def test_setpoint_actuation_creation_with_error():
    dummy_comms = CommsStub('a', 2, 4)
    actuator = PwmOutput(0, 6, 'a', dummy_comms)
    setpoint = -1
    with pytest.raises(ValueError):
        program = SetpointActuatorEvent(actuator, 1, 1, setpoint, 0, 0, 0)
