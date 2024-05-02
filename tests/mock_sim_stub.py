from src.simulation import SimProtocol


class SimStub(SimProtocol):
    def __init__(self, return_value: str) -> None:
        self.sensor_fun_called = False
        self._return_val = return_value

    def pass_command_to_sim(self, command: str) -> str:
        self.command_sent = command
        return self._return_val

    def get_time(self) -> float:
        return 0.0

    def update(self) -> None:
        pass

    def update_measurements(self) -> None:
        pass
