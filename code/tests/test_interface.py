import unittest
import serial

from interface import *
from braccio_adapter import BraccioAdapter

class Test_interface(unittest.TestCase):
    def test_inBounds(self):
        uBounds = [30, 180, 165, 180, 180, 180, 73]
        lBounds = [10, 0, 15, 0, 0, 0, 10]
        
        testValues = [8, 190, 15, 56, 85, 181, 72]
        self.assertEqual(checkInBounds(testValues, uBounds, lBounds) == [10, 180, 15, 56, 85, 180, 72])
        
        testValues = [31, -1, 166, 181, 181, -1, 9]
        self.assertEqual(checkInBounds(testValues, uBounds, lBounds) == [30, 0, 165, 180, 180, 0, 10])
        
    def test_servo_movement_and_Home_position(self):
        braccio = BraccioAdapter(serial_port_robot="COM3")
        braccio.servo_movement(90, 90, 90, 90, 90, 60, 20)
        self.assertEqual(braccio.s1, 90)
        self.assertEqual(braccio.s2, 90)
        self.assertEqual(braccio.s3, 90)
        self.assertEqual(braccio.s4, 90)
        self.assertEqual(braccio.s5, 90)
        self.assertEqual(braccio.s6, 60)

        braccio.home_position()
        self.assertEqual(braccio.s1, 0)
        self.assertEqual(braccio.s2, 40)
        self.assertEqual(braccio.s3, 180)
        self.assertEqual(braccio.s4, 0)
        self.assertEqual(braccio.s5, 180)
        
    def test_moveSingleJoint(self):
        braccio_debug = BraccioDebug(serial_port_robot_magnet="COM3")
        braccio_debug.move_single_joint(ServoMotor.S1, 10)
        self.assertTrue(10 <= braccio_debug.s1 <= 30)
   
     
def test_all():
    assert True
            
def test_feature():
    assert True
