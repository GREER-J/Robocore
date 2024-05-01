from src.sim_connection import SimConnection

class SimStub:
    def __init__(self) -> None:
        self.sensor_fun_called = False

    def sensor_fun(self) -> str:
        self.sensor_fun_called = True
        return 0, 20.3

def test_sim_connection_calls_correct_sim_function():
    """Sim connection object should call the correct function in sim"""
    expected_command = 'A'
    dummy_sim = SimStub()
    commands = {expected_command: (1, dummy_sim.sensor_fun)}
    sim_connection = SimConnection(commands)
    sim_connection.send_command(expected_command)

    assert dummy_sim.sensor_fun_called == True, "The correct function wasn't called"
