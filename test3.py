# a test for jaco in pybullet

import os
import pybullet as p
import pybullet_data

# connecting to pybullet
p.connect(p.GUI)
urdfRootPath=pybullet_data.getDataPath()

# adding the robot
jacoUid = p.loadURDF(os.path.join(urdfRootPath,"jaco/j2s7s300_gym.urdf"), useFixedBase=True)

# adding the table 
tableUid = p.loadURDF(os.path.join(urdfRootPath, "table/table.urdf"),basePosition=[0.5,0,-0.65])

# adding the tray
trayUid = p.loadURDF(os.path.join(urdfRootPath, "tray/traybox.urdf"),basePosition=[0.65,0,0])

# adding a random object for grasping
p.setGravity(0,0,-10)
objectUid = p.loadURDF(os.path.join(urdfRootPath, "random_urdfs/000/000.urdf"), basePosition=[0.7,0,0.1])

# changing the view for camera 
p.resetDebugVisualizerCamera(cameraDistance=1.5, cameraYaw=0, cameraPitch=-40, cameraTargetPosition=[0.55,-0.35,0.2])


while True:
    p.stepSimulation()
