import unittest
import serial

from interface import *

def test_inBounds():
    uBounds = [30, 180, 165, 180, 180, 180, 73]
    lBounds = [10, 0, 15, 0, 0, 0, 10]
    testValues = [8, 190, 15, 56, 85, 181, 72]
    assert checkInBounds(testValues, uBounds, lBounds) == [10, 180, 15, 56, 85, 180, 72]

    testValues = [31, -1, 166, 181, 181, -1, 9]
    assert checkInBounds(testValues, uBounds, lBounds) == [30, 0, 165, 180, 180, 0, 10]

def test_all():
    assert True

def test_feature():
    assert True
