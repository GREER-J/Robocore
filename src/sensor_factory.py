from src.communication import CommsProtocol
from src.sensors import AnalogueSensor, SensorProtocol

class SensorFactory:
    def __init__(self, connection: CommsProtocol, sensor_dict: dict[str:SensorProtocol]) -> SensorProtocol:
        self._connection = connection
        self._known_sensors = sensor_dict

    def create_sensor(self, sensor_config: dict):
        sensor_type = sensor_config['type']

        sensor_constructor = self._known_sensors[sensor_type]
        sensor = sensor_constructor(sensor_config['command'], self._connection)
        
        return sensor