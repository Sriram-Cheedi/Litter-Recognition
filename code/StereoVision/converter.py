import sympy as sp
import numpy as np
import StereoVision.distInf


def get_coordinate(depthL, depthR, Xl, Yl, Zl, Xr, Yr, Zr):
    #Get two depth from distInf
    MODEL_PATH = "./Model/model.tflite"
    LABELMAP_PATH = "./Model/labels.txt"
    depthL = StereoVision.distInf.detect(MODEL_PATH, LABELMAP_PATH)
    depthR = StereoVision.distInf.detect(MODEL_PATH, LABELMAP_PATH)

    #Distance between object and camera in 2D plane
    Dl = np.sqrt(depthL ** 2 - Zl ** 2)
    Dr = np.sqrt(depthR ** 2 - Zr ** 2)
    
    x, y = sp.symbols('u v', nonnegative = True)
    eq1 = sp. Eq((x + 5) ** 2 + y ** 2, Dr ** 2)
    eq2 = sp. Eq((x - 5) ** 2 + y ** 2, Dl ** 2)

    solution = sp.solve([eq1, eq2], (x, y))
    if not solution:
        raise ValueError("No solution")
    

    x_coord = -x if Dl < Dr else x
    y_coord = y
    z_coord = 0

    return np.array([x_coord, y_coord, z_coord])

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