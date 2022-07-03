import unittest
import cv2
import numpy as np

from common import pp, make_matrix


class TestKernel(unittest.TestCase):
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

    def compare_multiplication(self, _xy, _x, _y):
        kernel_xy, kernel_x, kernel_y = [
            np.array(_xy) / 9,
            np.array(_x) / 3,
            np.array(_y) / 3
        ]
        grayImg = np.asanyarray(self.matrix, np.float32)
        dst_xy = TestKernel.filter(grayImg, kernel_xy)
        print("M**(XY)")
        pp(dst_xy)
        dst_x = TestKernel.filter(grayImg, kernel_x)
        print("M**X")
        pp(dst_x)
        dst_x_y = TestKernel.filter(dst_x, kernel_y)
        print("(M**X)**Y")
        pp(dst_x_y)
        TestKernel.__compare(dst_xy, dst_x_y)

    def test_Gaus(self):
        self.compare_multiplication(
            [[1, 1, 1], [1, 1, 1], [1, 1, 1]],
            [[1, 1, 1]],
            [[1], [1], [1]]
        )

    def test_Breakdown(self):
        self.compare_multiplication(
            [[15, 5, 10], [24, 8, 16], [12, 4, 8]],
            [[3, 1, 2]],
            [[5], [8], [4]]
        )


if __name__ == '__main__':
    unittest.main()
