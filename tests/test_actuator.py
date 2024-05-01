from src.actuators import PwmOutput
import pytest

def test_can_set_current_val():
    actuator = PwmOutput(0, 6)  # Assuming 0 is the channel and 6 is the maximum voltage
    volts = 2
    actuator.set_actuator_command(volts)
    assert actuator.current_val == volts, "Actuator should store the command voltage accurately"

def test_when_voltage_over_max_raises_error():
    actuator = PwmOutput(0, 6)
    with pytest.raises(ValueError):
        actuator.set_actuator_command(7)

def test_when_voltage_over_min_raises_error():
    actuator = PwmOutput(2, 6)
    with pytest.raises(ValueError):
        actuator.set_actuator_command(1)

def test_voltage_type():
    actuator = PwmOutput(0, 6)
    with pytest.raises(TypeError):
        actuator.set_actuator_command("High")  # Non-numeric input should raise an error

def test_schedule_setpoint():
    pass