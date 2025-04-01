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

    def test_drawBoxes(self):
        capture = np.zeros((480, 640, 3), dtype=np.uint8)
        scores = [0.8]
        boxes = [[0.1, 0.1, 0.2, 0.2]]
        lbl_map = {1: "plastic"}
        class_map = {1: "Non-Biodegradable"}
        classes = [1]

        pos, count, label, classification = distInf.drawBoxes(
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
            
    
    def test_home_position_resets_servos(self):
        mock_braccio = MagicMock()
        mock_braccio.servo_movement = MagicMock()
        mock_braccio.home_position()
        mock_braccio.servo_movement.assert_called()

    def test_move_single_joint_bounds(self):
        mock_braccio = MagicMock()
        mock_braccio.s5 = 170
        mock_braccio.servo_movement = MagicMock()
        distInf.move_single_joint(mock_braccio, ServoMotor.S5, 5)
        self.assertTrue(mock_braccio.servo_movement.called)

    def test_vector_transform_with_ik(self):
        vector = np.array([100, 150, 20])
        result = distInf.Inverse_kinematics.move(vector)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 5)
        self.assertIsInstance(result[4], np.ndarray)
        
    def test_read_feedback_format(self):
        mock_braccio = MagicMock()
        mock_braccio.s1 = 10
        mock_braccio.s2 = 20
        mock_braccio.s3 = 30
        mock_braccio.s4 = 40
        mock_braccio.s5 = 50
        mock_braccio.s6 = 60

        feedback = distInf.read_feedback(mock_braccio)
        self.assertIsInstance(feedback, str)
        self.assertIn("Servo positions", feedback)
        for value in [10, 20, 30, 40, 50, 60]:
            self.assertIn(str(value), feedback)

if __name__ == '__main__':
    unittest.main()
