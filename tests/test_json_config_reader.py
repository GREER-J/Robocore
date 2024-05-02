from src.json_config_reader import JsonConfigReader


def test_json_config_reader_can_read_json():
    expected_config = {
        "name": "Sim Temperature Control Lab",
        "conn": "simulation",
        "plant_type": "Temperature Control Lab",
        "time_multiplier": 2,
        "sensors": [
            {"id": "T1", "type": "analog", "subtype": "temperature", "command": "T1",
                "resolution": 0.1, "limits": [0, 100], "units": "degrees Celsius"},
            {"id": "T2", "type": "analog", "subtype": "temperature", "command": "T2",
                "resolution": 0.01, "limits": [0, 100], "units": "degrees Celsius"}
        ],
        "actuators": [
            {"id": "Q1", "type": "pwm", "subtype": "heater",
                "command": "Q1", "limits": [0, 100], "units": "percent"},
            {"id": "Q2", "type": "pwm", "subtype": "heater",
                "command": "Q2", "limits": [0, 100], "units": "percent"}
        ]
    }
    config_path = 'tests/data/example_config.json'
    json_config_reader = JsonConfigReader()
    data = json_config_reader.read_config(config_path)
    assert data == expected_config
