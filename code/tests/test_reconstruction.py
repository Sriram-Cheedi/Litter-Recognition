# Unit Tests for Graph Reconstruction code

import unittest
from unittest.mock import patch, mock_open, MagicMock
from graphReconstructer import reconstruct
import tensorflow as tf
import os

@patch("os.path.isfile", return_value=True)
@patch("tensorflow.io.gfile.GFile")
@patch("tensorflow.io.write_graph")
def test_correctInput(self, mock_write_graph, mock_gfile, mock_isfile):
    # Mock reading the .pb file
    mock_gfile.return_value.read.return_value = b"mock serialized graph"

    # Run the function
    graph = reconstruct("valid/path/to/input.pb", "valid/path/to/output.pb")
        
    # Assertions
    self.assertIsInstance(graph, tf.Graph)
    mock_gfile.assert_called_once_with("valid/path/to/input.pb", "rb")
    mock_write_graph.assert_called_once()


def test_dirCreated():
    return

def test_missingFile():
    return


if __name__ == "__main__":
    unittest.main()