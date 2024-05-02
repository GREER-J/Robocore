import numpy as np
from scipy.integrate import odeint
from typing import Protocol, NoReturn, Tuple


class StateProtocol(Protocol):
    def __init__(self, nx: int, nu: int) -> None:
        pass

    @property
    def mu(self) -> None:
        pass

    @property
    def u(self) -> None:
        pass

    def predict(self, time_span: Tuple[float, float], state_dynamics: callable) -> NoReturn:
        """
        Get current simulation time.

        Returns:
            None
        """
        pass


class State(StateProtocol):
    def __init__(self, nx: int, nu: int) -> None:
        self._time = 0
        self.nx = nx
        self._mu = np.zeros((nx))
        self._u = np.zeros((nu))

    @property
    def mu(self) -> None:
        return self._mu

    @mu.setter
    def mu(self, value: np.ndarray) -> None:
        if len(value) != self.nx:
            raise ValueError("Length of mu must match nx")
        self._mu = value

    def predict(self, time_span: list[float, float], state_dynamics):

        # x = f(x)*dt
        y = odeint(state_dynamics, self.mu, time_span, args=(self._u,))

        self._mu = y[-1]
