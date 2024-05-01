from src.sensors import SensorProtocol
from src.communication import CommsProtocol

class SensorStub(SensorProtocol):
    def __init__(self, command: str, connection: CommsProtocol, interval=None) -> None:
        self.n_called = 0
        self.time = 0
        self._command = command
        self._connection = connection
        
        if(interval):
            self.interval = interval
        else:
            self.interval = 0      

    def get_sensor_command(self):
        self.n_called += 1
        self.time += self.interval
        return self.time, 20.0