# Robocore
A standard framework to make common robotics tasks easier.

## Use cases:
### Initial design with Robocore
Robocore should make the process from idea to first test day as seamless as possible.
The idea starts with pen and paper, Robocore should provide a basic simulation of the kinematics.

System is built with Teensy or Arduino. Hardware is assembled.

Robocore should provide blocks to make coding easier.

Robocore should be able to run generic tests to quickly ensure modules are working:
- For sensors Robocore should display values to visually see if they're reasonable
- For actuators Robocore should provide *programs* to run on them (sweep, setpoint, ramp ect)
- Robocore should provide basic simulation environment

### Test day
Test days consist of taking vehicle or system to it's operating environment and letting it loose. It's about collecting data to see how closely the actual thing matches your expectations.

Robocore should make it easy to set programs in the controller for specific types of test.
- Eg *forward* for 30 seconds at 50% thrust, right right, ect

While this is happening Robocore should make it easy to log data for later analysis.

Robocore should have easy integration with manual control and estops.

### Post test day analysis
Robocore should help with the process of getting better models of the plant.
It should be able to run KF and KS to get better data.
It should be able to do system identification.
- First Order Dead Time model
- Second order transfer functions

Models of actuators should be able to be separate from the main body.

Robocore should provide a simulation environment and tools to create basic control

### Later iterations
Robocore should provide frameworks for standard modules such as;
- Mission planning
- Guidance
- Advanced control
- User input
- Hardware in the loop testing


## Design
Robocore will be an event based system where events (eg, sensor updates, logging, calculating control values) are all event driven.

Robocore has maintains two different lists of events that it tracks.
- The active event queue: These are events that are ready for execution.
- The scheduled event queue: These are events that are scheduled in the future.

Periodically events are moved from the scheduled events to the active list.

Events from the active list are queued for execution and are sorted based on priority and time. This list should be quite small at all times.

### Simple Mission Design 
This allows for simple mission design such as drawing a [Victor Sierra](https://www.bing.com/search?pglt=169&q=victor+sierra+search+pattern&cvid=da5eb72dabfb4fda9da07d170236aac0&gs_lcrp=EgZjaHJvbWUqBggCEAAYQDIGCAAQRRg5MgYIARAAGEAyBggCEAAYQDIGCAMQABhAMgYIBBAAGEAyBggFEAAYQDIGCAYQABhAMgYIBxAAGEAyBggIEAAYQNIBCDUwNTlqMGoxqAIAsAIA&FORM=ANNTA1&PC=LCTS) by scheduling update setpoint events for specific times.

This will not interfere with regular events such as control updates or sensor polling.

## Types of events
### Sensor update
Polls a specific sensor and performs a state update with the specific information.

### Control update
Update either PID controllers for specific actuators or higher level MPC controllers.

### Guidance update
Updates guidance trajectory to deliver setpoints for controller.

### Mission planning update

### Supervisory update

### State logging update
Logs current state at known frequency

## Config files
The micro controller and python program talk to each other with commands. If we specify available commands or sensors that can be standardised.

