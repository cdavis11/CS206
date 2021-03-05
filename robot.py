import pybullet as p
import time as t
import pybullet_data
import pyrosim.pyrosim as pyrosim

class ROBOT:
    def __init__(self):
        # Simulate robot
        robot = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate("body.urdf")
