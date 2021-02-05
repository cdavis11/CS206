# Created by Claire Davis
# CS 206 Assingment 1

import pybullet as p
import time as t

# Display GUI
physicsClient = p.connect(p.GUI)

# Read in box
p.loadSDF("box.sdf")

# Create loop to make GUI visibe for ~16 seconds
for i in range (0, 1000):
    p.stepSimulation()
    t.sleep(1/60)
    
# Close GUI
p.disconnect()
