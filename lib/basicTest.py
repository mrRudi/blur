import unittest
import cv2
import numpy as np

from .common import make_matrix, pp
from .constant import kernels, breakdowns


class TestBasic(unittest.TestCase):
    def set_matrix(self, name, **options):
        self.matrix_rare = make_matrix(name, **options)
        self.matrix = np.asanyarray(self.matrix_rare, np.float32)

    def setUp(self):
        self.set_matrix("up")

        self.kernels = {}
        for method in kernels:
            self.kernels[method] = np.array(kernels[method])

        self.breakdowns = {}
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
