from world import WORLD
from robot import ROBOT
from sensor import SENSOR
import pybullet as p
import time as t
import pybullet_data
import pyrosim.pyrosim as pyrosim

class SIMULATION:

    # Initializer
    def __init__(self, directOrGUI, solutionID):
        self.directOrGUI = directOrGUI
        if directOrGUI == "DIRECT":
            p.connect(p.DIRECT)
        else:
            # Display GUI
            self.physicsClient = p.connect(p.GUI)

        p.setAdditionalSearchPath(pybullet_data.getDataPath())

        #Add gravitational force
        p.setGravity(0,0,-9.8)

        self.world = WORLD()
        self.robot = ROBOT(solutionID)

    # Destructor
    def __del__(self):
        p.disconnect()

    # Run simulation    
    def Run(self):
        # Create loop to make GUI visibe for ~16 seconds
        for i in range (0, 1000):
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)
            #if self.directOrGUI == "GUI":
                #t.sleep(1/60)

    def Get_Fitness(self):
        self.robot.Get_Fitness()
