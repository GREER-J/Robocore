from src.sim_connection import SimConnection
from tests.mock_sim_stub import SimStub


def test_sim_connection_calls_correct_sim_function():
    """Sim connection object should call the correct function in sim"""
    expected_command = 'A'
    dummy_sim = SimStub("1")
    sim_connection = SimConnection(dummy_sim.pass_command_to_sim)
    sim_connection.send_command(expected_command)

    assert dummy_sim.command_sent == expected_command, "The correct command wasn't sent"
