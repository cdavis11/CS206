import pybullet as p
import time as t
import pybullet_data

class WORLD:

    def __init__(self):

        # Add floor
        self.planeId = p.loadURDF("plane.urdf")
        # Import box
        p.loadSDF("world.sdf")
