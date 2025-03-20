"""
This part of the code was about taking two depth from two cameras to convert into coordinate, while two cameras can only generate one depth
This code now could only work with the object standing in the middle of two cameras so the depth for both cameras will be the same
"""


#Cameras and the robot arm are all at the y = 0
import sympy as sp
import numpy as np
import StereoVision.distInf






def get_coordinate(depthL, depthR, camera_positionL, camera_positionR):
    #Get two depth from distInf
    MODEL_PATH = "./Model/model.tflite"
    LABELMAP_PATH = "./Model/labels.txt"
    depthL = StereoVision.distInf.detect(MODEL_PATH, LABELMAP_PATH)
    depthR = StereoVision.distInf.detect(MODEL_PATH, LABELMAP_PATH)

    #Distance between object and camera in 2D plane
    Dl = np.sqrt(depthL ** 2 - camera_positionL[2] ** 2)
    Dr = np.sqrt(depthR ** 2 - camera_positionR[2] ** 2)
    
    #Using sympy to construct a function
    x, y = sp.symbols('u v', nonnegative = True)
    eq1 = sp. Eq((x + abs(camera_positionL[0])) ** 2 + y ** 2, Dr ** 2)
    eq2 = sp. Eq((x - abs(camera_positionR[0])) ** 2 + y ** 2, Dl ** 2)

    #Solve x and y coord
    solution = sp.solve([eq1, eq2], (x, y))

    #Guard clause
    if not solution:
        raise ValueError("No solution")
    
    #Get z coord depending on whether the obect is at the left-hand side or the right
    distanceL = np.sqrt((x - camera_positionL[0]) ** 2 + y ** 2)
    midL = np.sqrt(depthL ** 2 - distanceL ** 2)
    zL = camera_positionL[2] - midL

    distanceR = np.sqrt((x - camera_positionL[0] ** 2 + y ** 2))
    midR = np.sqrt(depthR ** 2 - distanceR ** 2)
    zR = camera_positionR[2] - midR

    #Get the coordinate
    #Since we're using vector in inverse_kinematics
    #Need to have the sign correct
    x_coord = -x if Dl < Dr else x
    y_coord = y
    z_coord = zL if Dl < Dr else zR



    object_position = np.array([x_coord, y_coord, z_coord])
    
    return object_position

#TEST
camera_positionL = np.array([-3.5, 0, 30])
camera_positionR= np.array([3.5, 0, 30])
depthL = 10
depthR = 12
Vector = get_coordinate(depthL, depthR, camera_positionL, camera_positionR)
print(Vector)


'''
2d-distanceL < 2d-distanceR
x_cameraL = x_cameraR = x_camera

2d-distanceL = sqrt(depthL ** 2 - z_cameraL ** 2)
2d-distanceR = sqrt(depthR ** 2 - z_cameraR ** 2)

y_arm ** 2 + (x_arm - x_cameraL) ** 2 = 2d-distanceL ** 2
y_arm ** 2 + (x_arm + x_cameraR) ** 2 = 2d-distanceR ** 2

2 * x_arm * x_cameraR - 2 * x_arm * x_cameraL = 2d-distanceR ** 2 - 2d-distanceL ** 2
x_arm = 2d-distanceR ** 2 - 2d-distanceL ** 2)/2 * x_camera
y_arm = sqrt(2d-distanceL ** 2 - (x_arm - x_cameraL) ** 2)
z_arm = z_object


2d-distanceL > 2d-distanceR



(x-xcamera) ** 2 + y ** 2 = distance ** 2
a**2 = depth ** 2 - distance ** 2
height = camera height - a

'''