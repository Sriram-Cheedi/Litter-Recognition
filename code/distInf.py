import sys
import cv2
import numpy as np
import tensorflow.lite as tflite
import time
#import imutils
from matplotlib import pyplot as plt

# Other packages we have created
#import triangulation as tri
#import calibration

# Loads the label map into a list
def loadLabelMap(LABELMAP_PATH):
    labelMap = {}
    
    with open(LABELMAP_PATH, "r") as lmap:
        for line in lmap:
            # Split line at the space
            parts = line.strip().split(" ", 1)
            if len(parts) == 2:
                index, lbl = parts
                labelMap[int(index)] = lbl
    return labelMap

# Pre process the frame before inference
def preProcess(frame, width, height):
    img = cv2.resize(frame, (width, height))
    img = img.astype(np.uint8) 
    img = np.expand_dims(img, 0)
    return img

# Draws the bounding boxes onto the image
def drawBoxes(capture, scores, boxes, lblMap, classes):
    h, w, _ = capture.shape
    for i in range(len(scores)):
        if scores[i] > 0.5:
            # Gets the coordinates of the bounding boxes
            (startY, startX, endY, endX) = (int(boxes[i][0] * h), int(boxes[i][1] * w), int(boxes[i][2] * h), int(boxes[i][3] * w))
                
            # Gets the class and score associated with the detection
            label = lblMap[int(classes[i])]
            score = int(scores[i] * 100)
                
            # Draws the bounding box
            cv2.rectangle(capture, (startX, startY), (endX, endY), (0, 255, 0), 2)
            cv2.putText(capture, f"{label}: {score}%", (startX, startY - 10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        
    

# Main script for real time detection
def detect(MODEL_PATH, LABELMAP_PATH):
    # Set up the interpreter for inference
    interpreter = tflite.Interpreter(MODEL_PATH)
    interpreter.allocate_tensors()
    
    # Get the input shape and tensors, and the output tensors
    inpTensors = interpreter.get_input_details()
    outTensors = interpreter.get_output_details()
    inpShape = inpTensors[0]['shape']
    height, width = inpShape[1], inpShape[2]
    
    lblMap = loadLabelMap(LABELMAP_PATH)
    
    # Set up the camera
    cameraLeft = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cameraRight = cv2.VideoCapture(1, cv2.CAP_DSHOW)
    
    if not cameraLeft.isOpened() or not cameraRight.isOpened():
        print("Error: a camera could not be opened")
        exit()
        
    # Stereo vision setup parameters
   # frameRate = 120
   # camDist = 14 # Distance between cams (cm)
   # focalLength = 12 # Camera lense's focal length (mm)
   # alpha = 95 # Camera fov in horizontal plane (degrees)
        
    # Main detection loop
    while True:
        #  Capture and pre-process image
        ret, captureLeft = cameraLeft.read()
        ret1, captureRight = cameraRight.read()
        #capture = cv2.cvtColor(capture, cv2.COLOR_RGB2BGR)
        img = preProcess(captureLeft, width, height)
        img1 = preProcess(captureRight, width, height)
        
        # Prepare interpreter for first detection
        interpreter.set_tensor(inpTensors[0]['index'], img)
        interpreter.invoke()
        
        # Gets detection results
        boxes = interpreter.get_tensor(outTensors[0]['index'])[0]
        classes = interpreter.get_tensor(outTensors[1]['index'])[0]
        scores = interpreter.get_tensor(outTensors[2]['index'])[0]
        
        # Prepare interpreter for second detection
        interpreter.set_tensor(inpTensors[0]['index'], img1)
        interpreter.invoke()
        
        # Gets detection results
        boxes1 = interpreter.get_tensor(outTensors[0]['index'])[0]
        classes1 = interpreter.get_tensor(outTensors[1]['index'])[0]
        scores1 = interpreter.get_tensor(outTensors[2]['index'])[0]

        # Iterates through the detections
        drawBoxes(captureLeft, scores, boxes, lblMap, classes)
        drawBoxes(captureRight, scores1, boxes1, lblMap, classes1)
        
        # Display image with detection 
        cv2.imshow("Litter Detection Left", captureLeft)
        cv2.imshow("Litter Detection Right", captureRight)
        
        # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # End capture cleanly
    cameraLeft.release()
    cameraRight.release()
    cv2.destroyAllWindows()
    return
    



if __name__ == "__main__":
    MODEL_PATH = "model.tflite"
    LABELMAP_PATH = "label_map.txt"
    detect(MODEL_PATH, LABELMAP_PATH)
    