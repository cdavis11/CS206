# Created by Claire Davis
# CS 206 Assingment 1

import pybullet as p
import time as t
import pybullet_data

# Display GUI
physicsClient = p.connect(p.GUI)

p.setAdditionalSearchPath(pybullet_data.getDataPath())

# Add gravitational force
p.setGravity(0,0,-9.8)

# Add floor
planeId = p.loadURDF("plane.urdf")

# Simulate robot
bodyId = p.loadURDF("body.urdf")

# Import box
p.loadSDF("world.sdf")

# Create loop to make GUI visibe for ~16 seconds
for i in range (0, 1000):
    p.stepSimulation()
    t.sleep(1/60)
    
# Close GUI
p.disconnect()
