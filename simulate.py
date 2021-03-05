# Created by Claire Davis
# CS 206 Assingment 1

from simulation import SIMULATION
simulation = SIMULATION()

##import pybullet as p
##import time as t
##import pybullet_data
##import pyrosim.pyrosim as pyrosim
##import numpy as np
##import math
##import random
##import constants as c

### Initialize variables
##amplitude1 = c.amp1
##frequency1 = c.freq1
##phaseOffset1 = c.phase1
##amplitude2 = c.amp2
##frequency2 = c.freq2
##phaseOffset2 = c.phase2
##
### Display GUI
##physicsClient = p.connect(p.GUI)
##
##p.setAdditionalSearchPath(pybullet_data.getDataPath())
##
### Add gravitational force
##p.setGravity(0,0,-9.8)
##
### Add floor
##planeId = p.loadURDF("plane.urdf")
##
### Simulate robot
##robot = p.loadURDF("body.urdf")
##
### Import box
##p.loadSDF("world.sdf")
##
##pyrosim.Prepare_To_Simulate("body.urdf")
##
### Create vectors filled with 0s
##backLegSensorValues = np.zeros(1000)
##frontLegSensorValues = np.zeros(1000)
##
### Create sinusoidal vector
##targetAngles1 = amplitude1*np.sin(frequency1*(np.linspace(-math.pi, math.pi, 1000)) + phaseOffset1)
##targetAngles2 = amplitude2*np.sin(frequency2*(np.linspace(-math.pi, math.pi, 1000)) + phaseOffset2)
##np.save('data/targetAngleValuesBackLeg.npy', targetAngles1)
##np.save('data/targetAngleValuesFrontLeg.npy', targetAngles2)
##
### Create loop to make GUI visibe for ~16 seconds
##for i in range (0, 1000):
##    p.stepSimulation()
##    # Add sensor to back and front leg
##    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
##    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
##    # Simulate motor
##    pyrosim.Set_Motor_For_Joint(bodyIndex = robot, jointName = "Torso_BackLeg", controlMode = p.POSITION_CONTROL,
##                                targetPosition = targetAngles1[i], maxForce = 500)
##    pyrosim.Set_Motor_For_Joint(bodyIndex = robot, jointName = "Torso_FrontLeg", controlMode = p.POSITION_CONTROL,
##                                targetPosition = targetAngles2[i], maxForce = 500)
##    t.sleep(1/240)
##
### Save sensor values
##np.save('data/backLegSensorValues.npy', backLegSensorValues)
##np.save('data/frontLegSensorValues.npy', frontLegSensorValues)
##
### Close GUI
##p.disconnect()
##
### Print values
##print(backLegSensorValues)
##print(frontLegSensorValues)
