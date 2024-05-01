from src.plant import Plant
from src.sensors import SensorProtocol
from src.timekeeper import TimeKeeper
from src.events import EventManager

class SensorStub(SensorProtocol):
    def __init__(self, interval) -> None:
        self.n_called = 0
        self.interval = interval
        self.time = 0

    def get_sensor_command(self):
        self.n_called += 1
        self.time += self.interval
        return self.time, 20.0

def test_vehicle_calls_sensor_n_number_times():
    n_samples = 10
    frequency = 2

    temp_sensor = SensorStub(frequency)
    sensors = {'temperature': temp_sensor}
    tk = TimeKeeper(300)
    vehicle = Plant(tk, EventManager(3, tk), sensors, actuators=None)
    vehicle.poll_sensors('temperature', n_samples, frequency)

    expected_calls = n_samples
    assert temp_sensor.n_called == expected_calls, f"The sensor function was called {temp_sensor.n_called} times instead of the expected {expected_calls}"

def test_vehicle_times_values_correct_length():
    n_measurements = 10
    frequency = 2

    temp_sensor = SensorStub(frequency)
    sensors = {'temperature': temp_sensor}

    tk = TimeKeeper(250)
    vehicle = vehicle = Plant(tk, EventManager(2, tk), sensors, actuators=None)
    times, values = vehicle.poll_sensors('temperature', n_measurements, frequency)

    expected_calls = n_measurements
    assert len(times) == expected_calls, f"The length of the time vector is{len(times)} instead of {expected_calls}"
    assert len(values) == expected_calls, f"The length of the values vector is{len(values)} instead of {expected_calls}"
