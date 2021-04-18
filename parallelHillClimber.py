from solution import SOLUTION
import constants as c
import os
import copy
import time

class PARALLEL_HILL_CLIMBER:

    def __init__(self):
        
        # Delete any brain or fitness files existing in directory
        os.system("rm brain*.nndf")
        os.system("rm fitness*.txt")

        # Initialize next available ID value
        self.nextAvailableID = 0
        # Create empty parent directory
        self.parents = {}

        for i in range(0, c.populationSize):
            # Create instance of Solution and set it to ith parent dict element
            self.parents[i] = SOLUTION(self.nextAvailableID)
            # Increment next available ID
            self.nextAvailableID += 1

    def Evolve(self):

        # Call own evaluate method
        self.Evaluate(self.parents)
        for currentGeneration in range(0,c.numberOfGenerations):
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()

    def Spawn(self):
        self.children ={}
        for i in self.parents:
            self.children[i] = copy.deepcopy(self.parents[i])
            self.children[i].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1;

    def Mutate(self):
        for i in self.children:
            self.children[i].Mutate()

    def Evaluate(self, solutions):

        # Call start simulation method for each solution in parents dict
        for i in self.parents:
            solutions[i].Start_Simulation("DIRECT")
        # Call Wait for simulation to end method for each solution in parents dict
        for i in self.parents:
            solutions[i].Wait_For_Simulation_To_End()

    def Print(self):
        print("\n")
        for i in self.parents:
            print(self.parents[i].fitness, self.children[i].fitness)
        print("\n")
        
    def Select(self):
        for i in self.parents:
            if (self.parents[i].fitness < self.children[i].fitness):
                self.parents[i] = self.children[i]

    def Show_Best(self):
        best = -1000
        bestIndex = 0
        for i in self.parents:
            if self.parents[i].fitness > best:
                best = self.parents[i].fitness
                bestIndex = i
        self.parents[bestIndex].Start_Simulation("GUI")
