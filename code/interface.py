import pygame
import sys
import braccio_adapter
from enum import Enum

class ServoMotor(Enum):
    S1 = 1
    S2 = 2
    S3 = 3
    S4 = 4
    S5 = 5
    S6 = 6

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
    def __init__(self, serial_port_robot_magnet="COM4"):
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
    
    def up(self, servo : ServoMotor, degrees = 4):
        self.move_single_joint(servo, degrees)
        
    def down(self, servo: ServoMotor, degrees = -4):
        self.move_single_joint(servo, degrees)

def main():
    braccioDebug :BraccioDebug = BraccioDebug(serial_port_robot_magnet="COM4")
    braccioControlString = "Control the Braccio using: \n\
                            Servo 1 UP/DOWN Q/A\n\
                            Servo 2 UP/DOWN W/S\n\
                            Servo 3 UP/DOWN E/D\n\
                            Servo 4 UP/DOWN R/F\n\
                            Servo 5 UP/DOWN T/G\n\
                            Servo 6 UP/DOWN Z/Y\n\
                            HOME C\
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

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                key_name = pygame.key.name(event.key)
                key_history.append(key_name)
                if event.key == pygame.K_c:
                    braccioDebug.home_position()
                elif event.key == pygame.K_p:
                    braccioDebug.move_to_object()
                    # print(braccioDebug.s1, braccioDebug.s2, braccioDebug.s3, braccioDebug.s4, braccioDebug.s5, braccioDebug.s6)
                elif event.key == pygame.K_l:
                    braccioDebug.move_to_object(0)
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
        if keys[pygame.K_z]:
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

        
        if key_history:
            display_text(f"Last Key Pressed: {key_history[-1]}", font, WHITE, screen_width // 2 - 250, screen_height // 2 - 40)


        pygame.display.flip()


    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
