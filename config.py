from src.sensors import AnalogueSensor
from src.actuators import PwmOutput
from src.sim_connection import SimConnection


known_sensor_dict = {"analog": AnalogueSensor}

known_actuator_dict = {"pwm": PwmOutput}

known_comms_dict = {"simulation": SimConnection}
