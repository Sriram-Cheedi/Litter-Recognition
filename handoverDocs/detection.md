# Litter Detection and Depth Calculation Code Guide

## You will need:
- Two cameras of the exact same specification,
- A computer with enough processing power to run the detection,
- An object displaying an 8 by 6 (measured by interior vertices) chessboard pattern,
- The code loaded up with the model onto the computer.

## Step 1: Taking The Images for Calibration
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

## Step 2: Calibrate your Cameras
Once the images have been taken, they should be saved into the local files 'left' and 'right' like above. Now run:

```console
python calibration.py
```

This should show a series of frames with openCV having detected the chessboard corners in the images you took earlier. These corner locations are used to create a local file 'stereoMap.xml' needed to rectify the images which will be taken while running the depth and image detection. This file can be reused whenever now that you have calibrated the two cameras.

## Step 3: Run the Detection Script
Now that you have completed the preliminary tasks, all you need to do is run:

```console
python distInf.py
```

This script runs real time inference on the camera feeds using the TFlite TACO-trained model powering our project. If both frames detect an object, the distance of this object should be calculated and displayed with the help of the rectification parameters you calculated via the calibration script. Now that the script is hopefully running as intended, you can act like Timmy below:

![Shaun The Sheep](https://media0.giphy.com/media/tIeCLkB8geYtW/giphy.gif?cid=47028fa8jgwxw5pmayj1hkegw38jlet0446le5qcmbnzcdy7&ep=v1_gifs&rid=giphy.gif&ct=g)
