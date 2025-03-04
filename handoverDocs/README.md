# Litter Recognition Handover Documentation
## Contents:
- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Robot System Guide](#robot-system-guide)
- [Litter Detection and Depth Calculation Code Guide](#litter-detection-and-depth-calculation-code-guide)
- [Further Documentation](#further-documentation)

## Introduction:

## Project Structure:

## Robot System Guide

#### 1. braccio_adapter.py 
**Purpose:** 
- Handles serial communication with the Braccio robotic arm via an Arduino.
- Sends commands to move servos to specific angles.

#### 2. Inverse_kinematics.py
**Purpose:**
- Calculates servo angles using inverse kinematics.
- Ensures the arm moves precisely to the target position.

#### 3. Interface.py
- Main python file which integrates braccio_adapter for serial communication and Inverse_kinematics for movement control.
- Provides a pygame based UI for real time servo movement visualisation and to control the robotic arm using keyboard input.

### System Setup:
**You will need:**
- Braccio Robotic Arm
- Arduino UNO
- Arduino IDE
- Computer with Python Installed
- Install dependencies using:

   ```console
   pip install pygame numpy pyserial
   ```


### Instructions for Controlling the Arm:

**To control the arm for debugging:**

| Keys |           Functions            | 
|------|--------------------------------|
| W/S  | open/close the claw            |
| A/D  | rotating (twisting) the wrist  |
| I/K  | move arm forward/backward      |
| J/L  | move arm left/right            |
| U/O  | move arm up/down               |


**To control the from specific coordinates:**

- Press 'M' to select coordinates screen 
- Enter x,y,z coordinates when prompted (in millimetres,(0,0,0) is at the middle of the shoulder joint).

The arm will now perform the pick up procedure at the given position.


### Step 1: Connecting the Braccio arm

Connect the braccio arm and your computer to the arduino. This should initialise the arduino script and move arm to the safety position.

### Step 2: Identifying the Arduino Port

Open the Arduino IDE and check and remember the arduino port (e.g., COM3 or COM4 or /dev/ttyUSB0 etc.) under Arduino Uno on top-left side of your
screen.

### Step 3: Run the Interface Script

Now you have completed all the setup, run interface.py using:

```console
python interface.py
```

Now it will ask you to enter the port which was in you Arduino IDE. After entering the braccio arm will start to run and a pygame interface will
be opened. This displays servo angles of different joints of the robot and gives last key pressed along with history of last 5 keys pressed. You
can now move the robot by following the instructions given above.

### Troubleshooting:
### Common Issues and Fixes

| Issue                                          | Possible Fix                                                        |
|------------------------------------------------|---------------------------------------------------------------------|
| **Braccio didn't move to the safety position**     | Check Arduino connections.                                          |
| **Interface.py is not running**                | Ensure all dependencies (`pygame`, `numpy`, `pyserial`) are installed.  |
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

Pictures must include the chessboard at different orientations and angles in every frame. For example, the first picture could just be the chessboard held to the middle of the frame, while another could have the chessboaard held to the corner of one of the cameras at an angle. Examples can be found in:

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
