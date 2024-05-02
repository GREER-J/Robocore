from tests.mock_comms_stub import CommsStub
from src.sensor_factory import SensorFactory
from src.sensors import AnalogueSensor
from tests.mock_sensor_stub import SensorStub


def test_sensor_fac_create_correct_sensor():
    # Sensor configuration for the test
    sensor_config = {
        "id": "T2",
        "type": "analog",
        "subtype": "temperature",
        "command": "T2",
        "resolution": 0.01,
        "limits": [0, 100],
        "units": "degrees Celsius"
    }

    dummy_comms = CommsStub('a', 1, 1)
    sensor_dict = {"analog": SensorStub}
    fac = SensorFactory(dummy_comms, sensor_dict)

    sensor = fac.create_sensor(sensor_config)
    assert isinstance(sensor, SensorStub)


def test_sensor_fac_create_analog_sensor():
    # Sensor configuration for the test
    sensor_config = {
        "id": "T2",
        "type": "analog",
        "subtype": "temperature",
        "command": "T2",
        "resolution": 0.01,
        "limits": [0, 100],
        "units": "degrees Celsius"
    }

    dummy_comms = CommsStub('a', 1, 1)
    sensor_dict = {"analog": AnalogueSensor}
    fac = SensorFactory(dummy_comms, sensor_dict)

    sensor = fac.create_sensor(sensor_config)
    assert isinstance(sensor, AnalogueSensor)
