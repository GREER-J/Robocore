from typing import Protocol
from src.communication import CommsProtocol


class ActuatorProtocol(Protocol):
    def set_actuator(self, command: float) -> None:
        """
        Set the current level for an actuator.

        Returns:
            None:
        """
        pass

    def is_legal_command(self, command: float) -> bool:
        ...


class PwmOutput(ActuatorProtocol):
    def __init__(self, min: float, max: float, command: str, connection: CommsProtocol) -> None:
        self._min = min
        self._max = max
        self._current_val = 0  # [V]
        self._connection = connection
        self._set_actuator_command = command

    def is_legal_command(self, command: float) -> bool:
        return self._min <= command <= self._max

    @property
    def actuator_command(self) -> str:
        return f"{self._set_actuator_command}, {self._current_val}"

    def set_actuator(self, setpoint_val: float) -> None:
        if self.is_legal_command(setpoint_val):
            self._current_val = setpoint_val
            self._connection.send_command(self.actuator_command)
        else:
            if setpoint_val < self._min:
                raise ValueError(
                    f"Command value {setpoint_val} is below the minimum limit of {self._min}.")
            else:
                raise ValueError(
                    f"Command value {setpoint_val} is below the maximum limit of {self._max}.")

    @property
    def current_val(self) -> float:
        return self._current_val
