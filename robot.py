import pybullet as p
import time as t
import pybullet_data
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR

class ROBOT:

    # Initializer
    def __init__(self):
        # Simulate robot
        robot = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate("body.urdf")
        self.Prepare_To_Sense()

    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            # Create sensor for each link
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, x):
        for i in self.sensors:
            self.sensors[i].Get_Value(x)
            
        


        
