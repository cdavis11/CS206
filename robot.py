import pybullet as p
import time as t
import pybullet_data
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR

class ROBOT:

    # Initializer
    def __init__(self):
        # Simulate robot
        self.robot = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate("body.urdf")
        self.Prepare_To_Sense()
        self.Prepare_To_Act()

    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            # Create sensor for each link
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, x):
        for i in self.sensors:
            self.sensors[i].Get_Value(x)

    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)
            
    def Act(self, x):
        for i in self.motors:
            self.motors[i].Set_Value(x, self.robot)
        


        
