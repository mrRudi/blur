import unittest
import cv2
import numpy as np

from .common import make_matrix, pp

GAUS = "gaus"
CUSTOM_BREAKDOWN = "breakdown"
IDENTITY = "identity"
X = "X"
Y = "Y"


class TestBasic(unittest.TestCase):
    def set_matrix(self, name, **options):
        self.matrix_rare = make_matrix(name, **options)
        self.matrix = np.asanyarray(self.matrix_rare, np.float32)

    def setUp(self):
        self.set_matrix("up")

        self.kernels = {}
        kernels = {
            GAUS: [[1/9, 1/9, 1/9], [1/9, 1/9, 1/9], [1/9, 1/9, 1/9]],
            CUSTOM_BREAKDOWN: [[5/3, 5/9, 10/9], [8/3, 8/9, 16/9], [4/3, 4/9, 8/9]],
            IDENTITY: [[0, 0, 0], [0, 1, 0], [0, 0, 0]],
        }
        for method in kernels:
            self.kernels[method] = np.array(kernels[method])

        self.breakdowns = {}
        breakdowns = {
            GAUS: {
                X: [[1/3, 1/3, 1/3]],
                Y: [[1/3], [1/3], [1/3]]
            },
            CUSTOM_BREAKDOWN: {
                X: [[1, 1/3, 2/3]],
                Y: [[5/3], [8/3], [4/3]]
            }
        }
        for method in breakdowns:
            self.breakdowns[method] = {}
            for key in breakdowns[method]:
                self.breakdowns[method][key] = np.array(
                    breakdowns[method][key])

    @staticmethod
    def filter(matrix, kernel):
        return cv2.filter2D(matrix, -1, kernel)

    @staticmethod
    def round(matrix, decimals=2):
        return np.round_(matrix, decimals)

    @staticmethod
    def compare_arrays(matrixA, matrixB):
        np.testing.assert_array_equal(
            TestBasic.round(matrixA),
            TestBasic.round(matrixB)
        )

    @staticmethod
    def step_filter(title, matrix, kernel):
        res = TestBasic.filter(matrix, kernel)
        print(title)
        pp(res)
        return res


def run():
    unittest.main()
