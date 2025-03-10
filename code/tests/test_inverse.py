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
    def test_bound_vector(self):

        # Test both sides of the bounding
        self.assertEqual(np.linalg.norm(boundVector(np.array([100000, 200000, 300000]))), dmax)
        self.assertEqual(np.linalg.norm(boundVector(np.array([1, 2, 3]))), dmin)

        # Make sure inputting large result does not create vector out of bounds
        self.assertTrue(np.array_equal (boundVector(np.array([100000000, 0, 0])), boundVector(np.array([dmax, 0, 0]))))    
        self.assertTrue(np.array_equal (boundVector(np.array([-100000000, 0, 0])), boundVector(np.array([-dmax, 0, 0])))) 

        self.assertTrue(np.array_equal (boundVector(np.array([0, -1, 0])), boundVector(np.array([0, -dmin, 0]))))
        self.assertTrue(np.array_equal (boundVector(np.array([0, 1, 0])), boundVector(np.array([0, dmin, 0]))))

    def test_move(self):
        # Test that bound vector works within the context of the move function
        self.assertEqual(np.linalg.norm(move(np.array([100000, 200000, 300000]))[4]), dmax)
        self.assertEqual(np.linalg.norm(move(np.array([1, 2, 3]))[4]), dmin)

        self.assertTrue(np.array_equal (move(np.array([100000000, 0, 0]))[4], move(np.array([dmax, 0, 0]))[4]))    
        self.assertTrue(np.array_equal (move(np.array([-100000000, 0, 0]))[4], move(np.array([-dmax, 0, 0]))[4])) 

        self.assertTrue(np.array_equal (move(np.array([0, -1, 0]))[4], move(np.array([0, -dmin, 0]))[4]))
        self.assertTrue(np.array_equal (move(np.array([0, 1, 0]))[4], move(np.array([0, dmin, 0]))[4]))
        
        self.assertTrue(np.array_equal (boundVector(np.array([100000000, 0, 0])), np.array([dmax, 0, 0])))
  
        

if __name__ == "__main__":
    unittest.main()
