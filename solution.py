import numpy as np
import time
import os
import pyrosim.pyrosim as pyrosim
import random
import constants as c

class SOLUTION:

    def __init__(self,nextAvailableID):

        # Set ID number to passed in argument
        self.myID = nextAvailableID
        # Create marix of random weights with dimensions of number of sensor neurons by number of motor neurons 
        self.weights = np.random.rand(c.numSensorNeurons,c.numMotorNeurons)
        #Make weights range from 1 to -1
        self.weights = self.weights *2 -1

        # Create matrix of random values from 0-2 for upper and lower legs
        self.lengths = np.random.rand(1,2)
        self.lengths = self.lengths +1

    def Set_ID(self, nextAvailableID):
        self.myID = nextAvailableID

    def Start_Simulation(self, directORGUI):

        # Call create word, body and brain methods
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()

        # System call to run simulate.py
        os.system("python simulate.py " + directORGUI + " " + str(self.myID) + " &")
        # While a fitness file for the last ID does not exist, call time.sleep
        while not os.path.exists("fitness" + str(self.myID) + ".txt"):
            time.sleep(0.01)

    def Wait_For_Simulation_To_End(self):

        # Open fitness file of last ID 
        f = open("fitness" + str(self.myID) + ".txt", "r")
        # read fitness value and set to self.fitness
        self.fitness = float(f.read())
        f.close()

        # System call to remove that fitness file
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

        # Send cube
        pyrosim.Send_Cube(name="Box", pos=[x, y, z] , size=[length, width, height])

        pyrosim.End()

    def Create_Body(self):

        pyrosim.Start_URDF("body.urdf")
        
        # Create Torso
        pyrosim.Send_Cube(name="Torso", pos=[0, 0, self.lengths[0,1]] , size=[1, 1, 1])

        # Create Torso, back leg joint
        pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = "0 -0.5 " +str(self.lengths[0,1]), jointAxis = "1 0 0")
        # Create Back Leg
        pyrosim.Send_Cube(name="BackLeg", pos=[0, -self.lengths[0,0]/2, 0] , size=[0.2, self.lengths[0,0], 0.2])

        # Create Torso, front leg joint
        pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = "0 0.5 " +str(self.lengths[0,1]), jointAxis = "1 0 0")
        # Create Front leg
        pyrosim.Send_Cube(name="FrontLeg", pos=[0, self.lengths[0,0]/2, 0] , size=[0.2, self.lengths[0,0], 0.2])

        # Create Torso, left leg joint
        pyrosim.Send_Joint( name = "Torso_LeftLeg" , parent= "Torso" , child = "LeftLeg" , type = "revolute", position = "-0.5 0 " +str(self.lengths[0,1]), jointAxis = "0 1 0")
        # Create Left leg
        pyrosim.Send_Cube(name="LeftLeg", pos=[-self.lengths[0,0]/2, 0, 0] , size=[self.lengths[0,0], 0.2, 0.2])

        # Create Torso, right leg joint
        pyrosim.Send_Joint( name = "Torso_RightLeg" , parent= "Torso" , child = "RightLeg" , type = "revolute", position = "0.5 0 " +str(self.lengths[0,1]), jointAxis = "0 1 0")
        # Create Right leg
        pyrosim.Send_Cube(name="RightLeg", pos=[self.lengths[0,0]/2, 0, 0] , size=[self.lengths[0,0], 0.2, 0.2])


        # Create back leg joint
        pyrosim.Send_Joint( name = "BackLeg_LowerBackLeg" , parent= "BackLeg" , child = "LowerBackLeg" , type = "revolute", position = "0 " + str(-self.lengths[0,0]) + " 0", jointAxis = "1 0 0")
        # Create lower back leg
        pyrosim.Send_Cube(name="LowerBackLeg", pos=[0, 0, -self.lengths[0,1]/2] , size=[0.2, 0.2, self.lengths[0,1]])

        # Create front leg joint
        pyrosim.Send_Joint( name = "FrontLeg_LowerFrontLeg" , parent= "FrontLeg" , child = "LowerFrontLeg" , type = "revolute", position = "0 " + str(self.lengths[0,0]) + " 0", jointAxis = "1 0 0")
        # Create lower front leg
        pyrosim.Send_Cube(name="LowerFrontLeg", pos=[0, 0, -self.lengths[0,1]/2] , size=[0.2, 0.2, self.lengths[0,1]])

        # Create right leg joint
        pyrosim.Send_Joint( name = "RightLeg_LowerRightLeg" , parent= "RightLeg" , child = "LowerRightLeg" , type = "revolute", position = str(self.lengths[0,0]) + " 0 0", jointAxis = "0 1 0")
        # Create lower right leg
        pyrosim.Send_Cube(name="LowerRightLeg", pos=[0, 0, -self.lengths[0,1]/2] , size=[0.2, 0.2, self.lengths[0,1]])

        # Create left leg joint
        pyrosim.Send_Joint( name = "LeftLeg_LowerleftLeg" , parent= "LeftLeg" , child = "LowerLeftLeg" , type = "revolute", position = str(-self.lengths[0,0]) + " 0 0", jointAxis = "0 1 0")
        # Create lower left leg
        pyrosim.Send_Cube(name="LowerLeftLeg", pos=[0, 0, -self.lengths[0,1]/2] , size=[0.2, 0.2, self.lengths[0,1]])

        pyrosim.End()

    def Create_Brain(self):

        # Create brain.nndf file
        pyrosim.Start_NeuralNetwork("brain"+str(self.myID)+".nndf")
        # List sensor neurons
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
        pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "LeftLeg")
        pyrosim.Send_Sensor_Neuron(name = 4 , linkName = "RightLeg")
        pyrosim.Send_Sensor_Neuron(name = 5 , linkName = "LowerBackLeg")
        pyrosim.Send_Sensor_Neuron(name = 6 , linkName = "LowerFrontLeg")
        pyrosim.Send_Sensor_Neuron(name = 7 , linkName = "LowerRightLeg")
        pyrosim.Send_Sensor_Neuron(name = 8 , linkName = "LowerLeftLeg")
        # List motor neurons
        pyrosim.Send_Motor_Neuron( name = 9 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 10 , jointName = "Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron( name = 11 , jointName = "Torso_LeftLeg")
        pyrosim.Send_Motor_Neuron( name = 12 , jointName = "Torso_RightLeg")
        pyrosim.Send_Motor_Neuron( name = 13 , jointName = "BackLeg_LowerBackLeg")
        pyrosim.Send_Motor_Neuron( name = 14 , jointName = "FrontLeg_LowerFrontLeg")
        pyrosim.Send_Motor_Neuron( name = 15 , jointName = "RightLeg_LowerRightLeg")
        pyrosim.Send_Motor_Neuron( name = 16 , jointName = "LeftLeg_LowerLeftLeg")

        # Loop through matrix of synaptic weights
        for currentRow in range(0,c.numSensorNeurons):
            for currentColumn in range(0,c.numMotorNeurons):
                # Create synapses between each sensor and motor neuron 
                pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn + c.numSensorNeurons , weight = self.weights[currentRow][currentColumn] )

        pyrosim.End()

    def Mutate(self):
        randRow = random.randint(0,c.numSensorNeurons-1)
        randCol = random.randint(0,c.numMotorNeurons-1)
        self.weights[randRow,randCol] = random.random() * 2 - 1

        randCol2 = random.randint(0,1)
        self.lengths[0,randCol2] = random.random() +1
        
         
