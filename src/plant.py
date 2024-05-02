from src.sensors import SensorProtocol
from src.timekeeper import TimeKeeper
from src.events import EventManager, Event
from src.config_reader import ConfigReaderProtocol
from src.communications_factory import CommsFactory
from src.sensor_factory import SensorFactory
from src.actuator_fac import ActuatorFactory
from src.simulation import SimProtocol


class Plant():
    def __init__(self, time_keeper: TimeKeeper, event_manager: EventManager, sensors: dict[str, SensorProtocol], actuators) -> None:
        self._time_keeper = time_keeper
        self._event_manager = event_manager
        self._sensors = sensors
        self._actuators = actuators

    def poll_sensors(self, sensor: str, n_samples: int, frequency: float) -> tuple[list[float], list[float]]:
        selected_sensor = self._sensors[sensor]
        times = []
        values = []
        current_time = self._time_keeper.time  # Ensure this is callable

        duration = 1

        # Combined function to update times and values
        def update_readings():
            time, val = selected_sensor.get_sensor_command()
            print(f"Getting sensor at {time:.2f}")

            times.append(time)
            values.append(val)

        # Schedule events for periodic sensor readings

        self._event_manager.add_scheduled_event(Event(
            self._time_keeper.time, update_readings, duration, 1, frequency, n_samples))

        while len(times) < n_samples:
            self._event_manager.update()

        print("Rounds complete")
        return times, values


def build_plant(config_file_path: str, config_reader: ConfigReaderProtocol, comms_fac: CommsFactory, sensor_fac: SensorFactory, actuator_fac: ActuatorFactory, sim_reference: SimProtocol = None) -> Plant:
    """
    Get's passed a config and optionally a sim object to create a plant with
    """
    # Read config
    config = config_reader.read_config(config_file_path)

    if config['conn'] == 'simulation':
        tk = sim_reference.time_keeper
    else:
        tk = TimeKeeper(int(config['time_multiplier']))

    # Create connection
    comms_fac.create_comms(config['conn'], command_fun=sim_reference)

    # Create sensors
    sensors = {}
    for sensor_config in config['sensors']:
        sensors[sensor_config['id']] = sensor_fac.create_sensor(sensor_config)

    # Create actuators
    actuators = {}
    for actuator_config in config['actuators']:
        actuators[actuator_config['id']
                  ] = actuator_fac.create_actuator(actuator_config)

    event_manager = EventManager(2, tk)

    # Create plant
    plant = Plant(tk, event_manager, sensors, None)
    return plant
