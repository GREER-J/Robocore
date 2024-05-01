from tests.mock_comms_stub import CommsStub
from tests.mock_actuator_stub import ActuatorStub
from src.actuator_fac import ActuatorFactory
from src.actuators import PwmOutput

def test_actuator_fac_create_correct_actuator():
    # Sensor configuration for the test
    actuator_config = {
        "id": "Q1",
        "type": "pwm",
        "subtype": "heater",
        "command": "Q1",
        "limits": [0, 100],
        "units": "percent"
    }

    dummy_comms = CommsStub('a', 1,1)
    actuator_dict = {"pwm": ActuatorStub}
    fac = ActuatorFactory(dummy_comms, actuator_dict)

    sensor = fac.create_actuator(actuator_config)
    assert isinstance(sensor, ActuatorStub)

def test_actuator_fac_create_pwm_actuator():
    # Sensor configuration for the test
    actuator_config = {
        "id": "Q1",
        "type": "pwm",
        "subtype": "heater",
        "command": "Q1",
        "limits": [0, 100],
        "units": "percent"
    }

    dummy_comms = CommsStub('a', 1,1)
    actuator_dict = {"pwm": PwmOutput}
    fac = ActuatorFactory(dummy_comms, actuator_dict)

    sensor = fac.create_actuator(actuator_config)
    assert isinstance(sensor, PwmOutput)