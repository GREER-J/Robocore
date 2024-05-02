from src.plant import Plant
from src.timekeeper import TimeKeeper
from src.events import EventManager

from tests.mock_sensor_stub import SensorStub
from tests.mock_comms_stub import CommsStub

import pytest


@pytest.mark.skip(reason="Skipping test until issue is resolved")
def test_vehicle_calls_sensor_n_number_times():
    n_samples = 10
    frequency = 2

    temp_sensor = SensorStub('a', CommsStub('a', 1, 1))
    sensors = {'temperature': temp_sensor}
    tk = TimeKeeper(300)
    vehicle = Plant(tk, EventManager(3, tk), sensors, actuators=None)
    vehicle.poll_sensors('temperature', n_samples, frequency)

    expected_calls = n_samples
    assert temp_sensor.n_called == expected_calls, f"The sensor function was called {temp_sensor.n_called} times instead of the expected {expected_calls}"


@pytest.mark.skip(reason="Skipping test until issue is resolved")
def test_vehicle_times_values_correct_length():
    n_measurements = 10
    frequency = 2

    temp_sensor = SensorStub('a', CommsStub('a', 1, 1), frequency)
    sensors = {'temperature': temp_sensor}

    tk = TimeKeeper(250)
    vehicle = vehicle = Plant(tk, EventManager(2, tk), sensors, actuators=None)
    times, values = vehicle.poll_sensors(
        'temperature', n_measurements, frequency)

    expected_calls = n_measurements
    assert len(
        times) == expected_calls, f"The length of the time vector is{len(times)} instead of {expected_calls}"
    assert len(
        values) == expected_calls, f"The length of the values vector is{len(values)} instead of {expected_calls}"
