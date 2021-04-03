import pybullet as p
import os
import time as t
import pybullet_data
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK

class ROBOT:

    # Initializer
    def __init__(self, solutionID):
        self.solutionID = solutionID
        # Simulate robot
        self.robot = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate("body.urdf")
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        self.nn = NEURAL_NETWORK("brain" +str(self.solutionID)+ ".nndf")
        os.system("rm brain" +str(self.solutionID)+ ".nndf")

    # Create dictionary of sensors
    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            # Create sensor for each link
            self.sensors[linkName] = SENSOR(linkName)

    # Get sensor values for each sensor
    def Sense(self, x):
        for i in self.sensors:
            self.sensors[i].Get_Value(x)

    # Create dictionary of motors
    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)
        
    def Act(self, x):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                for i in self.motors:
                    self.motors[i].Set_Value(desiredAngle, self.robot)

    def Think(self):
        self.nn.Update()
        self.nn.Print()

    def Get_Fitness(self):
        stateOfLinkZero = p.getLinkState(self.robot,0)
        positionOfLinkZero = stateOfLinkZero[0]
        xCoordinateOfLinkZero = positionOfLinkZero[0]
        print(xCoordinateOfLinkZero)
        f = open("fitness" + str(self.solutionID) + ".txt","w")
        f.write(str(xCoordinateOfLinkZero))
        f.close()
        exit()
        
        


        
