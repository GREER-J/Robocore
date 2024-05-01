from src.communication import CommsProtocol
from src.sensors import AnalogueSensor

class SensorFactory:
    def __init__(self, connection: CommsProtocol) -> None:
        self._connection = connection

    def create_sensor(self, sensor_config: dict):
        sensor_type = sensor_config['type']
        sensor = None  # Initialize sensor to None
        
        if sensor_type == 'pwm':
            sensor = AnalogueSensor(sensor_config['command'], self._connection)
        
        return sensor