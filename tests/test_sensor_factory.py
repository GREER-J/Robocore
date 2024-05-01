from tests.mock_comms_stub import CommsStub
from src.sensor_factory import SensorFactory
from src.sensors import AnalogueSensor

def test_sensor_create_analog():
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
    fac = SensorFactory(dummy_comms)

    sensor = fac.create_sensor(sensor_config)
    assert isinstance(sensor, AnalogueSensor)