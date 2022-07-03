import random
import enum
import numpy as np

X = "X"
Y = "Y"


class SHARPEN(enum.Enum):
    center4 = "sharpen 4"
    center5 = "sharpen 5"


class RIDGE_DETECTION(enum.Enum):
    rd_mns1_7 = "RidgeDetection -1 7"
    rd_mns1_8 = "RidgeDetection -1 8"
    rd_mns1_9 = "RidgeDetection -1 9"
    rd_mns2_10 = "RidgeDetection -2 10"
    rd_mns1div9_10 = "RidgeDetection -1/9 1"


class BLUR(enum.Enum):
    box_3x3_div9 = "gaus 3x3 1/9"
    gaus_3x3_div16 = "gaus 3x3 1/16"
    gaus_5x5_div256 = "gaus 5x5 1/256"
    gaus_5x5_dot04 = "gaus 5x5 0.04"


class CUSTOM(enum.Enum):
    breakdown1 = "breakdown 1"
    emboss1 = "emboss 1"
    horizontal_direction1 = "horizontal direction 1"
    horizontal_direction2 = "horizontal direction 2"
    vertical_direction1 = "vertical direction 1"
    vertical_direction2 = "vertical direction 2"
    unsharp_5x5_mnsdiv256 = "unsharp 5x5 -1/256"


class IDENTITY(enum.Enum):
    identity1 = "identity 1"


def make_circle(center, border):
    return [[border, border, border], [border, center, border], [border, border, border]]


def make_shapen(center):
    return [[0, -1, 0], [-1, center, -1], [0, -1, 0]]


def make_horizontal_3x3_direction(a, b):
    return [[-a, 0, a], [-b, 0, b], [-a, 0, a]]


def make_vertical_3x3_direction(a, b):
    return [[-a, -b, -a], [0, 0, 0], [a, b, a]]


def make_arithmetic_progression(n):
    return [[1+x+y*n for x in range(n)] for y in range(n)]


def make_random(n, min, max):
    return [[random.randint(min, max) for _ in range(n)] for _ in range(n)]


def make_full(n, val):
    return np.full((n, n), val)


kernels = {
    BLUR.box_3x3_div9: make_full(3, 1/9),
    BLUR.gaus_3x3_div16: [
        [1/16, 2/16, 1/16],
        [2/16, 4/16, 2/16],
        [1/16, 2/16, 1/16]
    ],
    BLUR.gaus_5x5_div256: [
        [1/256, 4/256, 6/256, 4/256, 1/256],
        [4/256, 16/256, 24/256, 16/256, 4/256],
        [6/256, 24/256, 36/256, 24/256, 6/256],
        [4/256, 16/256, 24/256, 16/256, 4/256],
        [1/256, 4/256, 6/256, 4/256, 1/256],
    ],
    BLUR.gaus_5x5_dot04: make_full(5, 0.04),

    CUSTOM.breakdown1: [
        [15/9, 5/9, 10/9],
        [24/9, 8/9, 16/9],
        [12/9, 4/9, 8/9]
    ],

    CUSTOM.unsharp_5x5_mnsdiv256: [
        [-1/256, -4/256, -6/256, -4/256, -1/256],
        [-4/256, -16/256, -24/256, -16/256, -4/256],
        [-6/256, -24/256, 476/256, -24/256, -6/256],
        [-4/256, -16/256, -24/256, -16/256, -4/256],
        [-1/256, -4/256, -6/256, -4/256, -1/256],
    ],

    CUSTOM.emboss1: [
        [-2, -1, 0],
        [-1, 1, 1],
        [0, 1, 2]
    ],

    CUSTOM.horizontal_direction1: make_horizontal_3x3_direction(1, 2),
    CUSTOM.horizontal_direction2: make_horizontal_3x3_direction(3, 10),
    CUSTOM.vertical_direction1: make_vertical_3x3_direction(1, 2),
    CUSTOM.vertical_direction2: make_vertical_3x3_direction(3, 10),

    IDENTITY.identity1: make_circle(1, 0),

    SHARPEN.center4: make_shapen(4),
    SHARPEN.center5: make_shapen(5),

    RIDGE_DETECTION.rd_mns1_7: make_circle(7, -1),
    RIDGE_DETECTION.rd_mns1_8: make_circle(8, -1),
    RIDGE_DETECTION.rd_mns1_9: make_circle(9, -1),
    RIDGE_DETECTION.rd_mns2_10: make_circle(10, -2),
    RIDGE_DETECTION.rd_mns1div9_10: make_circle(1, -1/9)
}

breakdowns = {
    BLUR.box_3x3_div9: {
        X: [[1/3, 1/3, 1/3]],
        Y: [
            [1/3],
            [1/3],
            [1/3]
        ]
    },
    CUSTOM.breakdown1: {
        X: [[1, 1/3, 2/3]],
        Y: [
            [5/3],
            [8/3],
            [4/3]
        ]
    }
}
