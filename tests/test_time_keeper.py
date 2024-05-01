from src.timekeeper import TimeKeeper
import time

def test_time_keeper_faster_time():
    exp_time = 1 #[s]
    delay_time = 1
    time_scalar = exp_time/delay_time
    tk = TimeKeeper(time_scalar)
    time.sleep(delay_time)
    tolerance = 10/1000 # [s]
    assert tk.time - exp_time <= tolerance 






