from src.actuators import ActuatorProtocol
from src.communication import CommsProtocol


class ActuatorStub(ActuatorProtocol):
    def __init__(self, min: float, max: float, command: str, connection: CommsProtocol) -> None:
        self._min_setpoint = min
        self._max_setpoint = max
        self._command_val = command
        self._connection = connection

    def set_actuator(self, setpoint: float) -> None:
        pass

    def is_legal_command(self, setpoint: float) -> bool:
        return True
