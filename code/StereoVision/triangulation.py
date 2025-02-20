# Code containing formulas for depth calculation

import sys
import cv2
import numpy as np
import time

def findDepth(leftPoint, rightPoint, captureLeft, captureRight, camDist, focalLength, alpha):
    # Convert the focal length from mm to pixels
    leftHeight, leftWidth, leftDepth = captureLeft.shape
    rightHeight, rightWidth, rightDepth = captureRight.shape
    
    if leftWidth == rightWidth:
        focalPixel = (rightWidth * 0.5) / np.tan(alpha * 0.5 * np.pi/180)
    else: 
        print("Left and right frames do not have the same width")
    
    leftX = leftPoint[0]    
    rightX = rightPoint[0]
    
    # Calculate disparity between frames
    disparity = leftX - rightX
    
    # Calculate depth
    depth = (camDist*focalPixel)/disparity
    
    return abs(depth)
    