#Running this file by "python -m StereoVision.distInf"

import os
import sys
import cv2
import numpy as np
import tensorflow.lite as tflite
import time
import imutils
from matplotlib import pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as figCanvas
import pygame
from pygame.locals import *
from enum import Enum
import pandas as pd

# Other packages we have created
# Make sure python can tell StereoVision is one of the packages
import StereoVision.activeCalibration as activeCalibration
import StereoVision.triangulation as triangulation

import braccio_adapter
import Inverse_kinematics

import camera_distance

pygame.init()

screen_width = 1080
screen_height = 720

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Object Interface")

detected_objects = []  # Store (label, position) tuples

def display_litter_history(objects):
    y_offset = 100
    max_items = 5
    line_height = 30
    box_width = 500
    box_height = max_items * line_height + 40

    pygame.draw.rect(screen, BLACK, pygame.Rect(50, y_offset - 40, box_width, box_height))

    display_text("Litter History:", 60, y_offset - 30, WHITE)

    for i, obj in enumerate(reversed(objects[-max_items:])): 
        label, position = obj  
        rounded_position = tuple(f"{round(float(p), 1):.1f}" for p in position)
        display_text(f"{i+1}. {label} at {rounded_position}", 60, y_offset + (i * line_height), WHITE)

    pygame.display.update()



        
        
WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
RED = (255,0,0)

font = pygame.font.Font(None, 36)

d = 100


#Enum class defining servo motor IDs
class ServoMotor(Enum):
    S1 = 1
    S2 = 2
    S3 = 3
    S4 = 4
    S5 = 5
    S6 = 6

#Function to ensure servo positions stay within defined bounds
#Checks that all of the movement values are within their bounds
#If not, they are set to the closest bound
def checkInBounds(values, uBound, lBound):
    newValues = [0] * 7
    for index, item in enumerate(values):
        if (uBound[index] < item):
            newValues[index] = uBound[index]
        elif (lBound[index] > item):
            newValues[index] = lBound[index]
        else:
            newValues[index] = item
    return newValues


class BraccioDebug(braccio_adapter.BraccioAdapter):
    def __init__(self, serial_port_robot_magnet="COM4", mock=None):
        # Detect CI mode automatically
        if mock is None:
            mock = os.getenv("USE_MOCK", "true").lower() == "true"

        if mock:
            # Set default values for attributes that are normally initialized in BraccioAdapter
            self.s1 = 0
            self.s2 = 40
            self.s3 = 180
            self.s4 = 0
            self.s5 = 180
            self.s6 = 60
            self.keywords_robot = ["P"]  # Ensure this exists to prevent AttributeError
            self.s_conn_robot = None  # Mock serial connection
            self.write = lambda x: None  # Mock write function
            self.servo_movement = lambda *args, **kwargs: None  # Mock servo movement
        
        else:
            super().__init__(serial_port_robot_magnet)

        self.home_position()
        
    def read_feedback(self):
        return {
            "s1": self.s1,
            "s2": self.s2,
            "s3": self.s3,
            "s4": self.s4,
            "s5": self.s5,
            "s6": self.s6
        }

    def get_position_feedback(self):
        try:
            feedback = self.read_feedback()
            if feedback:
                print(f"Real-time position feedback: {feedback}")
        except Exception as e:
            print(f"Error reading position feedback: {e}")
    #Function to move the arm joints by specified degrees
    def move_single_joint(self, servo, degrees):
  
        try:
                 # get currect vals
            s1 = self.s1
            s2 = self.s2 
            s3 = self.s3
            s4 = self.s4 
            s5 = self.s5
            s6 = self.s6
            servoPos = [10, s1, s2, s3, s4, s5, s6]
            uBounds = [30, 180, 165, 180, 180, 180, 73]  #Holds upper and lower bounds for each servo motors movement
            lBounds = [10, 0, 15, 0, 0, 0, 10]
            
            
            if servo.value == 1:  #Adjusts servo based on input degrees
                servoPos[1] += degrees
            if servo.value == 2:
                servoPos[2] += degrees
            if servo.value == 3:
                servoPos[3] += degrees
            if servo.value == 4:
                servoPos[4] += degrees
            if servo.value == 5:
                servoPos[5] += degrees
            if servo.value == 6:
                servoPos[6] += degrees
                
            servoPos = checkInBounds(servoPos, uBounds, lBounds)
            self.servo_movement(servoPos[1], servoPos[2], servoPos[3], servoPos[4], servoPos[5], servoPos[6])
            self.s1, self.s2, self.s3, self.s4, self.s5, self.s6 = servoPos[1:] 
            self.get_position_feedback()
        except Exception as e:
            print(f"Error moving joint {servo.name}: {e}")
 
    #Moves servo upwards
    SPEED_MULTIPLIER = 1  # Adjust speed dynamically
    def up(self, servo : ServoMotor, degrees = SPEED_MULTIPLIER):
        self.move_single_joint(servo, degrees)

    #Moves servo downwards
    def down(self, servo: ServoMotor, degrees = -SPEED_MULTIPLIER):
        self.move_single_joint(servo, degrees)
        
        
    def calibrate_servos(braccio):
        print("Calibrating servos to default positions...")
        braccio.servo_movement(90, 90, 90, 90, 90, 90)  # Calibrate to default position0, 40, 180, 0, 180)
        print("Calibration complete.")



# Function to "correct" the precision error in the base servo
def jiggle(braccioDebug, baseServo):
    direction = -1
    jiggleAmount = 5
    for i in range(jiggleAmount + 1):
        offset = (jiggleAmount-i) * jiggleAmount * direction
        braccioDebug.servo_movement(baseServo + offset, braccioDebug.s2, braccioDebug.s3, braccioDebug.s4, braccioDebug.s5, braccioDebug.s6)
        direction *= -1

def display_text(text, x, y, color=WHITE,clear_area = False):
    if clear_area:
        print(x, y)
        pygame.draw.rect(screen, BLACK, pygame.Rect(x, y, 300, 40)) #clears the previous text to print the updated text
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))
    
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
    startY, startX, endY, endX = 0, 0, 0, 0
    count = 0
    label = None
    for i in range(len(scores)):
        if scores[i] > 0.75:
            count += 1
            # Gets the coordinates of the bounding boxes
            (startY, startX, endY, endX) = (int(boxes[i][0] * h), int(boxes[i][1] * w), int(boxes[i][2] * h), int(boxes[i][3] * w))
                
            # Gets the class and score associated with the detection
            label = lblMap[int(classes[i])]
            score = int(scores[i] * 100)
                
            # Draws the bounding box
            cv2.rectangle(capture, (startX, startY), (endX, endY), (0, 255, 0), 2)
            cv2.putText(capture, f"{label}: {score}%", (startX, startY - 10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            
    return ((startX + endX) / 2, (startY + endY) / 2), count, label
            
# Calculates the fps (frames per second)
def calculateFPS(captureLeft, captureRight, start, end):
    total = end - start
    fps = 1 / total
    
    cv2.putText(captureLeft, f'FPS: {int(fps)}', (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 2)
    
# Creates a Pie chart of the collected litter so far
def createPieChart():
    
    # Closes all current figures
    plt.close('all')
    
    # Read the collected litter into a dataframe format
    dataReader = pd.read_csv('Data/litters.txt', header=None, names=["Litter"])
    sums = dataReader["Litter"].value_counts()
    
    fig, ax = plt.subplots()
    fig.patch.set_facecolor('black')
    ax.axis('equal')    
    ax.set_aspect('equal', adjustable='box')

    ax.pie(sums, labels=sums.index, textprops={'color': 'white'}, radius=0.7)


    fig.tight_layout()

    
    pieArea = figCanvas(fig)
    
    # Converts the pie chart to a Pygame surface
    pieArea.draw()
    renderer = pieArea.get_renderer()
    rgbData = renderer.tostring_argb()
    canWidth, canHeight = pieArea.get_width_height()
    
    pieSurface = pygame.image.fromstring(rgbData, (canWidth, canHeight), "ARGB")
    
    # Renders the surface onto the interface
    screen.blit(pieSurface, (0, screen_height - canHeight))

    
    

# Main script for real time detection
def detect(MODEL_PATH, LABELMAP_PATH, robot=False):

    timeCounter = 0
    display_text("PICKING UP!", 780, 520, GREEN)
    pygame.display.flip()
    # input()
    display_text("PICK UP FAILED!", 780, 570, RED)
    display_text("NO OBJECTS!", 780, 620, RED)
    pygame.draw.rect(screen, BLACK, pygame.Rect(780, 520, 300, 45))
    pygame.display.flip()

    if robot:
        serial_port = input("Enter the serial port (e.g., COM3, COM4, /dev/ttyUSB0): ")
        braccioDebug = BraccioDebug(serial_port_robot_magnet=serial_port, mock = False)
    
    objects = []

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
    cameraLeft.set(3, 640)
    cameraLeft.set(4, 480)
    cameraRight = cv2.VideoCapture(2, cv2.CAP_DSHOW)
    cameraRight.set(3, 640)
    cameraRight.set(4, 480)
    
    if not cameraLeft.isOpened() or not cameraRight.isOpened():
        print("Error: a camera could not be opened")
        exit()
        
    # Stereo vision setup parameters
    frameRate = 60
    camDist = 7 # Distance between cams (cm)
    focalLength = 4 # Camera lense's focal length (mm)
    alpha = 60 # Camera fov in horizontal plane (degrees)

    # Camera position
    camera_position1 = np.array([270, -90, 165])
    camera_position2 = np.array([277, -90, 165])
    camera_position = (camera_position1 + camera_position2)/2
    camera_angle = 35

        
    # Main detection loop
    while True:

        # Draw over the previous picking up alert
        pygame.draw.rect(screen, BLACK, pygame.Rect(780, 520, 300, 45))
        pygame.display.flip()

        #  Capture and pre-process image
        ret, captureLeft = cameraLeft.read()
        ret1, captureRight = cameraRight.read()
        #capture = cv2.cvtColor(capture, cv2.COLOR_RGB2BGR)
        
        captureLeft, captureRight = activeCalibration.undistortRect(captureLeft, captureRight)

        start = time.time()
        
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
        centreLeft, leftCount, labelL = drawBoxes(captureLeft, scores, boxes, lblMap, classes)
        centreRight, rightCount, labelR = drawBoxes(captureRight, scores1, boxes1, lblMap, classes1)
        
        # Ensures both cameras detect object
        if leftCount == 0 or rightCount == 0:
            cv2.putText(captureLeft, "OBJECT NOT FOUND", (75, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            cv2.putText(captureRight, "OBJECT NOT FOUND", (75, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

            # If it has been 60 frames since an object has been found
            timeCounter += 1
            if timeCounter >= 60:
                display_text("NO OBJECTS!", 780, 620, RED)
                pygame.display.flip()
        else:
            timeCounter = 0
            pygame.draw.rect(screen, BLACK, pygame.Rect(780, 620, 300, 45))
            pygame.display.flip()

            depth = triangulation.findDepth(centreLeft, centreRight, captureLeft, captureRight, camDist, focalLength, alpha)

           
            #print(coords)
 
            cv2.putText(captureLeft, "Distance: " + str(round(depth, 1)), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 2)
            cv2.putText(captureRight, "Distance: " + str(round(depth, 1)), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 2)

            if robot:
                display_text("PICKING UP!", 780, 520, GREEN)
                pygame.display.flip()
                depth *= 10

                # Calculate angles to object from the normal to the camera and 
                midpointx = screen_width / 2
                midpointy = screen_height / 2

                theta1 = -camera_angle + ((midpointy - centreLeft[1]) * (alpha / width))
                phi1 = (centreLeft[0] - midpointx) * (alpha / width)

                theta2 = -camera_angle + ((midpointy - centreRight[1]) * (alpha / width))
                phi2 = (centreRight[0] - midpointx) * (alpha / width)

                # Average the two angles between the cameras
                theta = (theta1 + theta2) / 2
                phi = (phi1 + phi2) / 2
                print("Theta: ", theta)
                print("Phi: ", phi)

                # Calculating coordinates based on depth and angles from the cameras normal vectors
                z = depth * np.sin(np.deg2rad(theta))
                x = depth * np.sin(np.deg2rad(phi))
                y = np.sqrt(depth**2 - x**2 - z**2)
                
                
                # Translate the vector to the position of the robot
                vector = [x,y,z] + camera_position
                
                
                # vector[0] = int(input("Enter x:"))
                # vector[1] = int(input("Enter y:"))
                # vector[2] = int(input("Enter z:"))
                print([x, y, z])
                print(camera_position)
                print(vector)

                objects.append((labelL, vector))
                display_litter_history(objects)
                print(objects)
                
                with open('Data/litters.txt', 'a') as file:
                    file.write(labelL + "\n")

                items = len(objects)

                # Draw over the previous pickup failed alert
                pygame.draw.rect(screen, BLACK, pygame.Rect(780, 570, 300, 45))
                pygame.display.flip()

                # If the last two items detected are the same, turn on the pickup failed alert
                if items > 1 and objects[items - 1][0] == objects[items - 2][0]:
                    display_text("PICK UP FAILED!", 780, 570, RED)
                    pygame.display.flip()


                # Stand up straight
                braccioDebug.servo_movement(90, 90, 90, 90, 90, 10)

                # Jiggle the base
                baseServo = 90 - Inverse_kinematics.move(vector)[0]
                jiggle(braccioDebug, baseServo)
                

                # Move thew arm down with class open
                braccioDebug.servo_movement(braccioDebug.s1, 90 - Inverse_kinematics.move(vector)[1], 90 - Inverse_kinematics.move(vector)[2], 90 - Inverse_kinematics.move(vector)[3], braccioDebug.s5, braccioDebug.s6)
                
                # Shut the claw
                braccioDebug.servo_movement(braccioDebug.s1, braccioDebug.s2, braccioDebug.s3, braccioDebug.s4, braccioDebug.s5, 73)
                
                # Stand up straight with claw shut
                braccioDebug.servo_movement(90, 90, 90, 90, 90, braccioDebug.s6)
            
                vector = Inverse_kinematics.move(vector)[4]

        # Calculates and labels depth from object
        # depthCalculation(centreLeft, centreRight)
        
        end = time.time()
        calculateFPS(captureLeft, captureRight, start, end)
        
        
        # Display image with detection 
        cv2.imshow("Litter Detection Left", captureLeft)
        cv2.imshow("Litter Detection Right", captureRight)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cameraLeft.release()
                cameraRight.release()
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    cameraLeft.release()
                    cameraRight.release()
                    pygame.quit()
                    sys.exit()
       
        
        createPieChart()
        pygame.display.flip()
        
        # Get vector pos

       

        # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # End capture cleanly
    cameraLeft.release()
    cameraRight.release()
    cv2.destroyAllWindows()
    return
    



if __name__ == "__main__":
    MODEL_PATH = "./Model/model.tflite"
    LABELMAP_PATH = "./Model/labels.txt"
    detect(MODEL_PATH, LABELMAP_PATH, True)
