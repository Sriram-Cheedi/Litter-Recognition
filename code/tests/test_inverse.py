import sys
import os
import unittest
import numpy as np


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from unittest import skipIf
from interface import *
from inverse_kinematics import *
from braccio_adapter import BraccioAdapter


class TestInverseKin(unittest.TestCase):
    def test_move(self):
        # Make sure inputting large result does not create vector out of bounds
        self.assertTrue(np.array_equal (move(np.array([100000000, 0, 0]))[4], move(np.array([dmax, 0, 0]))[4]))    
        self.assertTrue(np.array_equal (move(np.array([-100000000, 0, 0]))[4], move(np.array([-dmax, 0, 0]))[4])) 

        self.assertTrue(np.array_equal (move(np.array([0, 0, 0]))[4], move(np.array([0, dmin, 0]))[4]))
        self.assertTrue(np.array_equal (move(np.array([0, 1, 0]))[4], move(np.array([0, dmin, 0]))[4]))
  
        

if __name__ == "__main__":
    unittest.main()
