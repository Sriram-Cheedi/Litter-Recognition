import serial
import time

""" 
Class that communicates with an Arduino over the serial protocol
"""
class BraccioAdapter:
    def __init__(self, serial_port_robot="COM3"):
        # serial connection
        self.s_conn_robot = serial.Serial(serial_port_robot, 115200, timeout=10)
        time.sleep(3)
        self.keywords_robot = ["P"]
        print("Braccio initialized...")


    def write(self, string):
        # Braccio control
        if any( keyword in string for keyword in  self.keywords_robot ):
            self.s_conn_robot.write(string.encode())
            self.s_conn_robot.readline()

    """
        (step delay  M1 , M2 , M3 , M4 , M5 , M6)

        Step Delay: a milliseconds delay between the movement of each servo.  Allowed values from 10 to 30 msec.
        M1=base degrees. Allowed values from 0 to 180 degrees
        M2=shoulder degrees. Allowed values from 15 to 165 degrees
        M3=elbow degrees. Allowed values from 0 to 180 degrees
        M4=wrist vertical degrees. Allowed values from 0 to 180 degrees
        M5=wrist rotation degrees. Allowed values from 0 to 180 degrees
        M6=gripper degrees. Allowed values from 10 to 73 degrees. 10: the toungue is open, 73: the gripper is closed.
  """
    def servo_movement(self, s1, s2, s3, s4, s5, s6=60, speed=100):
        self.s1 = s1
        self.s2 = s2 
        self.s3 = s3
        self.s4 = s4 
        self.s5 = s5
        self.s6 = s6
        self.write(f'P{speed},{s1},{s2},{s3},{s4},{s5},{s6},\n')

    def get_serial_connection(self):
        return self.s_conn

    def straight_position(self):
        self.servo_movement(90, 90, 90, 90, 90)
    
    def home_position(self):
        self.servo_movement(0, 40, 180, 0, 180)