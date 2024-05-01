from src.timekeeper import TimeKeeper
from typing import Protocol, runtime_checkable

@runtime_checkable
class EventProtocol(Protocol):
    """
    Protocol for event objects, requiring implementations to provide
    properties for trigger time, duration, priority, and a method to check if the event is recurring.
    """
    
    @property
    def trigger_time(self) -> float:
        """Get the time at which the event is supposed to trigger."""
        ...

    @property
    def duration(self) -> float:
        """Get the expected duration of the event."""
        ...

    @property
    def priority(self) -> int:
        """Get the priority level of the event."""
        ...

    @property
    def is_recurring(self) -> bool:
        """Determine if the event is recurring."""
        ...

    def process(self) -> None:
        """Process the event according to its defined behavior."""
        ...

    def increment_trigger_time(self) -> None:
        ...


class Event(EventProtocol):
    def __init__(self, time: float, process_fun: callable, expected_duration: float, priority: int, frequency:float=None, call_limit:int =None ) -> None:
        self._time = time
        self._process_fun = process_fun
        self._duration = expected_duration
        self._priority = priority
            # Recurring specific
        self._frequency = frequency
        self._n_called = 0
        self._call_limit = call_limit

    @property
    def is_recurring(self) -> bool:
        """
        Determine if the event is recurring based on its frequency and call limit.
        An event is considered recurring if:
        - It has a frequency set (not None).
        - It either has no call limit (None) or has not reached its call limit yet.

        Returns:
            bool: True if the event is recurring, False otherwise.
        """
        # Check if the event has a frequency set, indicating it is intended to be recurring.
        if self._frequency is None:
            return False
        # If no call limit is set, the event can recur indefinitely.
        elif self._call_limit is None:
            return True
        # If a call limit is set, check if the event has not yet reached this limit.
        else:
            return self._n_called < self._call_limit - 1

    @property
    def trigger_time(self) -> float:
        return self._time
    
    @property
    def duration(self) -> float:
        """Get the expected duration of the event."""
        return self._duration

    @property
    def priority(self) -> int:
        """Get the priority level of the event."""
        return self._priority
    
    def increment_trigger_time(self) -> None:
        self._time += 1/self._frequency

    def process(self) -> None:
        self._n_called += 1
        self._process_fun()
  

class EventManager():
    def __init__(self, queue_max: int, time_keeper: TimeKeeper) -> None:
        self._queue_max = queue_max
        self._time_keeper = time_keeper
        self._active_queue: list[EventProtocol] = list()
        self._scheduled_events: list[EventProtocol] = list()

    def add_event_to_active(self, event: EventProtocol) -> None:
        if len(self._active_queue) < self._queue_max:
            self._active_queue.append(event)

    def process_events(self):
        self._active_queue.sort(key=lambda event: (event.priority, event.trigger_time))
        remaining_events = []

        for event in self._active_queue:
            try:
                event.process()
            except Exception as e:
                print(f"Error processing event: {e}")
                remaining_events.append(event)

        self._active_queue = remaining_events

    def add_scheduled_event(self, event: EventProtocol) -> None:
        self._scheduled_events.append(event)
    
    @property
    def n_events_in_active_queue(self):
        return len(self._active_queue)
    
    @property
    def n_scheduled_events(self):
        return len(self._scheduled_events)
    
    def transfer_events(self) -> None:
        """ Transfer events from scheduled to active based on the current time. """
        current_time = self._time_keeper.time
        new_scheduled_events = []
        for event in self._scheduled_events:
            if event.trigger_time <= current_time:
                self._active_queue.append(event)
                if event.is_recurring:
                    event.increment_trigger_time()
                    new_scheduled_events.append(event)
            else:
                new_scheduled_events.append(event)
    
        # Remove transferred events from the scheduled queue
        self._scheduled_events = [
            event for event in self._scheduled_events if event.trigger_time > current_time
        ]

    def update(self):
        self.transfer_events()
        self.process_events()