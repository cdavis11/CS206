import pybullet as p
import os
import constants as c
import time as t
import pybullet_data
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK

class ROBOT:

    def __init__(self, solutionID):

        self.solutionID = solutionID

        # Simulate robot
        self.robot = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate("body.urdf")

        # Call prepare to sense and act methods
        self.Prepare_To_Sense()
        self.Prepare_To_Act()

        # Call neural network constructor and create instance of it for that solution
        self.nn = NEURAL_NETWORK("brain" +str(self.solutionID)+ ".nndf")

        # Delete brain.nndf file for that solution
        os.system("rm brain" +str(self.solutionID)+ ".nndf")

    def Prepare_To_Sense(self):

        # Create empty dictionary of sensors
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            # Create sensor for each link by calling sensor constructor
            self.sensors[linkName] = SENSOR(linkName)

    # Get sensor values for each sensor
    def Sense(self, x):
        for i in self.sensors:
            self.sensors[i].Get_Value(x)

    def Prepare_To_Act(self):

        # Create empty dictionary of motors
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            # Call Motor constructor to create motor instance for each joint
            self.motors[jointName] = MOTOR(jointName)
        
    def Act(self, x):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName) * c.motorJointRange
                for i in self.motors:
                    self.motors[i].Set_Value(desiredAngle, self.robot)

    def Think(self):
        self.nn.Update()
        self.nn.Print()

    def Get_Fitness(self):

        # Get base position and orientation 
        basePositionAndOrientation = p.getBasePositionAndOrientation(self.robot)
        # Get base position
        basePosition = basePositionAndOrientation[0]
        # Get z coordinate of base postition
        zCoordinateOfLinkZero = basePosition[2]
        print(zCoordinateOfLinkZero)
        f = open("tmp" + str(self.solutionID) + ".txt","w")
        f.write(str(zCoordinateOfLinkZero))
        f.close()
        os.system("mv tmp" + str(self.solutionID) + ".txt fitness" + str(self.solutionID) + ".txt")
        
        


        
