from src.temperature_control_lab import TemperatureSimulation, labsim, g
from src.plant import build_plant
from src.state import State
from src.timekeeper import TimeKeeper
from config import known_comms_dict, known_sensor_dict ,known_actuator_dict
from src.json_config_reader import JsonConfigReader
from src.plant import Plant
from src.events import EventManager
from src.communications_factory import CommsFactory
from src.json_config_reader import JsonConfigReader
from src.sensor_factory import SensorFactory
from src.actuator_fac import ActuatorFactory

import numpy as np
import os

config_file_path = 'data/sim_tclab_config.json'

dt = 0.2 # [s]
T0 = 18 # [deg c]
x0 = np.ones(1)*T0

tclab_sim = TemperatureSimulation(State(1, 1), labsim, g, TimeKeeper(10), x0)

# Read config
config_reader = JsonConfigReader()
config = config_reader.read_config(config_file_path)

# Create connection
comms_fac = CommsFactory(known_comms_dict)
conn = comms_fac.create_comms(config['conn'], command_fun=tclab_sim.pass_command_to_sim)


# Create sensors
sensors = {}
sensor_fac = SensorFactory(conn, known_sensor_dict)
for sensor_config in config['sensors']:
    sensors[sensor_config['id']] = sensor_fac.create_sensor(sensor_config)

# Create actuators
actuators = {}
actuator_fac = ActuatorFactory(conn, known_actuator_dict)
for actuator_config in config['actuators']:
    actuators[actuator_config['id']] = actuator_fac.create_actuator(actuator_config)

tclab = Plant(tclab_sim.time_keeper, EventManager(5, tclab_sim.time_keeper), sensors, actuators)

time, data = tclab.poll_sensors('T1', 3, 1)

# Create the 'out' directory if it doesn't exist
output_directory = "out"
os.makedirs(output_directory, exist_ok=True)

# Save sensor data to a text file in the 'out' directory
output_file = os.path.join(output_directory, "sensor_data.txt")
with open(output_file, "w") as file:
    file.write("Time (s)\tSensor Value\n")
    for t, d in zip(time, data):
        file.write(f"{t:.2f}\t{d:.2f}\n")

print(f"Sensor data saved to {output_file}")