from src.sim_connection import SimConnection

class SimStub:
    def __init__(self) -> None:
        self.sensor_fun_called = False

    def send_command(self, command:str) -> str:
        self.command_sent = command
        return ""

def test_sim_connection_calls_correct_sim_function():
    """Sim connection object should call the correct function in sim"""
    expected_command = 'A'
    dummy_sim = SimStub()
    sim_connection = SimConnection(dummy_sim.send_command)
    sim_connection.send_command(expected_command)

    assert dummy_sim.command_sent == expected_command, "The correct command wasn't sent"
