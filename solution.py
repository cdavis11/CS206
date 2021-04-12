import numpy as np
import time
import os
import pyrosim.pyrosim as pyrosim
import random
import constants as c

class SOLUTION:

    def __init__(self,nextAvailableID):
        self.myID = nextAvailableID
        self.weights = np.random.rand(c.numSensorNeurons,c.numMotorNeurons)
        self.weights = self.weights *2 -1

    def Set_ID(self, nextAvailableID):
        self.myID = nextAvailableID

    def Start_Simulation(self, directORGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        os.system("python simulate.py " + directORGUI + " " + str(self.myID) + " &")
        while not os.path.exists("fitness" + str(self.myID) + ".txt"):
            time.sleep(0.01)

    def Wait_For_Simulation_To_End(self):
        f = open("fitness" + str(self.myID) + ".txt", "r")
        self.fitness = float(f.read())
        f.close()
        #print(self.fitness)
        os.system("rm fitness" + str(self.myID) + ".txt")

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
        x = 0
        y = 0
        z = 1
        xb = 0
        yb = -0.5
        zb = 0
        xf = 0
        yf = 0.5
        zf = 0
        xl = -0.5
        yl = 0
        zl = 0
        xr = 0.5
        yr = 0
        zr = 0
        
        # Define Torso, Leg dimensions
        length = 1
        width = 1
        height = 1

        # Create Torso
        pyrosim.Send_Cube(name="Torso", pos=[x, y, z] , size=[length, width, height])
        # Create Torso, back leg joint
        pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = "0 -0.5 1", jointAxis = "1 0 0")
        # Create Back Leg
        pyrosim.Send_Cube(name="BackLeg", pos=[xb, yb, zb] , size=[0.2, 1, 0.2])
        # Create Torso, front leg joint
        pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = "0 0.5 1", jointAxis = "1 0 0")
        # Create Front leg
        pyrosim.Send_Cube(name="FrontLeg", pos=[xf, yf, zf] , size=[0.2, 1, 0.2])
        # Create Torso, left leg joint
        pyrosim.Send_Joint( name = "Torso_LeftLeg" , parent= "Torso" , child = "LeftLeg" , type = "revolute", position = "-0.5 0 1", jointAxis = "0 1 0")
        # Create Left leg
        pyrosim.Send_Cube(name="LeftLeg", pos=[xl, yl, zl] , size=[1, 0.2, 0.2])
        # Create Torso, right leg joint
        pyrosim.Send_Joint( name = "Torso_RightLeg" , parent= "Torso" , child = "RightLeg" , type = "revolute", position = "0.5 0 1", jointAxis = "0 1 0")
        # Create Right leg
        pyrosim.Send_Cube(name="RightLeg", pos=[xr, yr, zr] , size=[1, 0.2, 0.2])

        # Create back leg joint
        pyrosim.Send_Joint( name = "BackLeg_LowerBackLeg" , parent= "BackLeg" , child = "LowerBackLeg" , type = "revolute", position = "0 -0.5 0", jointAxis = "1 0 0")
        # Create lower back leg
        pyrosim.Send_Cube(name="LowerBackLeg", pos=[0, -0.5, -0.5] , size=[0.2, 0.2, 1])
        # Create front leg joint
        pyrosim.Send_Joint( name = "FrontLeg_LowerFrontLeg" , parent= "FrontLeg" , child = "LowerFrontLeg" , type = "revolute", position = "0 0.5 0", jointAxis = "1 0 0")
        # Create lower front leg
        pyrosim.Send_Cube(name="LowerFrontLeg", pos=[0, 0.5, -0.5] , size=[0.2, 0.2, 1])
        # Create right leg joint
        pyrosim.Send_Joint( name = "RightLeg_LowerRightLeg" , parent= "RightLeg" , child = "LowerRightLeg" , type = "revolute", position = "0.5 0 0", jointAxis = "0 1 0")
        # Create lower right leg
        pyrosim.Send_Cube(name="LowerRightLeg", pos=[0.5, 0, -0.5] , size=[0.2, 0.2, 1])
        # Create left leg joint
        pyrosim.Send_Joint( name = "LeftLeg_LowerleftLeg" , parent= "LeftLeg" , child = "LowerLeftLeg" , type = "revolute", position = "-0.5 0 0", jointAxis = "0 1 0")
        # Createlower left leg
        pyrosim.Send_Cube(name="LowerLeftLeg", pos=[-0.5, 0, -0.5] , size=[0.2, 0.2, 1])
        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain"+str(self.myID)+".nndf")
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
        pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "LeftLeg")
        pyrosim.Send_Sensor_Neuron(name = 4 , linkName = "RightLeg")
        pyrosim.Send_Sensor_Neuron(name = 5 , linkName = "LowerBackLeg")
        pyrosim.Send_Sensor_Neuron(name = 6 , linkName = "LowerFrontLeg")
        pyrosim.Send_Sensor_Neuron(name = 7 , linkName = "LowerRightLeg")
        pyrosim.Send_Sensor_Neuron(name = 8 , linkName = "LowerLeftLeg")

        pyrosim.Send_Motor_Neuron( name = 9 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 10 , jointName = "Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron( name = 11 , jointName = "Torso_LeftLeg")
        pyrosim.Send_Motor_Neuron( name = 12 , jointName = "Torso_RightLeg")
        pyrosim.Send_Motor_Neuron( name = 13 , jointName = "BackLeg_LowerBackLeg")
        pyrosim.Send_Motor_Neuron( name = 14 , jointName = "FrontLeg_LowerFrontLeg")
        pyrosim.Send_Motor_Neuron( name = 15 , jointName = "RightLeg_LowerRightLeg")
        pyrosim.Send_Motor_Neuron( name = 16 , jointName = "LeftLeg_LowerLeftLeg")
        for currentRow in range(0,c.numSensorNeurons):
            for currentColumn in range(0,c.numMotorNeurons):
                pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn + c.numSensorNeurons , weight = self.weights[currentRow][currentColumn] )
        pyrosim.End()

    def Mutate(self):
        randRow = random.randint(0,c.numSensorNeurons-1)
        randCol = random.randint(0,c.numMotorNeurons-1)
        self.weights[randRow,randCol] = random.random() * 2 - 1.
         
