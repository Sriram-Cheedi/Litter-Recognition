import pygame
import sys
import braccio_adapter
import Inverse_kinematics
from enum import Enum

x = 0
y = 150
z = 0
d = 100

class ServoMotor(Enum):
    S1 = 1
    S2 = 2
    S3 = 3
    S4 = 4
    S5 = 5
    S6 = 6
    
z_min = 20
# Function to ensure servo positions stay within defined bounds
def checkInBounds(values, uBound, lBound):
    newValues = [0] * 7
    for index, item in enumerate(values):
        if (uBound[index] < item):
            newValues[index] = uBound[index]
        elif (lBound[index] > item):
            newValues[index] = lBound[index]
        else:
            newValues[index] = item
    global z
    if z < z_min:
        z = z_min

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
        servoPos = [10, s1, s2, s3, s4, s5, s6]
        

        #Holds upper and lower bounds for each servo motors movement
        uBounds = [30, 180, 165, 180, 180, 180, 73]
        lBounds = [10, 0, 15, 0, 0, 0, 10]
    
        if servo.value == 1:
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

        # Update internal state
        self.s1, self.s2, self.s3, self.s4, self.s5, self.s6 = servoPos[1:]
    
    def up(self, servo : ServoMotor, degrees = 1):
        self.move_single_joint(servo, degrees)
        
    def down(self, servo: ServoMotor, degrees = -1):
        self.move_single_joint(servo, degrees)

def main():
    global d
    global x
    global y
    global z

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
    screen_width = 800
    screen_height = 600

    screen = pygame.display.set_mode((screen_width, screen_height))
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
                elif event.key == pygame.K_p:
                    print(braccioDebug.s1, braccioDebug.s2, braccioDebug.s3, braccioDebug.s4, braccioDebug.s5, braccioDebug.s6)
                if event.key == pygame.K_ESCAPE:
                    running = False

        keys = pygame.key.get_pressed()
        # if keys[pygame.K_q]:
        #     braccioDebug.up(ServoMotor.S1)
        # if keys[pygame.K_w]:
        #     braccioDebug.up(ServoMotor.S2)
        # if keys[pygame.K_e]:
        #     braccioDebug.up(ServoMotor.S3)
        # if keys[pygame.K_r]:
        #     braccioDebug.up(ServoMotor.S4)
        # if keys[pygame.K_t]:
        #     braccioDebug.up(ServoMotor.S5)
        # if keys[pygame.K_y]:
        #     braccioDebug.up(ServoMotor.S6)
        # if keys[pygame.K_a]:
        #     braccioDebug.down(ServoMotor.S1)
        # if keys[pygame.K_s]:
        #     braccioDebug.down(ServoMotor.S2)
        # if keys[pygame.K_d]:
        #     braccioDebug.down(ServoMotor.S3)
        # if keys[pygame.K_f]:
        #     braccioDebug.down(ServoMotor.S4)
        # if keys[pygame.K_g]:
        #     braccioDebug.down(ServoMotor.S5)
        # if keys[pygame.K_h]:
        #     braccioDebug.down(ServoMotor.S6)
        
        if keys[pygame.K_a]:
            braccioDebug.up(ServoMotor.S5)
        if keys[pygame.K_s]:
            braccioDebug.up(ServoMotor.S6)
        if keys[pygame.K_w]:
            braccioDebug.down(ServoMotor.S6)
        if keys[pygame.K_d]:
            braccioDebug.down(ServoMotor.S5)

        
        
        if keys[pygame.K_i]:
            y += 10
            servo4_adjustment = 10 
            braccioDebug.servo_movement(90 - Inverse_kinematics.move(x, y, z)[0], 90 - Inverse_kinematics.move(x, y, z)[1], 90 - Inverse_kinematics.move(x, y, z)[2], min(180, 90 - Inverse_kinematics.move(x, y, z)[3] + servo4_adjustment),braccioDebug.s5, braccioDebug.s6)


        if keys[pygame.K_k]:
            y -= 10
            braccioDebug.servo_movement(90 - Inverse_kinematics.move(x, y, z)[0], 90 - Inverse_kinematics.move(x, y, z)[1], 90 - Inverse_kinematics.move(x, y, z)[2], 90 - Inverse_kinematics.move(x, y, z)[3],braccioDebug.s5, braccioDebug.s6)

            
        if keys[pygame.K_j]:
            x += 10
            braccioDebug.servo_movement(90 - Inverse_kinematics.move(x, y, z)[0], 90 - Inverse_kinematics.move(x, y, z)[1], 90 - Inverse_kinematics.move(x, y, z)[2], 90 - Inverse_kinematics.move(x, y, z)[3], braccioDebug.s5, braccioDebug.s6)

        if keys[pygame.K_l]:
            x -= 10
            braccioDebug.servo_movement(90 - Inverse_kinematics.move(x, y, z)[0], 90 - Inverse_kinematics.move(x, y, z)[1], 90 - Inverse_kinematics.move(x, y, z)[2], 90 - Inverse_kinematics.move(x, y, z)[3], braccioDebug.s5, braccioDebug.s6)

        if keys[pygame.K_u]:
            z += 10
            braccioDebug.servo_movement(90 - Inverse_kinematics.move(x, y, z)[0], 90 - Inverse_kinematics.move(x, y, z)[1], 90 - Inverse_kinematics.move(x, y, z)[2], 90 - Inverse_kinematics.move(x, y, z)[3], braccioDebug.s5, braccioDebug.s6)

        if keys[pygame.K_o]:
            z -= 10
            braccioDebug.servo_movement(90 - Inverse_kinematics.move(x, y, z)[0], 90 - Inverse_kinematics.move(x, y, z)[1], 90 - Inverse_kinematics.move(x, y, z)[2], 90 - Inverse_kinematics.move(x, y, z)[3], braccioDebug.s5, braccioDebug.s6)

        if keys[pygame.K_m]:
            x = int(input("Enter x:"))
            y = int(input("Enter y:"))
            z = int(input("Enter z:"))
            print(x, y, z)

            braccioDebug.servo_movement(90, 90, 90, 90, 90, 10)
            braccioDebug.servo_movement(90 - Inverse_kinematics.move(x, y, z)[0], 90 - Inverse_kinematics.move(x, y, z)[1], 90 - Inverse_kinematics.move(x, y, z)[2], 90 - Inverse_kinematics.move(x, y, z)[3], braccioDebug.s5, braccioDebug.s6)
            braccioDebug.servo_movement(braccioDebug.s1, braccioDebug.s2, braccioDebug.s3, braccioDebug.s4, braccioDebug.s5, 73)
            braccioDebug.servo_movement(90, 90, 90, 90, 90, braccioDebug.s6)
        
        if key_history:
            display_text(f"Last Key Pressed: {key_history[-1]}", font, WHITE, screen_width // 2 - 150, screen_height - 100)


        pygame.display.flip()


    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()