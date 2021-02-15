import pyrosim.pyrosim as pyrosim

def Create_World():
    # Create box.sdf file
    pyrosim.Start_SDF("world.sdf")

    # Define box coordinates
    x = -2
    y = -2
    z = 0.5

    # Define box dimensions
    length = 1
    width = 1
    height = 1

    pyrosim.Send_Cube(name="Box", pos=[x, y, z] , size=[length, width, height])


    pyrosim.End()

def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    # Define Torso, Relative Leg coordinates
    x = 1.5
    y = 0
    z = 1.5
    xl = -0.5
    yl = 0
    zl = -0.5
    xr = 0.5
    yr = 0
    zr = -0.5

    # Define Torso, Leg dimensions
    length = 1
    width = 1
    height = 1

    # Create Torso
    pyrosim.Send_Cube(name="Torso", pos=[x, y, z] , size=[length, width, height])
    # Create Torso, back leg joint
    pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = "1 0 1")
    # Create Back Leg
    pyrosim.Send_Cube(name="BackLeg", pos=[xl, yl, zl] , size=[length, width, height])
    # Create Torso, front leg joint
    pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = "2 0 1")
    # Create Front leg
    pyrosim.Send_Cube(name="FrontLeg", pos=[xr, yr, zr] , size=[length, width, height])
    pyrosim.End()

Create_World()
Create_Robot()
