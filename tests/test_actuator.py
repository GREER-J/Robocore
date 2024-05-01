from src.actuators import PwmOutput
import pytest

from tests.mock_comms_stub import CommsStub

def test_can_set_current_val():
    dummy_comms = CommsStub('a', 2, 4)
    actuator = PwmOutput(0, 6, 'a', dummy_comms)
    volts = 2
    actuator.set_actuator(volts)
    assert actuator.current_val == volts, "Actuator should store the command voltage accurately"

def test_when_voltage_over_max_raises_error():
    dummy_comms = CommsStub('a', 2, 4)
    actuator = PwmOutput(0, 6, 'a', dummy_comms)
    with pytest.raises(ValueError):
        actuator.set_actuator(7)

def test_when_voltage_over_min_raises_error():
    dummy_comms = CommsStub('a', 2, 4)
    actuator = PwmOutput(0, 6, 'a', dummy_comms)
    with pytest.raises(ValueError):
        actuator.set_actuator(-1)

def test_voltage_type():
    dummy_comms = CommsStub('a', 2, 4)
    actuator = PwmOutput(0, 6, 'a', dummy_comms)
    with pytest.raises(TypeError):
        actuator.set_actuator("High")  # Non-numeric input should raise an error

def test_pwm_output_sends_correct_command():
    expected_command = 'A'
    setpoint = 5.2
    dummy_connection = CommsStub(1, 2, 3)
    actuator = PwmOutput(0, 6, expected_command, dummy_connection)
    actuator.set_actuator(setpoint)
    assert dummy_connection.command_sent == f"{expected_command}, {setpoint}"