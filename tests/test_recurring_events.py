from src.events import EventManager, Event
from src.timekeeper import TimeKeeper


def test_call_limit_on_recurring_event():
    call_limit = 3
    event = Event(4, lambda: print('Event triggered'), 1, 1, 2, call_limit)

    # Process the event (call_limit - 1) times
    for _ in range(call_limit - 1):
        assert event.is_recurring, f"Event should still be recurring after {_} calls."
        event.process()

    # Check calls before the final process
    assert event._n_called == call_limit - \
        1, f"Expected n_called to be {call_limit - 1}, got {event._n_called}"

    # Process the last call
    event.process()
    assert not event.is_recurring, f"Event should not be recurring after the limit reached. n_called: {event._n_called}"


def test_schedules_next_event_on_call():
    tk = TimeKeeper(3)
    event_manager = EventManager(4, tk)
    frequency = 2
    start_time = tk.time
    event = Event(start_time, lambda: print('1'), 1, 1, frequency, 2)
    event_manager.add_scheduled_event(event)
    assert len(event_manager._scheduled_events) == 1
    event_manager.update()

    assert len(event_manager._scheduled_events) == 1
    assert event_manager._scheduled_events[0].trigger_time == start_time + 1/frequency
