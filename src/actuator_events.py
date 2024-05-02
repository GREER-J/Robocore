from src.events import EventProtocol
from src.actuators import ActuatorProtocol


class SetpointActuatorEvent(EventProtocol):
    def __init__(self, actuator: ActuatorProtocol, trigger_time, priority, setpoint, duration=0, frequency=None, call_limit=None):
        """
        Initializes a setpoint actuator event.

        Args:
            actuator: The actuator object this event controls.
            trigger_time (float): The time at which this event should trigger.
            priority (int): The priority level of the event.
            setpoint (float): The target value to which the actuator should be set.
            duration (float, optional): The duration for which this action is considered to be active. Defaults to 0.
            frequency (float, optional): If specified, indicates how often (in seconds) to retrigger the event.
            call_limit (int, optional): The maximum number of times this event is allowed to trigger.
        """
        self._actuator = actuator
        self._time = trigger_time
        self._priority = priority
        self.setpoint = setpoint

        # Check setpoint
        if not self._actuator.is_legal_command(setpoint):
            # Illegal command so should fault!
            raise ValueError(
                f"{setpoint} is not a legal command for this actuator")

    def process(self):
        """
        Process the setpoint actuator event by setting the actuator to the specified setpoint.
        """
        self._actuator.set_actuator(self.setpoint)
