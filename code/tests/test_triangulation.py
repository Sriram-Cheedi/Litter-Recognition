import sys
import os
import unittest
import cv2
import numpy as np
import time 
from unittest.mock import patch


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../StereoVision")))
from triangulation import *

class TestTriangulation(unittest.TestCase):
    
    def test_DepthCalculation(self):
        leftFrame, rightFrame = np.zeros((300, 300))
        result = findDepth((10, 60), (30, 80), leftFrame, rightFrame, 9, 8, 60)
        self.assertEqual(result, 249.4)
    
    def test_SameCaptureWidth():
        leftFrame = np.zeros(450, 400)
        rightFrame = np.zeros((300, 300))
        with patch("builtins.print") as mock_print:
            findDepth((10, 60), (150, 20), leftFrame, rightFrame, 9, 8, 90)
            mock_print.assert_called_with("Left and right frames do not have the same width")
    
    
if __name__ == "__main__":
    unittest.main()