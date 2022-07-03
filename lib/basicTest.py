import unittest
import cv2
import enum
import numpy as np

from .common import make_matrix, pp


class SHARPEN(enum.Enum):
    center4 = "sharpen 4"
    center5 = "sharpen 5"


class RIDGE_DETECTION(enum.Enum):
    rd_mns1_7 = "RidgeDetection -1 7"
    rd_mns1_8 = "RidgeDetection -1 8"
    rd_mns1_9 = "RidgeDetection -1 9"
    rd_mns2_10 = "RidgeDetection -2 10"
    rd_mns1div9_10 = "RidgeDetection -1/9 1"


class GAUS(enum.Enum):
    g9 = "gaus 1/9"


class CUSTOM(enum.Enum):
    breakdown1 = "breakdown 1"


class IDENTITY(enum.Enum):
    identity1 = "identity 1"


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
            GAUS.g9: [[1/9, 1/9, 1/9], [1/9, 1/9, 1/9], [1/9, 1/9, 1/9]],
            CUSTOM.breakdown1: [[5/3, 5/9, 10/9], [8/3, 8/9, 16/9], [4/3, 4/9, 8/9]],
            IDENTITY.identity1: [[0, 0, 0], [0, 1, 0], [0, 0, 0]],
            SHARPEN.center4: [[0, -1, 0], [-1, 4, -1], [0, -1, 0]],
            SHARPEN.center5: [[0, -1, 0], [-1, 5, -1], [0, -1, 0]],
            RIDGE_DETECTION.rd_mns1_7: [[-1, -1, -1], [-1, 7, -1], [-1, -1, -1]],
            RIDGE_DETECTION.rd_mns1_8: [[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]],
            RIDGE_DETECTION.rd_mns1_9: [[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]],
            RIDGE_DETECTION.rd_mns2_10: [[-2, -2, -2], [-2, 10, -2], [-2, -2, -2]],
            RIDGE_DETECTION.rd_mns1div9_10: [[-1/9, -1/9, -1/9], [-1/9, 1, -1/9], [-1/9, -1/9, -1/9]],

        }
        for method in kernels:
            self.kernels[method] = np.array(kernels[method])

        self.breakdowns = {}
        breakdowns = {
            GAUS.g9: {
                X: [[1/3, 1/3, 1/3]],
                Y: [[1/3], [1/3], [1/3]]
            },
            CUSTOM.breakdown1: {
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
    def step_filter(title, matrix, kernel, show=True):
        res = TestBasic.filter(matrix, kernel)
        if show:
            print(title)
            pp(res)
        return res

    @staticmethod
    def deviation(matrixA, matrixB, show=True):
        bias = np.absolute(TestBasic.round(matrixA) - TestBasic.round(matrixB))
        if show:
            pp(bias)
        return bias


def run():
    unittest.main()
