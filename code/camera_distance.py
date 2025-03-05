"""
This function calculates the position of the object relative to the robot base using the depth of the object from the camera and the angle relative to the horizontal plane.

Steps:
Change the angle from degrees to radians.
Calculate the position of the object in the camera coordinate frame using trigonometry.
Transform the position from the camera frame to the robot base frame by adding the known position of the camera.

Inputs:
depth: The depth from the camera to the object.
angle: Object angle relative to the horizontal plane (in degrees).
camera_position: A NumPy array that defines the position of the camera relative to the robot base.

Output:
A NumPy array providing the position of the object relative to the robot base.
"""

import numpy as np
import StereoVision.distInf



def calculate_object_position(depth, angle, camera_position):
    """
    Calculate the object's position relative to the base of the robot.
    depth: The depth from the camera to the object.
    angle: The angle (in degrees) relative to the horizontal plane.
    camera_position: A 3D vector representing the camera's position relative to the robot base.
    """
    # Convert angle to radians
    angle_rad = np.radians(angle)

    # Calculate object position in camera's frame
    object_x = depth * np.cos(angle_rad)  # Horizontal depth from camera
    object_y = depth * np.sin(angle_rad)  # Vertical height from camera

    # Assuming the object is in the same Z-plane as the camera (or ignoring Z-axis for simplicity)
    object_position_camera_frame = np.array([object_x, object_y, 0])

    # Transform to the robot's base frame by adding the camera's position
    object_position_robot_frame = camera_position + object_position_camera_frame

    return object_position_robot_frame

#actual values to be added later 
MODEL_PATH = "model.tflite"
LABELMAP_PATH = "label_map.txt"
depth = StereoVision.distInf.detect(MODEL_PATH, LABELMAP_PATH)

angle = 95

camera_position1 = np.array([0, 150, 50])
camera_position2 = np.array([0, 150, 50])
camera_position = (camera_position1 + camera_position2)/2


object_position = calculate_object_position(depth, angle, camera_position)
print("Object Position Relative to Robot Base:", object_position)
