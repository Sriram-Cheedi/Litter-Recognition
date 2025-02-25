import sys
import os
import unittest
import numpy as np


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from unittest import skipIf
from interface import *


class TestInterface(unittest.TestCase):

    def setUp(self):
        self.braccio = BraccioDebug(mock=True)
    
    def test_checkInBounds(self):
    
        uBounds = [30, 180, 165, 180, 180, 180, 73]
        lBounds = [10, 0, 15, 0, 0, 0, 10]

        # Edge cases
        self.assertEqual(checkInBounds([10, 0, 15, 0, 0, 0, 10], uBounds, lBounds),[10, 0, 15, 0, 0, 0, 10])
        self.assertEqual(checkInBounds([30, 180, 165, 180, 180, 180, 73], uBounds, lBounds),[30, 180, 165, 180, 180, 180, 73])

        # Values exceeding bounds
        self.assertEqual(checkInBounds([20, 90, 90, 90, 90, 90, 40], uBounds, lBounds),[20, 90, 90, 90, 90, 90, 40])
        
        self.assertEqual(checkInBounds([15, 90, 100, 200, 150, -10, 50], uBounds, lBounds), [15, 90, 100, 180, 150, 0, 50])
        self.assertEqual(checkInBounds([-50, 500, 200, -100, 300, -50, 100], uBounds, lBounds),[10, 180, 165, 0, 180, 0, 73])

    def test_moving_joint(self):
        
        # Move servo within bounds
        self.braccio.move_single_joint(ServoMotor.S1, 10)
        self.assertTrue(10 <= self.braccio.s1 <= 30)
        
        # Move servo out of bounds
        self.braccio.move_single_joint(ServoMotor.S6, 100)
        self.assertEqual(self.braccio.s6, 73)
        
        self.braccio.move_single_joint(ServoMotor.S6, -100)
        self.assertEqual(self.braccio.s6, 10)

    def test_multiple_moves(self):
        self.braccio.move_single_joint(ServoMotor.S3, 20)
        self.braccio.move_single_joint(ServoMotor.S3, -10)
        
        self.assertTrue(15 <= self.braccio.s3 <= 165)
        
        self.braccio.move_single_joint(ServoMotor.S3, -100)
        self.assertEqual(self.braccio.s3, 15)

    def test_key_mapping_logic(self):
       
        initial_pos = self.braccio.s5
        
        # Simulate pressing 'A' key (Servo 5 up)
        self.braccio.up(ServoMotor.S5, 5)
        self.assertEqual(self.braccio.s5, min(180, initial_pos + 5))
    

    def test_inverse_kinematics(self):
        vector = np.array([50, 100, -30]) 
        result = Inverse_kinematics.move(vector)  
        self.assertEqual(len(result), 5)
        self.assertTrue(-180 <= result[0] <= 180)  
        self.assertTrue(-180 <= result[1] <= 180)  
        self.assertTrue(-180 <= result[2] <= 180)
        self.assertTrue(-180 <= result[3] <= 180)  
        self.assertIsInstance(result[4], np.ndarray)

    def test_initial_positions(self):
       
        self.assertEqual(self.braccio.s1, 0)
        self.assertEqual(self.braccio.s2, 40)
        self.assertEqual(self.braccio.s3, 180)
        self.assertEqual(self.braccio.s4, 0)
        self.assertEqual(self.braccio.s5, 180)
        self.assertEqual(self.braccio.s6, 60)

    def test_servo_reset(self):

        self.braccio.home_position()
        self.assertEqual(self.braccio.s1, 0)
        self.assertEqual(self.braccio.s2, 40)
        self.assertEqual(self.braccio.s3, 180)

    def test_extreme_movements(self):
        self.braccio.move_single_joint(ServoMotor.S4, 200)
        self.assertEqual(self.braccio.s4, 180)
        self.braccio.move_single_joint(ServoMotor.S4, -200)
        self.assertEqual(self.braccio.s4, 0)

    def test_inverse_kinematics_large_values(self):
        vector = np.array([500, 500, 500])
        result = Inverse_kinematics.move(vector)
        self.assertEqual(len(result), 5)

    def test_servo_decrement_logic(self):
        self.braccio.down(ServoMotor.S2, 15)
        self.assertGreaterEqual(self.braccio.s2, 0)
        self.braccio.down(ServoMotor.S2, 50)
        self.assertEqual(self.braccio.s2, 105)
    


if __name__ == "__main__":
    unittest.main()
