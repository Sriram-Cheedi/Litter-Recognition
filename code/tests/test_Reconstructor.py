import sys
import os
import unittest
import tensorflow
from unittest.mock import mock_open, patch
from graphReconstructer import *

class TestReconstructor(unittest.TestCase):
    
    @patch("os.path.isfile", return_value=False)
    def test_fileNotFound():
        return
    
    @patch("tensorflow.io.gfile.GFile")
    def test_fileCreated():
        return
    
    @patch("tensorflow.io.gfile.GFile")
    def test_emptyFileThrowsError():
        return
    
    def test_incorrectPBFile():
        return


if __name__ == "__main__":
    unittest.main()