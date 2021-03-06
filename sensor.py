import numpy as np
import pyrosim.pyrosim as pyrosim

class SENSOR:

    # Initializer
    def __init__(self, linkName):
        self.linkName = linkName

        # Create vectors filled with 0s
        self.values = np.zeros(1000)

    def Get_Value(self,x):
        # Add sensor to back and front leg
        self.values[x] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        if self.values[-1] != 0:
            print(self.values)

    
        
    
    
