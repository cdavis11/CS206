import pyrosim.pyrosim as pyrosim

# Create box.sdf file
pyrosim.Start_SDF("boxes.sdf")

# Define box x coordinate
x = 0

for i in range (0,6):
    
    # Define box y coordinate
    y = 0

    for j in range (0,6):

        # Define box z coordinate
        z = 0.5

        length = 1
        width = 1
        height = 1
        for k in range (0,10):
         
            # Set size and position of box
            pyrosim.Send_Cube(name="Box", pos=[x, y, z] , size=[length, width, height])
            z = z + height/2
            length = 0.9*length
            width = 0.9*width
            height = 0.9*height
            z = z + height/2
        y = y + 1
    x = x + 1

pyrosim.End()