# Dependency Requirements:
# Dependencies from Colab (tf, keras, protobuf etc)
# Distro
# sudo apt-get dist-upgrade
# ------------------------------------
# Tensorflow
# sudo apt-get install libatlas-base-dev (needed for tf)
# pip3 install tensorflow (version from colab)
# sudo pip3 install pillow lxml jupyter matplotlib cython
# sudo apt-get install python-tk
# ------------------------------------
# OpenCV
# sudo apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev
# sudo apt-get install libavcodec-dev libavformat-dev libwscale-dev lib4l-dev
# sudo apt-get install libxvidcore-dev libx264-dev
# sudo apt-get install qt4-dev-tools
# sudo apt-get libatlas-base-dev
# pip3 install opencv-python


# Unsure
# They install the tensorflow models github
# and point the python path at it
# Then they install a .tar.gz model from the model library and get the .pb files from there

# Code borrowed from https://github.com/EdjeElectronics/TensorFlow-Object-Detection-on-the-Raspberry-Pi


# Import packages and utilities
import os
import cv2
import numpy as np
from picamera.array import PiRGBArray
from piCamera import PiCamera
import tensorflow as tf
import argparse
import sys
from utils import label_map_util
from utils import visualization_utils as vis_util

IWidth = 1280
IHeight = 720
CamType = 'piCamera2'

Model = 'ssd_mobilenet_v2_taco_2018_03_29'



# TWO OPTIONS
# 1) Adapt code found at link
# 2) Adapt prewritten code and take frames and pass into detect

