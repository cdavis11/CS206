import numpy as np
import os
import pyrosim.pyrosim as pyrosim
import random

class SOLUTION:

    def __init__(self):
        self.weights = np.random.rand(3,2)
        self.weights = self.weights *2 -1
       
    def Evaluate(self, directORGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        os.system('python simulate.py ' + directORGUI)
        f = open("fitness.txt", "r")
        self.fitness = float(f.read())

    def Create_World(self):
        # Create box.sdf file
        pyrosim.Start_SDF("world.sdf")

        # Define box coordinates
        x = -2
        y = -2
        z = 0.5

        # Define box dimensions
        length = 1
        width = 1
        height = 1

        pyrosim.Send_Cube(name="Box", pos=[x, y, z] , size=[length, width, height])
        pyrosim.End()

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        # Define Torso, Relative Leg coordinates
        x = 1.5
        y = 0
        z = 1.5
        xl = -0.5
        yl = 0
        zl = -0.5
        xr = 0.5
        yr = 0
        zr = -0.5

        # Define Torso, Leg dimensions
        length = 1
        width = 1
        height = 1

        # Create Torso
        pyrosim.Send_Cube(name="Torso", pos=[x, y, z] , size=[length, width, height])
        # Create Torso, back leg joint
        pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = "1 0 1")
        # Create Back Leg
        pyrosim.Send_Cube(name="BackLeg", pos=[xl, yl, zl] , size=[length, width, height])
        # Create Torso, front leg joint
        pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = "2 0 1")
        # Create Front leg
        pyrosim.Send_Cube(name="FrontLeg", pos=[xr, yr, zr] , size=[length, width, height])
        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain.nndf")
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
        pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")
        for currentRow in range(0,3):
            for currentColumn in range(0,2):
                pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn + 3 , weight = self.weights[currentRow][currentColumn] )
        pyrosim.End()

    def Mutate(self):
        randRow = random.randint(0,2)
        randCol = random.randint(0,1)
        self.weights[randRow,randCol] = random.random() * 2 - 1.
         
