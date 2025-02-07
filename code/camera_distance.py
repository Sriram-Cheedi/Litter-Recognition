import numpy as np

def calculate_object_position(distance, angle, camera_position):
    """
    Calculate the object's position relative to the base of the robot.
    distance: The distance from the camera to the object.
    angle: The angle (in degrees) relative to the horizontal plane.
    camera_position: A 3D vector representing the camera's position relative to the robot base.
    """
    # Convert angle to radians
    angle_rad = np.radians(angle)

    # Calculate object position in camera's frame
    object_x = distance * np.cos(angle_rad)  # Horizontal distance from camera
    object_y = distance * np.sin(angle_rad)  # Vertical height from camera

    # Assuming the object is in the same Z-plane as the camera (or ignoring Z-axis for simplicity)
    object_position_camera_frame = np.array([object_x, object_y, 0])

    # Transform to the robot's base frame by adding the camera's position
    object_position_robot_frame = camera_position + object_position_camera_frame

    return object_position_robot_frame

#actual values to be added later 
camera_position = np.array([x1, x2, x3])
distance = distance 
angle = degree

object_position = calculate_object_position(distance, angle, camera_position)
print("Object Position Relative to Robot Base:", object_position)
