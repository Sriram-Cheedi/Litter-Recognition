import unittest
import serial

from main import checkInBounds 

def test_inBounds():
    upper_bounds = [30, 180, 165, 180, 180, 180, 73]
    lower_bounds = [10, 0, 15, 0, 0, 0, 10]
    testValues = [8, 190, 15, 56, 85, 181, 72]
    assert checkInBounds(testValues, upper_bounds, lower_bounds) == [10, 180, 15, 56, 85, 180, 72]
