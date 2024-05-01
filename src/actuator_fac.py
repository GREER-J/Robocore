from src.communication import CommsProtocol
from src.actuators import ActuatorProtocol

class ActuatorFactory:
    def __init__(self, connection: CommsProtocol, actuator_dict: dict[str:ActuatorProtocol]) -> ActuatorProtocol:
        self._connection = connection
        self._known_actuators = actuator_dict

    def create_actuator(self, actuator_config) -> ActuatorProtocol:
        actuator_type = actuator_config['type']

        actuator_constructor = self._known_actuators[actuator_type]
        sensor = actuator_constructor(actuator_config['limits'][0], actuator_config['limits'][1], actuator_config['command'], self._connection)
        
        return sensor