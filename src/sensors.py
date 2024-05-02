from typing import Protocol, Tuple
from src.communication import CommsProtocol


class SensorProtocol(Protocol):
    def get_sensor_command(self) -> Tuple[float, float]:
        """
        Retrieve the current value from the sensor.

        Returns:
            Tuple[float, float]: A tuple containing the sensor reading time and value.
        """
        pass


class AnalogueSensor(SensorProtocol):
    def __init__(self, command: str, connection: CommsProtocol) -> None:
        self._connection = connection
        self._get_sensor_command = command

    def process_analogue_sensor_response(self, response: str) -> Tuple[float, float]:
        response_code, data = response.split(':')

        time, value = data.split(',')
        return float(time.strip()), float(value.strip())

    def get_sensor_command(self) -> Tuple[float, float]:
        self._connection.send_command(self._get_sensor_command)
        response = self._connection.read_connection()
        time, value = self.process_analogue_sensor_response(response)
        return time, value
