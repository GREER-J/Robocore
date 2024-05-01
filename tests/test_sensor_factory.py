from tests.mock_comms_stub import CommsStub
from src.sensor_factory import SensorFactory
from src.sensors import AnalogueSensor
from tests.mock_sensor_stub import SensorStub

def test_sensor_fac_create_correct_sensor():
    # Sensor configuration for the test
    sensor_config = {
        "id": "Q1",
        "type": "pwm",
        "subtype": "heater",
        "command": "Q1",
        "limits": [0, 100],
        "units": "percent"
    }

    dummy_comms = CommsStub('a', 1,1)
    sensor_dict = {"pwm": SensorStub}
    fac = SensorFactory(dummy_comms, sensor_dict)

    sensor = fac.create_sensor(sensor_config)
    assert isinstance(sensor, SensorStub)

def test_sensor_fac_create_analog_sensor():
    # Sensor configuration for the test
    sensor_config = {
        "id": "Q1",
        "type": "pwm",
        "subtype": "heater",
        "command": "Q1",
        "limits": [0, 100],
        "units": "percent"
    }

    dummy_comms = CommsStub('a', 1,1)
    sensor_dict = {"pwm": AnalogueSensor}
    fac = SensorFactory(dummy_comms, sensor_dict)

    sensor = fac.create_sensor(sensor_config)
    assert isinstance(sensor, AnalogueSensor)