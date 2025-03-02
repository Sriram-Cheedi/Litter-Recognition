# Robot System Guide

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

## System Setup
**You will need:**
- Braccio Robotic Arm
- Arduino UNO
- Arduino IDE
- Computer with Python Installed
- Install dependencies using:

   ```console
   pip install pygame numpy pyserial
   ```


## Instructions for Controlling the Arm

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

## Troubleshooting
### Common Issues and Fixes

| Issue                                          | Possible Fix                                                        |
|------------------------------------------------|---------------------------------------------------------------------|
| **Braccio didn't move to the safety position**     | Check Arduino connections.                                          |
| **Interface.py is not running**                | Ensure all dependencies (`pygame`, `numpy`, `pyserial`) are installed.  |
| **Arduino port not found**                     | Enter the correct port given in Arduino IDE.                        |



