import cv2
import numpy as np
import tensorflow.lite as tflite

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
    camera = cv2.VideoCapture(0)
    
    if not camera.isOpened():
        print("Error: camera could not be opened")
        exit()
        
    # Main detection loop
    while True:
        #  Capture and pre-process image
        ret, capture = camera.read()
        #capture = cv2.cvtColor(capture, cv2.COLOR_RGB2BGR)
        img = cv2.resize(capture, (width, height))
        img = img.astype(np.uint8) 
        img = np.expand_dims(img, 0)
        
        # Prepare interpreter for detection
        interpreter.set_tensor(inpTensors[0]['index'], img)
        interpreter.invoke()
        
        # Gets detection results
        boxes = interpreter.get_tensor(outTensors[0]['index'])[0]
        classes = interpreter.get_tensor(outTensors[1]['index'])[0]
        scores = interpreter.get_tensor(outTensors[2]['index'])[0]

        # Iterates through the detections
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
        
        # Display image with detection 
        cv2.imshow("Litter Detection", capture)
        
        # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # End capture cleanly
    camera.release()
    cv2.destroyAllWindows()
    return
    



if __name__ == "__main__":
    MODEL_PATH = "Model/model.tflite"
    LABELMAP_PATH = "Model/labels.txt"
    detect(MODEL_PATH, LABELMAP_PATH)
    