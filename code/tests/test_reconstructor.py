import sys
import os
import unittest
import tensorflow
from unittest.mock import mock_open, patch, MagicMock

# Allows the tests to find the graphReconstructor module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from graph_reconstructer import *

class TestReconstructor(unittest.TestCase):
    
    # Test case where the file does not exist
    @patch("os.path.isfile", return_value=False)
    def test_fileNotFound(self, fakeFile):
        result = reconstruct("thisIsNotAFile.pb")
        self.assertIsNone(result)
        
    # Test case to check file read works
    @patch("os.path.isfile", return_value=True)
    @patch("tensorflow.io.gfile.GFile")
    def test_fileRead(self, fakeGfile, fakeRead):
        # Mocks a fake TensorFlow graph
        graph_def = tf.compat.v1.GraphDef()
        node = graph_def.node.add()
        node.name = "test_node"
        node.op = "Placeholder"
        node.attr["dtype"].type = tf.float64.as_datatype_enum
        fakeData = graph_def.SerializeToString() 
        
        # Mocks the file reading
        fakeFile = MagicMock()
        fakeFile.read.return_value = fakeData
        fakeGfile.return_value.__enter__.return_value = fakeFile
    
        result = reconstruct("valid.pb") 
        
        # Ensures the correct value was returned from the reconstruct function
        fakeRead.assert_called_once_with("valid.pb")
        self.assertIsNotNone(result)
        self.assertIsInstance(result, tf.Graph)
        
    #
    @patch("tensorflow.io.write_graph")
    def test_fileWritten(self, fakeWrite):
        fakeWrite.return_value = None
        fakeGraph = tf.Graph()
        writeToFilePath(fakeGraph, "directory/is/real")
        fakeWrite.assert_called()

if __name__ == "__main__":
    unittest.main()