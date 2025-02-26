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
        self.assertEqual(move(100000, 100000, 100000), move(0,0,dmax))
        
        


