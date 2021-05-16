import os
from parallelHillClimber import PARALLEL_HILL_CLIMBER
import numpy as np

# Create instance of parallel hill climber
phc = PARALLEL_HILL_CLIMBER()
# Call phc evolve method
phc.Evolve()
# Call phc show best method
phc.Show_Best()

np.save('fitnessMatrixB.npy',phc.fitnessMatrix)
