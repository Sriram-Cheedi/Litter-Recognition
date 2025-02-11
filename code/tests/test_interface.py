import sys
import os
import unittest
import numpy as np


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from unittest import skipIf
from interface import *
from braccio_adapter import BraccioAdapter

hardware_tests = os.getenv("RUN_HARDWARE_TESTS", "false").lower() == "true"

class TestInterface(unittest.TestCase):
    
    def test_checkInBounds(self):
        
        uBounds = [30, 180, 165, 180, 180, 180, 73]
        lBounds = [10, 0, 15, 0, 0, 0, 10]

        # Edge cases
        self.assertEqual(checkInBounds([10, 0, 15, 0, 0, 0, 10], uBounds, lBounds),[10, 0, 15, 0, 0, 0, 10])
        self.assertEqual(checkInBounds([30, 180, 165, 180, 180, 180, 73], uBounds, lBounds),[30, 180, 165, 180, 180, 180, 73])

        # Values exceeding bounds
        self.assertEqual(checkInBounds([20, 90, 90, 90, 90, 90, 40], uBounds, lBounds),[20, 90, 90, 90, 90, 90, 40])
        
        self.assertEqual(checkInBounds([15, 90, 100, 200, 150, -10, 50], uBounds, lBounds), [15, 90, 100, 180, 150, 0, 50])
        
        
    @skipIf(not hardware_tests, "Skipping hardware tests in CI.")
    def test_move_single_joint(self):
        
        braccio_debug = BraccioDebug(serial_port_robot_magnet="COM4")
        print(f"Braccio S1 value after move: {braccio_debug.s1}")
        
        
        for servo in ServoMotor:
            uBounds = [30, 180, 165, 180, 180, 180, 73]
            lBounds = [10, 0, 15, 0, 0, 0, 10]
            braccio_debug.move_single_joint(servo, 50)
            self.assertTrue(lBounds[servo.value - 1] <= getattr(braccio_debug, f"s{servo.value}") <= uBounds[servo.value - 1])

        # Move S1 within bounds
        braccio_debug.move_single_joint(ServoMotor.S1, 5)
        self.assertTrue(10 <= braccio_debug.s1 <= 30)
        
        # Move S6 outside bounds
        braccio_debug.move_single_joint(ServoMotor.S6, -100)
        self.assertEqual(braccio_debug.s6, 10)
        
        braccio_debug.move_single_joint(ServoMotor.S6, 100)
        self.assertEqual(braccio_debug.s6, 73)
        
        
    @skipIf(not hardware_tests, "Skipping hardware tests in CI.")
    def test_up_down(self):
        
        braccio_debug = BraccioDebug(serial_port_robot_magnet="COM4")
        # Move Servo 3 up and down
        initial_s3 = braccio_debug.s3
        braccio_debug.up(ServoMotor.S3, 5)
        self.assertEqual(braccio_debug.s3, min(165, initial_s3 + 5))
        braccio_debug.down(ServoMotor.S3, 10)
        self.assertEqual(braccio_debug.s3, max(15, initial_s3 - 5))

    def test_inverse_kinematics(self):
        
        vector = [50, 100, -30]
        result = Inverse_kinematics.move(*vector) 
        self.assertEqual(len(result), 5)
        self.assertTrue(-180 <= result[0] <= 180)  
        self.assertTrue(-180 <= result[1] <= 180)  
        self.assertTrue(-180 <= result[2] <= 180)
        self.assertTrue(-180 <= result[3] <= 180)  
        self.assertIsInstance(result[4], np.ndarray)
        
    @skipIf(not hardware_tests, "Skipping hardware tests in CI.") 
    def test_braccio_initialization(self):
        braccio = BraccioAdapter(serial_port_robot="COM4")
        self.assertEqual(braccio.s1, 0)
        self.assertEqual(braccio.s2, 40)
        self.assertEqual(braccio.s3, 180)
        self.assertEqual(braccio.s4, 0)
        self.assertEqual(braccio.s5, 180)
        self.assertEqual(braccio.s6, 60)
        
    @skipIf(not hardware_tests, "Skipping hardware tests in CI.") 
    def test_servo_edge_cases(self):
        braccio = BraccioAdapter(serial_port_robot="COM4")
        braccio.servo_movement(0, 0, 0, 0, 0, 0, 0)
        self.assertEqual(braccio.s1, 0)
        self.assertEqual(braccio.s2, 0)
        self.assertEqual(braccio.s3, 0)
        self.assertEqual(braccio.s4, 0)
        self.assertEqual(braccio.s5, 0)
        self.assertEqual(braccio.s6, 0)


    @skipIf(not hardware_tests, "Skipping hardware tests in CI.")
    def test_servo_movement_and_home_position(self):
        
        braccio = BraccioAdapter(serial_port_robot="COM4")
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
        self.assertEqual(braccio.s6, 60)

if __name__ == "__main__":
    unittest.main()
