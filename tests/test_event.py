from src.events import Event, EventManager
from src.timekeeper import TimeKeeper
import time

class DummyFun:
    def __init__(self, time_keeper: TimeKeeper) -> None:
        self.called = False
        self.call_time = None
        self.time_keeper = time_keeper

    def process(self):
        self.called = True
        self.call_time = self.time_keeper.time

class DummyTimeKeeper:
    def __init__(self, initial_time: float = 0.0):
        self._current_time = initial_time

    @property
    def time(self) -> float:
        """ Returns the current simulated time. """
        return self._current_time

    def advance_time(self, seconds: float) -> None:
        """ Advances the current time by the specified number of seconds. """
        self._current_time += seconds

    
def test_when_processed_event_calls_func():
    tk =DummyTimeKeeper()
    dummy_fun = DummyFun(tk)
    event = Event(8, dummy_fun.process, 10, 1)
    event.process()
    assert dummy_fun.called

def test_add_event_to_event_manager_active_queue():
    tk =DummyTimeKeeper()
    event_manager = EventManager(4, tk)
    event_1 = DummyFun(tk)
    event_2 = DummyFun(tk)
    event_manager.add_event_to_active(Event(2, event_1.process, 1, 1))
    event_manager.add_event_to_active(Event(2, event_2.process, 1, 1))
    assert event_manager.n_events_in_active_queue == 2

def test_event_manager_max_queue():
    tk =DummyTimeKeeper()
    event_manager = EventManager(2, tk)
    event_1 = Event(1, lambda: None, 1, 1)
    event_2 = Event(2, lambda: None, 1, 1)
    event_3 = Event(3, lambda: None, 1, 1)
    event_manager.add_event_to_active(event_1)
    event_manager.add_event_to_active(event_2)
    event_manager.add_event_to_active(event_3)
    assert event_manager.n_events_in_active_queue == 2  # Ensure no more than max events are added

def test_event_processing_order():
    event_manager = EventManager(3, DummyTimeKeeper())
    results = []
    event_manager.add_event_to_active(Event(2, lambda: results.append('second'), 1, 1))
    event_manager.add_event_to_active(Event(1, lambda: results.append('first'), 1, 1))
    event_manager.process_events()
    assert results == ['first', 'second']

def test_scheduled_events_processed_at_time():
    tk = DummyTimeKeeper()
    event_manager = EventManager(2, tk)
    initial_time = tk.time
    dummy_fun1 = DummyFun(tk)
    dummy_fun2 = DummyFun(tk)
    event_manager.add_scheduled_event(Event(initial_time+5, dummy_fun1.process, 1, 2))
    event_manager.add_scheduled_event(Event(initial_time+10, dummy_fun2.process, 1, 2))

    assert event_manager.n_scheduled_events == 2
    assert event_manager.n_events_in_active_queue == 0
    
    tk.advance_time(5)
    event_manager.transfer_events()
    assert event_manager.n_scheduled_events == 1
    assert event_manager.n_events_in_active_queue == 1

    event_manager.update()
    assert event_manager.n_scheduled_events == 1
    assert event_manager.n_events_in_active_queue == 0

    tk.advance_time(5)
    event_manager.update()
    assert event_manager.n_scheduled_events == 0
    assert event_manager.n_events_in_active_queue == 0
