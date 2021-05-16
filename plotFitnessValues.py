import numpy as np
import matplotlib.pyplot


fitnessMatrixA = np.load('fitnessMatrixA.npy')
fitnessMatrixB = np.load('fitnessMatrixB.npy')
fitnessMatrixA = np.reshape(fitnessMatrixA, (10,10))
fitnessMatrixB = np.reshape(fitnessMatrixB, (10,10))

avgFitnessA = np.mean(fitnessMatrixA, axis=0)
avgFitnessB = np.mean(fitnessMatrixB, axis=0)

sA = np.std(fitnessMatrixA, axis=0)
sB = np.std(fitnessMatrixB, axis=0)

matplotlib.pyplot.plot(avgFitnessA, label="Average fitness Quadruped")
matplotlib.pyplot.plot(avgFitnessA+sA, label="Average fitness Quadruped + stdev")
matplotlib.pyplot.plot(avgFitnessA-sA, label="Average fitness Quadruped - stdev")
matplotlib.pyplot.plot(avgFitnessB, label= "Average fitness daddy long legs")
matplotlib.pyplot.plot(avgFitnessB+sA, label="Average fitness daddy long legs + stdev")
matplotlib.pyplot.plot(avgFitnessB-sA, label="Average fitness daddy long legs - stdev")
matplotlib.pyplot.xlabel('Number of generations')
matplotlib.pyplot.ylabel('Average fitness value')
matplotlib.pyplot.legend()
matplotlib.pyplot.show()
