import json

# Load the JSON data from a file
with open('data/sim_tclab_config.json', 'r') as file:
    vehicle_config = json.load(file)

print(f"Conn type: {vehicle_config['name']}:")
print(f"- Conn type: {vehicle_config['conn']}")

# Accessing sensor data
print(f"- Sensors:")
for sensor in vehicle_config['sensors']:
    print(f"\t-{sensor['id']}: ({sensor['type']}) {sensor['subtype']}")

# Accessing actuator data
print(f"- Actuators:")
for actuator in vehicle_config['actuators']:
    print(f"\t-{actuator['id']} ({actuator['type']}) {actuator['subtype']}, range: {actuator['limits'][0]} <= setpoint <= {actuator['limits'][1]}")
