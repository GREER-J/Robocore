from src.state import StateProtocol
from typing import Protocol, NoReturn


class SimProtocol(Protocol):
    def __init__(self, state: StateProtocol, state_dynamics: callable, measurement_function: callable) -> None:
        pass

    def pass_command_to_sim(self, command:str) -> str:
        pass

    def get_time(self) -> float:
        """
        Get current simulation time.

        Returns:
            None
        """
        pass

    def update(self) -> NoReturn:
        """Updates the sim state so you can get a particular sensor type

        Returns:
            NoReturn: Doesn't return anything
        """
        pass

    def update_measurements(self) -> NoReturn:
        """Updates measurement values so we can request one

        Returns:
            NoReturn: No return...
        """
        pass