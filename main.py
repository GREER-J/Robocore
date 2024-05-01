from src.temperature_control_lab import TemperatureSimulation, labsim, g
from src.sim_connection import SimConnection
from src.timekeeper import TimeKeeper
from src.sensors import AnalogueSensor
from src.plant import build_plant
from src.state import State
import numpy as np

from matplotlib import pyplot as plt

dt = 0.2 # [s]
T0 = 18 # [deg c]
x0 = np.ones(1)*T0

tclab_sim = TemperatureSimulation(State(1, 1), labsim, g, TimeKeeper(10), x0)

# Sim data
# ('Sensor command', response code, sensor function)
conn_type = SimConnection
time_keeper = tclab_sim.time_keeper
sim_interactions = [
    ('A', 1, 'T1', AnalogueSensor, tclab_sim.get_sensor_temperature),
    ('B', 2, 'T2', AnalogueSensor, tclab_sim.get_sensor_temperature)
            ]

sim_data = [time_keeper, conn_type, sim_interactions]

tclab = build_plant(sim_data)

time, data = tclab.poll_sensors("T1", 100, 0.1)

plt.plot(time, data)
plt.title("Sensor Data Over Time")
plt.xlabel("Time (s)")
plt.ylabel("Sensor Value")
plt.grid(True)
plt.show()
