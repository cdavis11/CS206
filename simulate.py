# Created by Claire Davis
# CS 206 Assingment 1

import pybullet as p
import time as t
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import os

# Display GUI
physicsClient = p.connect(p.GUI)

p.setAdditionalSearchPath(pybullet_data.getDataPath())

# Add gravitational force
p.setGravity(0,0,-9.8)

# Add floor
planeId = p.loadURDF("plane.urdf")

# Simulate robot
bodyId = p.loadURDF("body.urdf")

# Import box
p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate("body.urdf")

# Create vectors filled with 0s
backLegSensorValues = np.zeros(100)
frontLegSensorValues = np.zeros(100)

# Create loop to make GUI visibe for ~16 seconds
for i in range (0, 100):
    p.stepSimulation()
    # Add sensor to back and front leg
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    t.sleep(1/60)

# Save sensor values
np.save('data/backLegSensorValues.npy', backLegSensorValues)
np.save('data/frontLegSensorValues.npy', frontLegSensorValues)

# Close GUI
p.disconnect()

# Print values
print(backLegSensorValues)
print(frontLegSensorValues)
