
import unittest
from unittest.mock import patch, MagicMock, mock_open
import numpy as np
import pygame
import StereoVision.distInf as distInf
from interface import *

class TestDistInf(unittest.TestCase):

    def test_checkInBounds(self):
        values = [20, 100, 100, 100, 100, 100, 50]
        uBound = [30, 180, 165, 180, 180, 180, 73]
        lBound = [10, 0, 15, 0, 0, 0, 10]
        result = distInf.checkInBounds(values, uBound, lBound)
        self.assertEqual(result, values)

    def test_checkInBounds_outof_bounds(self):
        values = [-100, 300, 5, -1, 250, -20, 100]
        uBound = [30, 180, 165, 180, 180, 180, 73]
        lBound = [10, 0, 15, 0, 0, 0, 10]
        expected = [10, 180, 15, 0, 180, 0, 73]
        result = distInf.checkInBounds(values, uBound, lBound)
        self.assertEqual(result, expected)

    def test_jiggle(self):
        mock_braccio = MagicMock()
        mock_braccio.s2 = 40
        mock_braccio.s3 = 180
        mock_braccio.s4 = 0
        mock_braccio.s5 = 180
        mock_braccio.s6 = 60

        distInf.jiggle(mock_braccio, baseServo=90)
        self.assertTrue(mock_braccio.servo_movement.called)

    def test_loadLabelMap(self):
        mock_file_content = """
                            0 background
                            1 plastic
                            16 banana_peel
                            """
        with patch("builtins.open", mock_open(read_data=mock_file_content)):
            label_map, classification_map = distInf.loadLabelMap("fake_path.txt")

        self.assertEqual(label_map[1], "plastic")
        self.assertEqual(classification_map[1], "Non-Biodegradable")
        self.assertEqual(classification_map[16], "Biodegradable")

    def test_preProcess(self):
        frame = np.ones((480, 640, 3), dtype=np.uint8) * 255
        result = distInf.preProcess(frame, 300, 300)
        self.assertEqual(result.shape, (1, 300, 300, 3))
        self.assertEqual(result.dtype, np.uint8)

    def test_draw_boxes(self):
        capture = np.zeros((480, 640, 3), dtype=np.uint8)
        scores = [0.8]
        boxes = [[0.1, 0.1, 0.2, 0.2]]
        lbl_map = {1: "plastic"}
        class_map = {1: "Non-Biodegradable"}
        classes = [1]

        pos, count, label, classification = distInf.draw_boxes(
            capture, scores, boxes, lbl_map, class_map, classes
        )

        self.assertEqual(count, 1)
        self.assertEqual(label, "plastic")
        self.assertEqual(classification, "Non-Biodegradable")
        self.assertIsInstance(pos, tuple)

    def test_display_text(self):
        pygame.init()
        distInf.screen = pygame.display.set_mode((300, 300))
        try:
            distInf.display_text("Hello", 10, 10)
        except Exception as e:
            self.fail(f"display_text raised an exception: {e}")
        finally:
            pygame.quit()
    
    def test_robot_servo_bounds(self):
        mock_braccio = MagicMock()
        mock_braccio.servo_movement = MagicMock()
        mock_braccio.s2 = 90
        mock_braccio.s3 = 90
        mock_braccio.s4 = 90
        mock_braccio.s5 = 90
        mock_braccio.s6 = 90

        baseServo = 90
        distInf.jiggle(mock_braccio, baseServo)

        self.assertTrue(mock_braccio.servo_movement.call_count >= 3)     
            

if __name__ == '__main__':
    unittest.main()
