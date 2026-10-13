"""Assignment 4: convert the sensor 1 example file to the sensor 2 format.

Orchestration only, no loops. Three lines are enough:
  1. load  data/sensor1_example.csv  with sensors.load_sensor1
  2. save the readings to  data/sensor2_converted.csv  with sensors.save_sensor2
     (one reading every 15 s)
  3. print a short message saying what was written, and how many readings
"""
import sensors

# Written by me
data = sensors.load_sensor1(r"data\sensor1_example.csv")
sensors.save_sensor2(r"data\sensor2_converted.csv", data, 15)
