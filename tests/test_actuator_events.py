import pytest
from src.actuators import PwmOutput
from src.actuator_events import SetpointActuatorEvent
from tests.mock_comms_stub import CommsStub


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
