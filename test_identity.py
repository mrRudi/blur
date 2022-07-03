import unittest
import cv2
import numpy as np

from common import pp, make_matrix


class TestIdentity(unittest.TestCase):
    def setUp(self):
        self.matrix_up = make_matrix("up")
        self.matrix_1 = make_matrix("1")
        self.matrix_rand = make_matrix("rand")
        self.matrix = self.matrix_up

    def filter(matrix, kernel):
        return cv2.filter2D(matrix, -1, kernel)

    def __compare(matrixA, matrixB):
        np.testing.assert_array_equal(
            np.round_(matrixA, 2),
            np.round_(matrixB, 2)
        )

    def step(name, matrix, kernel):
        res = TestIdentity.filter(matrix, kernel)
        print(name)
        pp(res)
        return res

    def compare_multiplication(self, xy,  reverse_xy):
        kernel = np.array(xy)
        kernel_reverse = np.array(reverse_xy)
        original = np.asanyarray(self.matrix, np.float32)
        print("\noriginal")
        pp(original)
        changed = TestIdentity.step("changed", original, kernel)
        reverse = TestIdentity.step("reverse", changed, kernel_reverse)
        TestIdentity.__compare(original, reverse)

    def test_1(self):
        self.compare_multiplication(
            [[0, 0, 0], [0, 1, 0], [0, 0, 0]],
            [[0, 0, 0], [0, 1, 0], [0, 0, 0]],
        )

    def test_Reverse(self):
        self.compare_multiplication(
            [[0, 0, 0], [0, 2, 0], [0, 0, 0]],
            [[0, 0, 0], [0, 1/2, 0], [0, 0, 0]],
        )


if __name__ == '__main__':
    unittest.main()
