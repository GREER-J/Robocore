from tests.mock_comms_stub import CommsStub
from src.sensors import AnalogueSensor


def test_get_sensor_value_sends_correct_command():
    expected_command = 'A'
    dummy_connection = CommsStub(1, 2, 3)
    sensor = AnalogueSensor(expected_command, dummy_connection)
    sensor.get_sensor_command()
    assert dummy_connection.command_sent == expected_command


def test_get_sensor_value_decodes_connection_response():
    expected_time = 23
    expected_value = 20.4
    expected_code = 1
    expected_command = 'A'
    dummy_connection = CommsStub(expected_code, expected_time, expected_value)
    sensor = AnalogueSensor(expected_command, dummy_connection)
    time, value = sensor.get_sensor_command()

    assert time == expected_time, "Incorrect value for time."
    assert value == expected_value, "Incorrect sensor value."
