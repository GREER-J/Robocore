# Requirements
## Initial construction
### For sensors Robocore should display values to visually see if they're reasonable
As a robotics developer, I want Robocore to display sensor values visually so that I can quickly assess if they are within reasonable ranges.

```python
tclab = vehicle(*setup*)
data = tclab.poll_sensor("temperature sensor", duration=10, interval=1)

plt.figure(figsize=(10, 5))
plt.plot(data)
plt.title("Sensor Data Over Time")
plt.xlabel("Time (s)")
plt.ylabel("Sensor Value")
plt.grid(True)
plt.show()
```
