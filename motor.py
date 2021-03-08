import constants as c
import numpy as np
import math
import pyrosim.pyrosim as pyrosim
import pybullet as p

class MOTOR:

    # Initializer
    def __init__(self, jointName):
        self.jointName = jointName
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        if self.jointName == "Torso_FrontLeg":
            self.amplitude = c.amp1
            self.frequency = c.freq1
            self.offset = c.phase1
        else:
            self.amplitude = c.amp2
            self.frequency = c.freq2
            self.offset = c.phase2
            
        # Create sinusoidal vector
        self.motorValues = self.amplitude*np.sin(self.frequency*(np.linspace(-math.pi, math.pi, 1000)) + self.offset)

    def Set_Value(self,x, robot):
        # Simulate motor
        pyrosim.Set_Motor_For_Joint(bodyIndex = robot, jointName = self.jointName, controlMode = p.POSITION_CONTROL,
                                    targetPosition = self.motorValues[x], maxForce = 500)

    def Save_Values(self):
        # Save motor values
        np.save('data/motorValues.npy', self.motorValues)

            
