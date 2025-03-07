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

    #Solve it
    solution = sp.solve([eq1, eq2], (x, y))

    #Guard clause
    if not solution:
        raise ValueError("No solution")
    
    #Get the coordinate
    #Since we're using vector in inverse_kinematics
    #Need to have the sign correct
    x_coord = -x if Dl < Dr else x
    y_coord = y
    z_coord = 0

    object_position = np.array([x_coord, y_coord, z_coord])
    
    return object_position

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



'''