import constants as c
import numpy as np
import math
import pyrosim.pyrosim as pyrosim
import pybullet as p

class MOTOR:

    # Initializer
    def __init__(self, jointName):
        self.jointName = jointName

    def Set_Value(self,desiredAngle, robot):
        # Simulate motor
        pyrosim.Set_Motor_For_Joint(bodyIndex = robot, jointName = self.jointName, controlMode = p.POSITION_CONTROL,
                                    targetPosition = desiredAngle, maxForce = 500)



            
