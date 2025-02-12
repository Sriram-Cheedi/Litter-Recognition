# Code to undistort and rectify images - requires stereoMap.xml
import sys
import numpy as np
import time
import imutils
import cv2

# Camera params to undistort and rectify images
file = cv2.FileStorage()
file.open('stereoMap.xml', cv2.FileStorage_READ)

stereoMapL_x = file.getNode('stereoMapL_x').mat()
stereoMapL_y = file.getNode('stereoMapL_y').mat()
stereoMapR_x = file.getNode('stereoMapR_x').mat()
stereoMapR_y = file.getNode('stereoMapR_y').mat()

# Use our parameters to 'fix' the image
def undistortRect(leftFrame, rightFrame):
    leftUndistorted = cv2.remap(leftFrame, stereoMapL_x, stereoMapL_y, cv2.INTER_LANCZOS4, cv2.BORDER_CONSTANT, 0)
    rightUndistorted = cv2.remap(rightFrame, stereoMapR_x, stereoMapR_y, cv2.INTER_LANCZOS4, cv2.BORDER_CONSTANT, 0)
    
    return leftUndistorted, rightUndistorted