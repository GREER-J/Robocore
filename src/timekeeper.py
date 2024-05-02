import time


class TimeKeeper:
    def __init__(self, scalar=1):
        self.start_time = time.time()
        self.scalar = scalar

    def set_scalar(self, scalar):
        self.scalar = scalar

    @property
    def time(self) -> float:
        """Returns the time since initialisation in seconds [s]

        Returns:
            _type_: _description_
        """
        elapsed = time.time() - self.start_time
        return elapsed * self.scalar

    def convert_time(self, sim_time: float) -> float:
        """Converts time from sim time to real time

        Args:
            sim_time (float): Time in sim time in seconds [s]

        Returns:
            float: realtime duration in seconds [s]
        """
        return sim_time / self.scalar

    def sleep(self, sim_time_duration: float) -> None:
        time.sleep(self.convert_time(sim_time_duration))
