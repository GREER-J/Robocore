from src.communications_factory import CommsFactory
from src.sim_connection import SimConnection
from tests.mock_sim_stub import SimStub

def test_comms_fac_create_sim_comms():
    # Sensor configuration for the test
    sim_config = {
    "name": "Sim Temperature Control Lab",
    "conn": "simulation",
    }

    dummy_sim = SimStub("1")

    comms_dict = {"simulation": SimConnection}
    fac = CommsFactory(comms_dict)

    sensor = fac.create_comms(sim_config["conn"], command_fun=dummy_sim.pass_command_to_sim)
    assert isinstance(sensor, SimConnection)
