from solution import SOLUTION
import constants as c
import copy

class PARALLEL_HILL_CLIMBER:
    
    def __init__(self):
        self.nextAvailableID = 0
        self.parents = {}
        for i in range(0, c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1

    def Evolve(self):
        for i in self.parents:
            self.parents[i].Evaluate("GUI")
##        for currentGeneration in range(0,c.numberOfGenerations):
##            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate("DIRECT")
        self.Print()
        self.Select()

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)
        self.child.Set_ID(self.nextAvailableID)
        self.nextAvailableID += 1;
        

    def Mutate(self):
        self.child.Mutate()

    def Print(self):
        print(self.parent.fitness, self.child.fitness)
        
    def Select(self):
        if (self.parent.fitness > self.child.fitness):
            self.parent = self.child

    def Show_Best(self):
        #self.parent.Evaluate("GUI")
        pass
