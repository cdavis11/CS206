# Created by Claire Davis
# CS 206 Assingment 1

import pybullet as p
import time as t
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import math

# Display GUI
physicsClient = p.connect(p.GUI)

p.setAdditionalSearchPath(pybullet_data.getDataPath())

# Add gravitational force
p.setGravity(0,0,-9.8)

# Add floor
planeId = p.loadURDF("plane.urdf")

# Simulate robot
robot = p.loadURDF("body.urdf")

# Import box
p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate("body.urdf")

# Create vectors filled with 0s
backLegSensorValues = np.zeros(1000)
frontLegSensorValues = np.zeros(1000)

# Create loop to make GUI visibe for ~16 seconds
for i in range (0, 1000):
    p.stepSimulation()
    # Add sensor to back and front leg
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    # Simulate motor
    pyrosim.Set_Motor_For_Joint(bodyIndex = robot, jointName = "Torso_BackLeg", controlMode = p.POSITION_CONTROL,
                                targetPosition = -math.pi/6.0, maxForce = 500)
    pyrosim.Set_Motor_For_Joint(bodyIndex = robot, jointName = "Torso_FrontLeg", controlMode = p.POSITION_CONTROL,
                                targetPosition = math.pi/6.0, maxForce = 500)
    t.sleep(1/100)

# Save sensor values
np.save('data/backLegSensorValues.npy', backLegSensorValues)
np.save('data/frontLegSensorValues.npy', frontLegSensorValues)

# Close GUI
p.disconnect()

# Print values
print(backLegSensorValues)
print(frontLegSensorValues)
