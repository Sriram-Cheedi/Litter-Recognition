# Code to calibrate our cameras using the images obtained in take_Images.py

import numpy as np
import cv2
import glob


def findCorners():
    boardSize = (8, 6)
    distanceBetweenCorners = 2 # Needs distance between corners of board in CM
    
    # Termination criteria for calibration
    termCrit = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
    
    # Prepare points
    points = np.zeros((boardSize[0] * boardSize[1], 3), np.float32)
    points[:, :2] = np.mgrid[0:boardSize[0],0:boardSize[1]].T.reshape(-1, 2)
    
    points = points * 10 * distanceBetweenCorners
    print(points)
    
    # Arrays intialised to store object and image points
    objPoints = [] # 3D point in real world
    lImgPoints = [] # 2D point in image plane
    rImgPoints = [] 

    # Gets calibration images
    leftImages = glob.glob('calibration_images/left/*.png')
    rightImages = glob.glob('calibration_images/right/*.png')
    
    for leftImage, rightImage in zip(leftImages, rightImages):
        imgL = cv2.imread(leftImage)
        imgR = cv2.imread(rightImage)
        grayL = cv2.cvtColor(imgL, cv2.COLOR_BGR2GRAY)
        grayR = cv2.cvtColor(imgR, cv2.COLOR_BGR2GRAY)
        
        # Finds the corners
        lStatus, lCorners = cv2.findChessboardCorners(grayL, boardSize, None)
        rStatus, rCorners = cv2.findChessboardCorners(grayR, boardSize, None)
        
        # If corners found, add object and image points
        if lStatus and rStatus:
            print("Corners detected")
            objPoints.append(points)
            
            # Finds corners in sub pixels for better accuracy
            lCorners = cv2.cornerSubPix(grayL, lCorners, (11, 11), (-1, -1), termCrit)
            lImgPoints.append(lCorners)
            
            rCorners = cv2.cornerSubPix(grayR, rCorners, (11, 11), (-1, -1), termCrit)
            rImgPoints.append(rCorners)
            
            # Draw and display corners
            cv2.drawChessboardCorners(imgL, boardSize, lCorners, lStatus)
            cv2.imshow('Left Image', imgL)
            cv2.drawChessboardCorners(imgR, boardSize, rCorners, rStatus)
            cv2.imshow('Right Image', imgR)
            cv2.waitKey(1000)
        
    cv2.destroyAllWindows()
    return objPoints, lImgPoints, rImgPoints, imgL, imgR, grayL, grayR
    
# Calibrates the cameras and stereovision
def calibrate(objPoints, lImgPoints, rImgPoints, imgL, imgR, grayL, grayR):
    imageSize = (640, 480)
    #TESTING LINES
    print(f"objPoints length: {len(objPoints)}")
    print(f"lImgPoints length: {len(lImgPoints)}")
    print(f"rImgPoints length: {len(rImgPoints)}")

    # Camera calibration
    lStatus, lCamMatrix, lDist, lRvecs, lTvecs = cv2.calibrateCamera(objPoints, lImgPoints, imageSize, None, None)
    lHeight, lWidth, lChannels = imgL.shape
    lNewCamMatrix, lRoi = cv2.getOptimalNewCameraMatrix(lCamMatrix, lDist, (lWidth, lHeight), 1, (lWidth, lHeight))
    
    rStatus, rCamMatrix, rDist, rRvecs, rTvecs = cv2.calibrateCamera(objPoints, rImgPoints, imageSize, None, None)
    rHeight, rWidth, rChannels = imgR.shape
    rNewCamMatrix, rRoi = cv2.getOptimalNewCameraMatrix(rCamMatrix, rDist, (rWidth, rHeight), 1, (rWidth, rHeight))
    
    # Stereo Vision calibration
    flags = 0
    flags |= cv2.CALIB_FIX_INTRINSIC # Fix intrinsic camera matrices so that only Rot, Trns, Emat and Fmat calculated
    
    stereoCrit = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
    
    stereoStatus, lNewCamMatrix, lDist, rNewCamMatrix, rDist, rot, trans, essMatrix, funMatrix = cv2.stereoCalibrate(objPoints, lImgPoints, rImgPoints, lNewCamMatrix, lDist, rNewCamMatrix, rDist, grayL.shape[::-1], stereoCrit, flags)
    
    # Stereo Vision Rectification
    rectifyScale = 1
    
    lRect, rRect, lProjMatrix, rProjMatrix, Q, lRoi, rRoi = cv2.stereoRectify(lNewCamMatrix, lDist, rNewCamMatrix, rDist, grayL.shape[::-1], rot, trans, rectifyScale, (0, 0))
    
    # Gets stereo maps required to undistort the left and right images
    lStereoMap = cv2.initUndistortRectifyMap(lNewCamMatrix, lDist, lRect, lProjMatrix, grayL.shape[::-1], cv2.CV_16SC2)
    rStereoMap = cv2.initUndistortRectifyMap(rNewCamMatrix, rDist, rRect, rProjMatrix, grayR.shape[::-1], cv2.CV_16SC2)
    
    # Saves the parameters needed to rectify the images
    output = cv2.FileStorage('stereoMap.xml', cv2.FILE_STORAGE_WRITE)
    output.write('stereoMapL_x', lStereoMap[0])
    output.write('stereoMapL_y', lStereoMap[1])
    output.write('stereoMapR_x', rStereoMap[0])
    output.write('stereoMapR_y', rStereoMap[1])
    output.release()
    
    

if __name__ == "__main__":
    objPoints, lImgPoints, rImgPoints, imgL, imgR, grayL, grayR = findCorners()
    calibrate(objPoints, lImgPoints, rImgPoints, imgL, imgR, grayL, grayR)