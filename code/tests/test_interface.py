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

    def test_moving_joint(self):
        braccio = BraccioDebug()
        
        # Move servo within bounds
        braccio.move_single_joint(ServoMotor.S1, 10)
        self.assertTrue(10 <= braccio.s1 <= 30)
        
        # Move servo out of bounds
        braccio.move_single_joint(ServoMotor.S6, 100)
        self.assertEqual(braccio.s6, 73)
        
        braccio.move_single_joint(ServoMotor.S6, -100)
        self.assertEqual(braccio.s6, 10)

    def test_multiple_moves(self):
        braccio = BraccioDebug()
        braccio.move_single_joint(ServoMotor.S3, 20)
        braccio.move_single_joint(ServoMotor.S3, -10)
        
        self.assertTrue(15 <= braccio.s3 <= 165)
        
        braccio.move_single_joint(ServoMotor.S3, -100)
        self.assertEqual(braccio.s3, 15)

    def test_key_mapping_logic(self):
        braccio = BraccioDebug()
        initial_pos = braccio.s5
        
        # Simulate pressing 'A' key (Servo 5 up)
        braccio.up(ServoMotor.S5, 5)
        self.assertEqual(braccio.s5, min(180, initial_pos + 5))
        
        # Simulate pressing 'D' key (Servo 5 down)
        braccio.down(ServoMotor.S5, 10)
        self.assertEqual(braccio.s5, max(0, initial_pos - 5))
    

    def test_inverse_kinematics(self):
        vector = np.array([50, 100, -30]) 
        result = Inverse_kinematics.move(vector)  
        self.assertEqual(len(result), 5)
        self.assertTrue(-180 <= result[0] <= 180)  
        self.assertTrue(-180 <= result[1] <= 180)  
        self.assertTrue(-180 <= result[2] <= 180)
        self.assertTrue(-180 <= result[3] <= 180)  
        self.assertIsInstance(result[4], np.ndarray)


if __name__ == "__main__":
    unittest.main()
