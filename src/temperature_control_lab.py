from src.state import StateProtocol
from src.simulation import SimProtocol
from src.timekeeper import TimeKeeper

class TemperatureSimulation(SimProtocol):
    def __init__(self, state: StateProtocol, state_dynamics: callable, measurement_function: callable, time_keeper: TimeKeeper, x0 = None):
        self.state = state
        self.state.mu = x0
        self.state_dynamics = state_dynamics
        self.measurement_function = measurement_function
        self.time_keeper = time_keeper
        self._time = time_keeper.time
        self.y = None
        self._available_commands = {}

    def update_measurements(self) -> None:
        pass

    def pass_command_to_sim(self, command: str) -> str:
        # Receive command
        cmd = self._available_commands[command]
        # Call appropriate function
        rv = cmd()
        # Return result
        rv = ""
        return rv

    def set_Q1(self) -> None:
        self.state._u

    def update(self) -> None:
        """Implements a simple model that increases temperature over time."""
        t = self._time
        tkp1 = self.time_keeper.time
        self.state.predict((t, tkp1), self.state_dynamics)
        
        # Update measurements
        self.y = self.measurement_function(self.state.mu)
        
        # Update time
        self._time = tkp1

    def get_sensor_temperature(self) -> tuple[float, float]:
        """Specific method to expose temperature sensor data."""
        self.update()
        return self._time, self.y

def labsim(TC: float, t: float, Q1: float) -> float:
    U: float = 10.0
    A: float = 0.0012
    Cp: float = 500
    m: float = 0.004
    alpha: float = 0.01
    Ta: float = 25.0  # Assuming Ta is a constant temperature

    dTCdt: float = (U * A * (Ta - TC) + alpha * Q1) / (m * Cp)
    return dTCdt

def g(x):
    return x[0]