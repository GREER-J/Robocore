import pytest
from src.actuators import PwmOutput
from src.actuator_events import SetpointActuatorEvent

def test_setpoint_actuation_creation_no_error():
    actuator = PwmOutput(2,4)
    setpoint = 2
    program = SetpointActuatorEvent(actuator, 1, 1, setpoint, 0, 0, 0)
    program.process()
    assert actuator.current_val == setpoint

def test_setpoint_actuation_creation_with_error():
    actuator = PwmOutput(2,4)
    setpoint = 1
    with pytest.raises(ValueError):
        program = SetpointActuatorEvent(actuator, 1, 1, setpoint, 0, 0, 0)
