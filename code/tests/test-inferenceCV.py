import sys
import os
import unittest
import numpy as np
from unittest.mock import MagicMock, patch

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__, ".."))))
from inferenceCV import *

class TestInferenceCV(unittest.TestCase):
    
    # Test case for loading the label file
    @patch("builtins.open", unittest.mock.mock_open(read_data="1 Testing\n2 Code\n3 Is\n4 Fun"))
    def test_loadLabelMap(self):
        returnedMap = loadLabelMap("labels.txt")
        expectedMap = [None, "Testing", "Code", "Is", "Fun"]
        self.assertEqual(returnedMap, expectedMap)
        
if __name__ == "__main__":
    unittest.main()