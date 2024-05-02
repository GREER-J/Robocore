from src.sensors import SensorProtocol
from src.timekeeper import TimeKeeper
from src.events import EventManager, Event

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
        
        self._event_manager.add_scheduled_event(Event(self._time_keeper.time, update_readings, duration, 1, frequency, n_samples))

        while len(times) < n_samples:
            self._event_manager.update()
        
        print("Rounds complete")
        return times, values

    
def build_plant(sim_config: dict, sim_reference =None) -> Plant:
    """
    Get's passed a config and optionally a sim object to create a plant with
    """    

    # Create connection
    

    # Create sensors
    sensors = {}
    

    # Create actuators
    actuators = {}
    

    event_manager = EventManager(2, time_keeper)
    
    # Create plant
    plant = Plant(time_keeper, event_manager, sensors, None)
    return plant