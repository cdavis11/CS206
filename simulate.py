# Created by Claire Davis
# CS 206 Assingment 1

from simulation import SIMULATION
import sys

# Get command line input
directOrGUI = sys.argv[1]

# Pass direct or GUI into Simulation's constructor
simulation = SIMULATION(directOrGUI)
simulation.Run()
simulation.Get_Fitness()

