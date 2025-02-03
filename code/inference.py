# Dependency Requirements:
# Dependencies from Colab (tf, keras, protobuf etc)
# Distro
# sudo apt-get dist-upgrade
# ------------------------------------
# Tensorflow
# sudo apt-get install libatlas-base-dev (needed for tf)
# pip3 install tensorflow (version from colab)
# sudo pip3 install pillow lxml jupyter matplotlib cython
# sudo apt-get install python-tk
# ------------------------------------
# OpenCV
# sudo apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev
# sudo apt-get install libavcodec-dev libavformat-dev libwscale-dev lib4l-dev
# sudo apt-get install libxvidcore-dev libx264-dev
# sudo apt-get install qt4-dev-tools
# sudo apt-get libatlas-base-dev
# pip3 install opencv-python


# Unsure
# They install the tensorflow models github
# and point the python path at it
# Then they install a .tar.gz model from the model library and get the .pb files from there

# Import packages and utilities
import os
import cv2
import tensorflow as tf
from picamera2 import Picamera2
import numpy as np

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

# Calculates and draws the bounding box
def boundingBox(box, image, label):
    (startY, startX, endY, endX) = (int(box[0] * 480), int(box[1] * 640), int(box[2] * 480), int(box[3] * 640))
    
    # Draw the bounding box
    cv2.rectangle(image, (startX, startY), (endX, endY), (0, 255, 0), 2)
    cv2.putText(image, label, (startX, startY - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    return image

# Main detection function of the script
def detect(MODEL_PATH, LABELMAP_PATH):
    # Set up the interpreter for inference
    interpreter = tf.lite.Interpreter(model_path=MODEL_PATH)
    interpreter.allocate_tensors()
    
    # Get the input shape and tensors, and the output tensors
    inpTensors = interpreter.get_input_details()
    inpShape = inpTensors[0]['shape']
    
    outTensors = interpreter.get_output_details()
    
    # Loads the label map into a list
    lblMap = loadLabelMap(LABELMAP_PATH)
    
    # Set up the camera 
    camera = Picamera2()
    config = camera.create_preview_configuration(main = {"size": (640, 480)})
    camera.configure(config)
    
    # Start the camera
    camera.start()
    
    # Continuous video stream
    while True:
        # Capture and pre-process image
        frame = camera.capture_array()
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        input = cv2.resize(frame, (300, 300))
        input = np.expand_dims(input, 0)
        
        # Prepare interpreter for detection
        interpreter.set_tensor(inpTensors[0]['index'], input)
        interpreter.invoke()
        
        # Gets detection results
        boxes = interpreter.get_tensor(outTensors[0]['index'])[0]
        classes = interpreter.get_tensor(outTensors[1]['index'])[0]
        scores = interpreter.get_tensor(outTensors[2]['index'])[0]
        
        # Iterates through the detections
        for detection in range(len(scores)):
            if scores[detection] > 0.5:
                box = boxes[detection]
                label = lblMap[int(classes[detection])]
                input = boundingBox(box, input, label)
           
        output = input.squeeze()
        cv2.imshow("Litter Detected", output)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    # Ending cleanly
    cv2.destroyAllWindows()
    camera.stop_preview()
    return


# Entry point of the program
if __name__ == "__main__":
    MODEL = "/2024-LitterRecognition1/code/Model/model.tflite"
    LABEL_MAP = "/2024-LitterRecognition1/code/Model/labels.txt"
    detect(MODEL, LABEL_MAP)
