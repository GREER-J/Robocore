from src.communication import CommsFactory
from src.sim_connection import SimConnection
import pytest

@pytest.mark.skip(reason="Skipping until function is implemented to pass command to sim. Sim conn shouldn't rely on command dict.")
def test_comms_fac_create_sim_comms():
    # Sensor configuration for the test
    sim_config = {
    "name": "Sim Temperature Control Lab",
    "conn": "simulation",
    }

    comms_dict = {"simulation": SimConnection}
    fac = CommsFactory(comms_dict)

    sensor = fac.create_comms(sim_config["conn"])
    #assert isinstance(sensor, SimConnection)
