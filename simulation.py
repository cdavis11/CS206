from world import WORLD
from robot import ROBOT
import pybullet as p
import time as t
import pybullet_data
import pyrosim.pyrosim as pyrosim

class SIMULATION:

    # Initializer
    def __init__(self):
        # Display GUI
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())

        #Add gravitational force
        p.setGravity(0,0,-9.8)

        self.world = WORLD()
        self.robot = ROBOT()

    # Destructor
    def __del__(self):
        p.disconnect()

    # Run simulation    
    def Run(self):
        # Create loop to make GUI visibe for ~16 seconds
        for i in range (0, 1000):
            p.stepSimulation()
##            # Add sensor to back and front leg
##            backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
##            frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
##            # Simulate motor
##            pyrosim.Set_Motor_For_Joint(bodyIndex = robot, jointName = "Torso_BackLeg", controlMode = p.POSITION_CONTROL,
##                                        targetPosition = targetAngles1[i], maxForce = 500)
##            pyrosim.Set_Motor_For_Joint(bodyIndex = robot, jointName = "Torso_FrontLeg", controlMode = p.POSITION_CONTROL,
##                                        targetPosition = targetAngles2[i], maxForce = 500)
            t.sleep(1/240)
            print(i)
