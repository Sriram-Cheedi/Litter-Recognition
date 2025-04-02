import time
import pygame
import sys
import braccio_adapter
import Inverse_kinematics
from enum import Enum
import numpy as np
import os

import time

import StereoVision.distInf as distInf

# Initial vector position and distance
vector = np.array([0, 150, 0])
d = 100


# Enum class defining servo motor IDs
class ServoMotor(Enum):
    S1 = 1
    S2 = 2
    S3 = 3
    S4 = 4
    S5 = 5
    S6 = 6


# Function to ensure servo positions stay within defined bounds
# Checks that all of the movement values are within their bounds
# If not, they are set to the closest bound
def checkInBounds(values, uBound, lBound):
    newValues = [0] * 7
    for index, item in enumerate(values):
        if uBound[index] < item:
            newValues[index] = uBound[index]
        elif lBound[index] > item:
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
            "s6": self.s6,
        }

    def get_position_feedback(self):
        try:
            feedback = self.read_feedback()
            if feedback:
                print(f"Real-time position feedback: {feedback}")
        except Exception as e:
            print(f"Error reading position feedback: {e}")

    # Function to move the arm joints by specified degrees
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
            uBounds = [30,180,165,180,180,180,73]  # Holds upper and lower bounds for each servo motors movement
            lBounds = [10, 0, 15, 0, 0, 0, 10]

            if servo.value == 1:  # Adjusts servo based on input degrees
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
            self.servo_movement(
                servoPos[1],
                servoPos[2],
                servoPos[3],
                servoPos[4],
                servoPos[5],
                servoPos[6],
            )
            self.s1, self.s2, self.s3, self.s4, self.s5, self.s6 = servoPos[1:]
            # self.get_position_feedback()
        except Exception as e:
            print(f"Error moving joint {servo.name}: {e}")

    # Moves servo upwards
    SPEED_MULTIPLIER = 1  # Adjust speed dynamically

    def up(self, servo: ServoMotor, degrees=SPEED_MULTIPLIER):
        self.move_single_joint(servo, degrees)

    # Moves servo downwards
    def down(self, servo: ServoMotor, degrees=-SPEED_MULTIPLIER):
        self.move_single_joint(servo, degrees)

    def calibrate_servos(braccio):
        print("Calibrating servos to default positions...")
        braccio.servo_movement(
            90, 90, 90, 90, 90, 90
        )  # Calibrate to default position (0, 40, 180, 0, 180)
        print("Calibration complete.")


# Function to "correct" the precision error in the base servo
def jiggle(braccioDebug, baseServo):
    direction = -1
    jiggleAmount = 5
    for i in range(jiggleAmount + 1):
        offset = (jiggleAmount - i) * jiggleAmount * direction
        braccioDebug.servo_movement(
            baseServo + offset,
            braccioDebug.s2,
            braccioDebug.s3,
            braccioDebug.s4,
            braccioDebug.s5,
            braccioDebug.s6,
        )
        direction *= -1


def is_safe_move(braccio, servo, degrees):
    new_pos = braccio.__dict__[f"s{servo.value}"] + degrees
    return 0 <= new_pos <= 180


def handle_key_press(braccio, key, vector):
    if key == pygame.K_a and is_safe_move(braccio, ServoMotor.S5, 5):
        braccio.up(ServoMotor.S5)
        vector = Inverse_kinematics.move(vector)[4]

    elif key == pygame.K_s:
        braccio.up(ServoMotor.S6)
        vector = Inverse_kinematics.move(vector)[4]

    elif key == pygame.K_w:
        braccio.down(ServoMotor.S6)
        vector = Inverse_kinematics.move(vector)[4]

    elif key == pygame.K_d:
        braccio.down(ServoMotor.S5)
        vector = Inverse_kinematics.move(vector)[4]

    elif key == pygame.K_i:
        vector[1] += 10
        angles = Inverse_kinematics.move(vector)
        braccio.servo_movement(
            90 - angles[0],
            90 - angles[1],
            90 - angles[2],
            90 - angles[3],
            braccio.s5,
            braccio.s6,
        )
        vector = angles[4]

    elif key == pygame.K_k:
        vector[1] -= 10
        angles = Inverse_kinematics.move(vector)
        braccio.servo_movement(
            90 - angles[0],
            90 - angles[1],
            90 - angles[2],
            90 - angles[3],
            braccio.s5,
            braccio.s6,
        )
        vector = angles[4]

    elif key == pygame.K_j:
        vector[0] += 10
        angles = Inverse_kinematics.move(vector)
        braccio.servo_movement(
            90 - angles[0],
            90 - angles[1],
            90 - angles[2],
            90 - angles[3],
            braccio.s5,
            braccio.s6,
        )
        vector = angles[4]

    elif key == pygame.K_l:
        vector[0] -= 10
        angles = Inverse_kinematics.move(vector)
        braccio.servo_movement(
            90 - angles[0],
            90 - angles[1],
            90 - angles[2],
            90 - angles[3],
            braccio.s5,
            braccio.s6,
        )

    elif key == pygame.K_u:
        vector[2] += 10
        angles = Inverse_kinematics.move(vector)
        braccio.servo_movement(
            90 - angles[0],
            90 - angles[1],
            90 - angles[2],
            90 - angles[3],
            braccio.s5,
            braccio.s6,
        )
        vector = angles[4]

    elif key == pygame.K_o:
        vector[2] -= 10
        angles = Inverse_kinematics.move(vector)
        braccio.servo_movement(
            90 - angles[0],
            90 - angles[1],
            90 - angles[2],
            90 - angles[3],
            braccio.s5,
            braccio.s6,
        )
        vector = angles[4]

    return vector


def robotLogic():
    """
    Function that handles the manual movement of robot in 3d plane.
    """

    global vector

    # Get serial port though user input
    global vector
    serial_port = input("Enter the serial port (e.g., COM3, COM4, /dev/ttyACM0): ")
    use_mock = os.getenv("USE_MOCK", "false").lower() == "true"
    braccioDebug = BraccioDebug(serial_port_robot_magnet=serial_port, mock=use_mock)

    pygame.init()
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Keypress Detection")

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)

    font = pygame.font.Font(None, 74)
    small_font = pygame.font.Font(None, 36)

    key_history = []
    type_of_litter = ""
    running = True

    def display_text(text, font, color, x, y):
        text_surface = font.render(text, True, color)
        screen.blit(text_surface, (x, y))

    print("Press the keys for the output. Press ESC to quit.")

    # Checks that all of the movement values are within their bounds
    # If not, they are set to the closest bound

    # Run the UI logic
    while running:

        screen.fill(BLACK)
        display_text(
            "Press the key to see which key is pressed. Press ESC to exit.",
            small_font,
            WHITE,
            10,
            10,
        )
        display_text("Key History (last 5):", small_font, WHITE, 10, 60)

        for i, key in enumerate(key_history[-5:]):
            display_text(f"{i+1}: {key}", small_font, RED, 10, 100 + i * 40)

        # Display current servo angles
        display_text(f"Servo 1: {braccioDebug.s1}°", small_font, GREEN, 400, 100)
        display_text(f"Servo 2: {braccioDebug.s2}°", small_font, GREEN, 400, 140)
        display_text(f"Servo 3: {braccioDebug.s3}°", small_font, GREEN, 400, 180)
        display_text(f"Servo 4: {braccioDebug.s4}°", small_font, GREEN, 400, 220)
        display_text(f"Servo 5: {braccioDebug.s5}°", small_font, GREEN, 400, 260)
        display_text(f"Servo 6: {braccioDebug.s6}°", small_font, GREEN, 400, 300)

        if type_of_litter:
            display_text(
                f"Classification:{type_of_litter}", small_font, WHITE, 100, 400
            )

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                key_name = pygame.key.name(event.key)
                key_history.append(key_name)
                if event.key == pygame.K_c:
                    braccioDebug.home_position()
                elif event.key == pygame.K_p:
                    print(
                        braccioDebug.s1,
                        braccioDebug.s2,
                        braccioDebug.s3,
                        braccioDebug.s4,
                        braccioDebug.s5,
                        braccioDebug.s6,
                    )
                elif event.key == pygame.K_b:  # Bind B key to calibration
                    braccioDebug.calibrate_servos(braccioDebug)
                if event.key == pygame.K_ESCAPE:
                    running = False

        keys = pygame.key.get_pressed()

        # Control servos using keys

        for key in [
            pygame.K_a,
            pygame.K_s,
            pygame.K_w,
            pygame.K_d,
            pygame.K_i,
            pygame.K_k,
            pygame.K_j,
            pygame.K_l,
            pygame.K_u,
            pygame.K_o,
        ]:
            if keys[key]:
                vector = handle_key_press(braccioDebug, key, vector)

        if keys[pygame.K_m]:
            vector = [0, 0, 0]
            vector[0] = int(input("Enter x:"))
            vector[1] = int(input("Enter y:"))
            vector[2] = int(input("Enter z:"))
            print(vector)

            # Stand up straight
            braccioDebug.servo_movement(90, 90, 90, 90, 90, 10)

            # Jiggle the base
            baseServo = 90 - Inverse_kinematics.move(vector)[0]
            jiggle(braccioDebug, baseServo)

            # Move thew arm down with class open
            braccioDebug.servo_movement(
                braccioDebug.s1,
                90 - Inverse_kinematics.move(vector)[1],
                90 - Inverse_kinematics.move(vector)[2],
                90 - Inverse_kinematics.move(vector)[3],
                braccioDebug.s5,
                braccioDebug.s6,
            )

            # Shut the claw
            braccioDebug.servo_movement(
                braccioDebug.s1,
                braccioDebug.s2,
                braccioDebug.s3,
                braccioDebug.s4,
                braccioDebug.s5,
                73,
            )

            # Stand up straight with claw shut
            braccioDebug.servo_movement(90, 90, 90, 90, 90, braccioDebug.s6)

            vector = Inverse_kinematics.move(vector)[4]

            # Open claw to drop object
            braccioDebug.servo_movement(
                braccioDebug.s1,
                braccioDebug.s2,
                braccioDebug.s3,
                braccioDebug.s4,
                braccioDebug.s5,
                10,
            )
            time.sleep(1)

            braccioDebug.home_position()

        # if keys[pygame.K_5]:

        # MODEL_PATH = "./Model/model.tflite"
        # LABELMAP_PATH = "./Model/labels.txt"
        # depth = StereoVision.distInf.detect(MODEL_PATH, LABELMAP_PATH)

        # angle = 95

        # camera_position1 = np.array([0, 150, 50])
        # camera_position2 = np.array([0, 150, 50])
        # camera_position = (camera_position1 + camera_position2)/2

        # object_position = camera_distance.calculate_object_position(depth, angle, camera_position)
        # print("Object Position Relative to Robot Base:", object_position)

        if key_history:
            display_text(
                f"Last Key Pressed: {key_history[-1]}",
                font,
                WHITE,
                SCREEN_WIDTH // 2 - 150,
                SCREEN_HEIGHT - 100,
            )

        pygame.display.flip()

    pygame.quit()
    sys.exit()


def cameraLogic():
    MODEL_PATH = "./Model/model.tflite"
    LABELMAP_PATH = "./Model/labels.txt"

    port = distInf.serial_port()
    distInf.screen.fill(distInf.BLACK)
    pygame.display.flip()
    if port:
        distInf.detect(MODEL_PATH, LABELMAP_PATH, robot=False, port=port)


def automatedSystem():
    MODEL_PATH = "./Model/model.tflite"
    LABELMAP_PATH = "./Model/labels.txt"

    port = distInf.serial_port()
    distInf.screen.fill(distInf.BLACK)
    pygame.display.flip()
    if port:
        distInf.detect(MODEL_PATH, LABELMAP_PATH, robot=True, port=port)


def main():
    global d
    global vector

    # User input for interface mode
    mode = input(
        "Enter the interface mode (0 = Manual Control, 1 = Camera Mode, 2 = Manual & Camera Mode)"
    )
    mode = int(mode)

    if mode == 0:
        robotLogic()

    if mode == 1:
        cameraLogic()

    if mode == 2:
        automatedSystem()


if __name__ == "__main__":
    main()
