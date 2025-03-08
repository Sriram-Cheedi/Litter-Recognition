# Litter Recognition Handover Documentation
## Contents:
- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Architecture Diagram](#architecture-diagram)
- [Robot System Guide](#robot-system-guide)
- [Litter Detection and Depth Calculation Code Guide](#litter-detection-and-depth-calculation-code-guide)
- [Further Documentation](#further-documentation)

## Introduction:
The purpose of this document is to serve as a guide for new developers to continue our work on the project. It will cover the existing code infrastructure and the structure of our repository.

## Project Structure:
This section covers the different directories of our repository:

```
.
├── .github/             # Templates and workflows
├── .gitignore           # Other files
├── LICENSE              ...
├── README.md            ...
├── Research/            # Research files
├── code/                # All project code
├── docs/                # Project documentation
└── handoverDocs/        # Handover documentation (You are here)
```

### Links:
These links allow you to navigate to explanations of different areas of the repository:
- [/.github](#github)
- [/Research](#research)
- [/code](#code)
- [/docs](#docs)
- [/handoverDocs](#handoverDocs)

### /.github:
The structure within the ```/.github``` directory can be found below:

```
.
├── ISSUE_TEMPLATE                 # Templates for GitHub issues
│   └── ISSUE_FORM.yml             # Issue template
├── labeler.yml                    # Labeller action config file
├── pull_request-template.md       # Pull request template
└── workflows                      # Automated GitHub workflows
    ├── handoverDocs.yml           # Action to upload the handover documents to GitHub pages
    ├── labeler.yml                # Action to automatically label pull requests
    ├── pyTest.yml                 # Action to run continuous integration tests on our code
    ├── pylint.yml                 # Action to lint our code
    └── zipDeployment.yml          # Action to deploy our code by releasing it as a zip
```

### /Research:
The structure within the ```/Research``` directory can be found below:

```
.
├── Arduino/                                 # Code to test our Arduino Braccio arm
├── BraccioCode/                             # Basic robot code to test the robot
├── CNN-Examples/                            # Example CNN training code
├── Image-Detection-Proof-of-Concept/        # Documentation of our process of finding a detection model
├── Inference-Set-Up.md                      # Documentation of the model conversion process
├── Litter-Datasets.md                       # Research into what litter datasets to use for the project
├── PiCam-Setup.md                           # Guides to set up PiCameras on a Raspberry Pi
├── RESEARCH.md                              # Placeholder md file
└── TensorFlow/                              # Research into how to use and install TensorFlow
```

### /code:
The structure within the ```/code``` directory can be found below:

```
.
├── Inverse_kinematics.py                    # Converts a distance to angles for the joints to move
├── Model                                    # Model and labels
│   ├── annotations.json                     # Bounding box annotations
│   ├── labels.txt                           # Label map for inference
│   └── model.tflite                         # TFLite inference model
├── README.md                                # Calculations used for inverse_kinematics.py
├── StereoVision                             # StereoVision depth estimation code
│   ├── README.md                             
│   ├── __init__.py                          
│   ├── activeCalibration.py                 # Undistorts captured video frames
│   ├── calibration.py                       # Calibrates two cameras by using a checkerboard
│   ├── calibration_images                   # Images captured by take_images.py
│   ├── distInf.py                           # Real time inference with depth estimation
│   ├── stereoMap.xml                        # Parameters used to undistort video frames
│   ├── take_Images.py                       # Takes calibration images 
│   └── triangulation.py                     # Calculates object depth from cameras
├── archived                                 # Outdated or redundant code
│   ├── error_testing.py                     # Debug code for robot arm
│   └── inference.py                         # Original real-time inference script using the PiCamera2 library
├── arduino-script                           # Code to move the arm
│   └── arduino-script.ino                   # Moves robot arm using specified input
├── braccio_adapter.py                       # Communicate with the arm through Python
├── camera_distance.py                       # Calculates distance vector using estimated depth
├── graphReconstructer.py                    # Reconstructs frozen graph from our incomplete inference model
├── inferenceCV.py                           # Real time inference using openCV
├── interface.py                             # Interface allowing interaction with the arm
├── labelMapCreator.py                       # Creates label map from annotations.json
├── requirements.txt                         # Project dependencies
└── tests/                                   # Unit tests
```

###  /docs:
The structure within the ```/docs``` directory can be found below:

```
.
├── AI_TOOLS.md             # Documentation on what AI tools we have used during the project
├── ARDUCAM.md              # Documentation of how to set up the multi cam adapter on the Raspberry Pi
├── Architecture-Diagrams/  # Architecture diagrams of the project
├── Client-Meeting-Notes/   # Bi-weekly client meetings
├── ETHICS.md               # Documentation of our chosen ethics route
├── Images-And-Videos/      # Images and videos of the project
├── Milestone-Slides/       # Slides for our MVP, Beta, and Final releases
├── Pi/                     # Documentation for our Raspberry Pi
├── Project-Proposal/       # Proposal of the project
├── Research-Forms/         # Forms for user testing
├── Robot-Documentation/    # Documentation of in-person hardware work
└── User-Testing/           # Questionnaire for user testing
```

### /handoverDocs:
The structure within the ```/handoverDocs``` directory can be found below:

```
.
└── README.md   # Handover documentation
```

## Architecture Diagram:
![image](https://github.com/user-attachments/assets/22d654af-39bc-4fdd-8003-1cc4eb89514f)

## Robot System Guide

#### 1. braccio_adapter.py 
**Purpose:** 
- Handles serial communication with the Braccio robotic arm via an Arduino.
- Sends commands to move servos to specific angles.

#### 2. Inverse_kinematics.py
**Purpose:**
- Calculates servo angles using inverse kinematics.
- Ensures the arm moves precisely to the target position.

#### 3. interface.py
- Main python file which integrates braccio_adapter for serial communication and Inverse_kinematics for movement control.
- It offers three distinct modes: Camera mode, Manual mode, and a combined Camera & Manual mode, each incorporating sorting techniques.
- Provides a pygame based UI for real time servo movement visualisation and to control the robotic arm using keyboard input.
- Manual mode: Arm can be controlled using inverse_kinematics manually and also by entering the position of the litter.
- Camera & Manual mode: This mode will be a autonomous system     where the litter detected by the camera will be picked and placed into a bin by the
arm.
- Camera mode: This mode will only run the camera to detect the litter.


### System Setup:
**Prerequisites**
- Braccio Robotic Arm
- Arduino UNO
- Arduino IDE
- Computer with Python installed
**Installation**
Ensure you have the required dependencies installed:

   ```console
   pip install pygame numpy pyserial
   ```


### Instructions for Controlling the Arm:

**To control the arm for debugging:**

| Keys |           Functions            | 
|------|--------------------------------|
| W/S  | Open/close the claw            |
| A/D  | Rotating (twisting) the wrist  |
| I/K  | Move arm forward/backward      |
| J/L  | Move arm left/right            |
| U/O  | Move arm up/down               |


**To control the arm from specific coordinates:**

- Press 'M' to select coordinates screen 
- Enter x,y,z coordinates when prompted (in millimetres,(0,0,0) is at the middle of the shoulder joint).
-The arm will now perform the pick up procedure at the given position.

### Running the Interface:
#### Step 1: Connecting the Braccio arm

Start by connecting the Braccio robotic arm and your computer to the Arduino. Once everything is securely in place, the Arduino script will automatically launch, allowing the system to
detect the Braccio arm and get it ready for use. During initialization, the script will guide the arm into its predefined safety position, ensuring it starts from a stable and secure
state before performing any tasks or movements.

>[!IMPORTANT]
> Make sure the Braccio robotic arm and your computer are securely connected to the Arduino board before starting any operations. A loose connection could cause communication issues or
> unexpected movements.

#### Step 2: Identifying the Arduino Port

Open the Arduino IDE and go to the top-left corner of the screen. Under the Tools menu, you'll find the Board and Port options. Click on Port, and check the list of available ports. Look
for the one linked to your Arduino Uno — on Windows, it’s usually labeled **COM3** or **COM4**, while on Linux or macOS, it may appear as **/dev/ttyUSB0 or /dev/ttyACM0**, depending on
your system setup.
> [!NOTE]
> Make sure to remember this port name, as you'll need it later when uploading code or setting up a communication link between your computer and the Braccio robotic arm.

> [!TIP]
> If multiple ports are listed and you're unsure which one belongs to the Arduino, try disconnecting and reconnecting the board. The correct port will be the one that disappears and then
> reappears in the list.


Once you've identified the correct port, make a note of it or write it down for easy reference. You'll need it for the next steps in setting up and controlling the robotic arm.

#### Step 3: Run the Interface Script

Now you have completed all the setup, run **interface.py** using:

```console
python interface.py
```
Next, it will ask you to select one of the three modes (Camera mode, Manual mode and Camera & Manual mode), after selecting your preferred mode, you'll be
prompted to enter the port name that was previously displayed in the Arduino IDE. Make sure to enter it correctly, as this is crucial for establishing a proper
connection between your computer and the Braccio robotic arm. Once you enter the correct port, the Braccio robotic arm will begin its startup routine. At the
same time, a Pygame based interface will automatically open on your screen. This interface serves as an intuitive control panel, allowing you to operate the
robotic arm using key presses. It provides real-time feedback on the current state of the arm, displaying servo angles for different joints and helping you
monitor movement accuracy also shows the last key pressed, and keeps a history of the last five key presses. You are now ready to control the robotic arm. Follow
the provided instructions carefully to execute precise movements. 

> [!WARNING]
> Avoid lifting objects that exceed the robotic arm's weight capacity. Overloading can strain the servos, potentially causing permanent damage and reducing the arm’s overall lifespan.

> [!CAUTION]
> Do not manually move the robotic arm while it is powered on. Forcing it by hand can strip the gears and damage the servo motors, leading to performance issues or permanent malfunction.
> Always use the designated controls to operate the arm safely.

### Troubleshooting:
### Common Issues and Fixes

| Issue                                          | Possible Fix                                                        |
|------------------------------------------------|---------------------------------------------------------------------|
| **Braccio didn't move to the safety position**     | Check Arduino connections.                                          |
| **interface.py is not running**                | Ensure all dependencies (`pygame`, `numpy`, `pyserial`) are installed.  |
| **Arduino port not found**                     | Enter the correct port given in Arduino IDE.                        |




## Litter Detection and Depth Calculation Code Guide

### You will need:
- Two cameras of the exact same specification,
- A computer with enough processing power to run the detection,
- An object displaying an 8 by 6 (measured by interior vertices) chessboard pattern,
- The code loaded up with the model onto the computer.

### Step 1: Taking The Images for Calibration
With the cameras connected to your device, first run:

```console
python take_Images.py
```

This should then display the two camera feeds on your screen. From here you will need to take a minimum of 5 photos by pressing the 's' key.

> [!IMPORTANT]
> Pictures must include the chessboard at different orientations and angles in every frame. For example, the first picture could just be the chessboard held to the middle of the frame, while another could have the chessboaard held to the corner of one of the cameras at an angle. Examples can be found in:

```bash
2024-LitterRecognition1
├── code/          
│   ├── StereoVision/
|   |   ├── calibration_images
|   |   |   ├── left  # HERE
|   |   |   ├── right # HERE
```

### Step 2: Calibrate your Cameras
Once the images have been taken, they should be saved into the local files 'left' and 'right' like above. Now run:

```console
python calibration.py
```

This should show a series of frames with openCV having detected the chessboard corners in the images you took earlier. These corner locations are used to create a local file 'stereoMap.xml' needed to rectify the images which will be taken while running the depth and image detection. This file can be reused whenever now that you have calibrated the two cameras.

### Step 3: Run the Detection Script
Now that you have completed the preliminary tasks, all you need to do is run:

```console
python distInf.py
```

This script runs real time inference on the camera feeds using the TFlite TACO-trained model powering our project. If both frames detect an object, the distance of this object should be calculated and displayed with the help of the rectification parameters you calculated via the calibration script. Now that the script is hopefully running as intended, you can act like Timmy below:

![Shaun The Sheep](https://media0.giphy.com/media/tIeCLkB8geYtW/giphy.gif?cid=47028fa8jgwxw5pmayj1hkegw38jlet0446le5qcmbnzcdy7&ep=v1_gifs&rid=giphy.gif&ct=g)

## Further Documentation

| Resource | Link | 
| ---------------- | --------------- |
| Arduino IDE Documentation | [here](https://docs.arduino.cc/) |
| Arduino Braccio Documentation | [here](https://docs.arduino.cc/retired/getting-started-guides/Braccio/) |
| OpenCV Documentation | [here](https://docs.opencv.org/4.x/index.html) |
| TensorFlow Lite Documentation | [here](https://www.tensorflow.org/api_docs/python/tf/lite) |
| TensorFlow Model Source | [here](https://www.kaggle.com/code/bouweceunen/garbage-detection-with-tensorflow/notebook) |
