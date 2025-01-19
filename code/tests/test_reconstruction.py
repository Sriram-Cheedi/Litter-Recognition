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

@patch("os.path.isfile", return_value=True)
@patch("os.makedirs")
@patch("tensorflow.io.gfile.GFile")
@patch("tensorflow.io.write_graph")
def test_dirCreated(self, mock_write_graph, mock_gfile, mock_makedirs, mock_isfile):
    mock_gfile.return_value.read.return_value = b"mock serialized graph"
        
    # Run the function with a non-existing output directory
    reconstruct("input.pb", "non/existent/directory/output.pb")
        
    # Assertions
    mock_makedirs.assert_called_once_with("non/existent/directory", exist_ok=True)

@patch("os.path.isfile", return_value=False)
def test_missingFile(self, mock_isfile):
    with self.assertLogs(level="ERROR") as log:
        graph = reconstruct("invalid/path/to/input.pb", "output.pb")
        self.assertIsNone(graph)
        self.assertIn("Error: invalid/path/to/input.pb not found", log.output[0])
    return

