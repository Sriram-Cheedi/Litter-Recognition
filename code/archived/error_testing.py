"""
This part of code is for testing the error values of the Braccio arm
"""
import pygame
import sys
import braccio_adapter
import Inverse_kinematics
from enum import Enum
import numpy as np

vector = np.array([0, 150, 0])
d = 100

class ServoMotor(Enum):
    S1 = 1
    S2 = 2
    S3 = 3
    S4 = 4
    S5 = 5
    S6 = 6

# Function to ensure servo positions stay within defined bounds
def checkInBounds(values, upper_bound, lower_bound):
    newValues = [0] * 7
    for index, item in enumerate(values):
        if (upper_bound[index] < item):
            newValues[index] = upper_bound[index]
        elif (lower_bound[index] > item):
            newValues[index] = lower_bound[index]
        else:
            newValues[index] = item
    return newValues

class BraccioDebug(braccio_adapter.BraccioAdapter):
    def __init__(self, serial_port_robot_magnet="COM3"):
        super().__init__(serial_port_robot_magnet,)
        self.home_position()
    

    def move_single_joint(self, servo, degrees):
        # get currect vals
        s1 = self.s1
        s2 = self.s2 
        s3 = self.s3
        s4 = self.s4 
        s5 = self.s5
        s6 = self.s6
        servo_position = [10, s1, s2, s3, s4, s5, s6]
        

        #Holds upper and lower bounds for each servo motors movement
        upper_bounds = [30, 180, 165, 180, 180, 180, 73]
        lower_bounds = [10, 0, 15, 0, 0, 0, 10]
    
        if servo.value == 1:
            servo_position[1] += degrees
        if servo.value == 2:
            servo_position[2] += degrees
        if servo.value == 3:
            servo_position[3] += degrees
        if servo.value == 4:
            servo_position[4] += degrees
        if servo.value == 5:
            servo_position[5] += degrees
        if servo.value == 6:
            servo_position[6] += degrees

    
            
        servo_position = checkInBounds(servo_position, upper_bounds, lower_bounds)
        self.servo_movement(servo_position[1], servo_position[2], servo_position[3], servo_position[4], servo_position[5], servo_position[6])

        # Update internal state
        self.s1, self.s2, self.s3, self.s4, self.s5, self.s6 = servo_position[1:]
    
    def up(self, servo : ServoMotor, degrees = 1):
        self.move_single_joint(servo, degrees)
        
    def down(self, servo: ServoMotor, degrees = -1):
        self.move_single_joint(servo, degrees)

def main():
    global d
    global vector

    # User input for serial port
    serial_port = input("Enter the serial port (e.g., COM3, COM4, /dev/ttyUSB0): ")
    braccioDebug = BraccioDebug(serial_port_robot_magnet=serial_port)    
    braccioControlString = "Control the Braccio using: \n\
                            Servo 5 UP/DOWN A/D\n\
                            Servo 6 UP/DOWN S/W\n\
                            HOME C\
                            Print degrees V\
                            "
    print(braccioControlString)
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

    running = True


    def display_text(text, font, color, x, y):
        text_surface = font.render(text, True, color)
        screen.blit(text_surface, (x, y))

    print("Press the keys for the output. Press ESC to quit.")

    #Checks that all of the movement values are within their bounds
    #If not, they are set to the closest bound
    

    while running:
        
        screen.fill(BLACK)
        display_text("Press the key to see which key is pressed. Press ESC to exit.", small_font, WHITE, 10, 10)
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

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                key_name = pygame.key.name(event.key)
                key_history.append(key_name)
                if event.key == pygame.K_c:
                    braccioDebug.home_position()
                elif event.key == pygame.K_v:
                    print(braccioDebug.s1, braccioDebug.s2, braccioDebug.s3, braccioDebug.s4, braccioDebug.s5, braccioDebug.s6)
                if event.key == pygame.K_ESCAPE:
                    running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            braccioDebug.up(ServoMotor.S1)
        if keys[pygame.K_w]:
            braccioDebug.up(ServoMotor.S2)
        if keys[pygame.K_e]:
            braccioDebug.up(ServoMotor.S3)
        if keys[pygame.K_r]:
            braccioDebug.up(ServoMotor.S4)
        if keys[pygame.K_t]:
            braccioDebug.up(ServoMotor.S5)
        if keys[pygame.K_y]:
            braccioDebug.up(ServoMotor.S6)
        if keys[pygame.K_a]:
            braccioDebug.down(ServoMotor.S1)
        if keys[pygame.K_s]:
            braccioDebug.down(ServoMotor.S2)
        if keys[pygame.K_d]:
            braccioDebug.down(ServoMotor.S3)
        if keys[pygame.K_f]:
            braccioDebug.down(ServoMotor.S4)
        if keys[pygame.K_g]:
            braccioDebug.down(ServoMotor.S5)
        if keys[pygame.K_h]:
            braccioDebug.down(ServoMotor.S6)
        
        # if keys[pygame.K_a]:
        #     braccioDebug.up(ServoMotor.S5)
        #     vector = Inverse_kinematics.move(vector)[4]
        # if keys[pygame.K_s]:
        #     braccioDebug.up(ServoMotor.S6)
        #     vector = Inverse_kinematics.move(vector)[4]
        # if keys[pygame.K_w]:
        #     braccioDebug.down(ServoMotor.S6)
        #     vector = Inverse_kinematics.move(vector)[4]
        # if keys[pygame.K_d]:
        #     braccioDebug.down(ServoMotor.S5)
        #     vector = Inverse_kinematics.move(vector)[4]

        
        
        # if keys[pygame.K_i]:
        #     vector[1] += 10
        #     braccioDebug.servo_movement(90 - Inverse_kinematics.move(vector)[0], 90 - Inverse_kinematics.move(vector)[1], 90 - Inverse_kinematics.move(vector)[2], 90 - Inverse_kinematics.move(vector)[3], braccioDebug.s5, braccioDebug.s6)
        #     vector = Inverse_kinematics.move(vector)[4]

        # if keys[pygame.K_k]:
        #     vector[1] -= 10
        #     braccioDebug.servo_movement(90 - Inverse_kinematics.move(vector)[0], 90 - Inverse_kinematics.move(vector)[1], 90 - Inverse_kinematics.move(vector)[2], 90 - Inverse_kinematics.move(vector)[3], braccioDebug.s5, braccioDebug.s6)
        #     vector = Inverse_kinematics.move(vector)[4]

        # if keys[pygame.K_j]:
        #     vector[0] += 10
        #     braccioDebug.servo_movement(90 - Inverse_kinematics.move(vector)[0], 90 - Inverse_kinematics.move(vector)[1], 90 - Inverse_kinematics.move(vector)[2], 90 - Inverse_kinematics.move(vector)[3], braccioDebug.s5, braccioDebug.s6)
        #     vector = Inverse_kinematics.move(vector)[4]

        # if keys[pygame.K_l]:
        #     vector[0] -= 10
        #     braccioDebug.servo_movement(90 - Inverse_kinematics.move(vector)[0], 90 - Inverse_kinematics.move(vector)[1], 90 - Inverse_kinematics.move(vector)[2], 90 - Inverse_kinematics.move(vector)[3], braccioDebug.s5, braccioDebug.s6)

        # if keys[pygame.K_u]:
        #     vector[2] += 10
        #     braccioDebug.servo_movement(90 - Inverse_kinematics.move(vector)[0], 90 - Inverse_kinematics.move(vector)[1], 90 - Inverse_kinematics.move(vector)[2], 90 - Inverse_kinematics.move(vector)[3], braccioDebug.s5, braccioDebug.s6)
        #     vector = Inverse_kinematics.move(vector)[4]

        # if keys[pygame.K_o]:
        #     vector[2] -= 10
        #     braccioDebug.servo_movement(90 - Inverse_kinematics.move(vector)[0], 90 - Inverse_kinematics.move(vector)[1], 90 - Inverse_kinematics.move(vector)[2], 90 - Inverse_kinematics.move(vector)[3], braccioDebug.s5, braccioDebug.s6)
        #     vector = Inverse_kinematics.move(vector)[4]

        # if keys[pygame.K_m]:
        #     vector[0] = int(input("Enter x:"))
        #     vector[1] = int(input("Enter y:"))
        #     vector[2] = int(input("Enter z:"))
        #     print(vector)

        #     braccioDebug.servo_movement(90, 90, 90, 90, 90, 10)
        #     braccioDebug.servo_movement(90 - Inverse_kinematics.move(vector)[0], 90 - Inverse_kinematics.move(vector)[1], 90 - Inverse_kinematics.move(vector)[2], 90 - Inverse_kinematics.move(vector)[3], braccioDebug.s5, braccioDebug.s6)
        #     braccioDebug.servo_movement(braccioDebug.s1, braccioDebug.s2, braccioDebug.s3, braccioDebug.s4, braccioDebug.s5, 73)
        #     braccioDebug.servo_movement(90, 90, 90, 90, 90, braccioDebug.s6)
        
        #     vector = Inverse_kinematics.move(vector)[4]

        if keys[pygame.K_b]:
            # ServoMotor.S1 = int(input("Enter 1:"))
            # ServoMotor.S2 = int(input("Enter 2:"))
            # ServoMotor.S3 = int(input("Enter 3:"))
            # ServoMotor.S4 = int(input("Enter 4:"))
            # ServoMotor.S5 = int(input("Enter 5:"))
            # ServoMotor.S6 = int(input("Enter 6:"))
            braccioDebug.s1 = int(input("Enter 1:"))
            braccioDebug.s2 = int(input("Enter 2:"))
            braccioDebug.s3 = int(input("Enter 3:"))
            braccioDebug.s4 = int(input("Enter 4:"))
            braccioDebug.s5 = int(input("Enter 5:"))
            braccioDebug.s6 = int(input("Enter 6:"))

            braccioDebug.servo_movement(braccioDebug.s1, braccioDebug.s2, braccioDebug.s3, braccioDebug.s4, braccioDebug.s5, braccioDebug.s6)

        if key_history:
            display_text(f"Last Key Pressed: {key_history[-1]}", font, WHITE, SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT - 100)


        pygame.display.flip()


    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
