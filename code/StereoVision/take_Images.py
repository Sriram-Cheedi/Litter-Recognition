# Code to take the images used to calibrate the dual camera set up
# These images will likely be of a chessboard
# Need to take around 3 to 5 images which can then be used in calibration.py

import cv2

# Used to take images intended for calibration
def takeImages(capture1, capture2):
    count = 0
    
    while capture1.isOpened():
        # Takes images from video feed
        _, image1 = capture1.read()
        _, image2 = capture2.read()
        
        key = cv2.waitKey(5)
        
        if key == ord('q'):
            break
        elif key == ord('s'):
            cv2.imwrite('calibration_images/left/left' + str(count) + '.png', image1)
            cv2.imwrite('calibration_images/right/right' + str(count) + '.png', image2)
            count += 1
            
        cv2.imshow('Left Image', image1)
        cv2.imshow('Right Image', image2)
        
    


if __name__ == "__main__":
    stream1 = cv2.VideoCapture(0)
    stream1.set(3, 640)
    stream1.set(4, 480)
    stream2 = cv2.VideoCapture(1)
    stream2.set(3, 640)
    stream2.set(4, 480)
    
    takeImages(stream1, stream2)