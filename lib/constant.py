import enum

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


class GAUS(enum.Enum):
    g9 = "gaus 1/9"


class CUSTOM(enum.Enum):
    breakdown1 = "breakdown 1"


class IDENTITY(enum.Enum):
    identity1 = "identity 1"


def make_circle(center, border):
    return [[border, border, border], [border, center, border], [border, border, border]]


def make_fill(cell):
    return make_circle(cell, cell)


def make_shapen(center):
    return [[0, -1, 0], [-1, center, -1], [0, -1, 0]]


kernels = {
    GAUS.g9: make_fill(1/9),
    CUSTOM.breakdown1: [[5/3, 5/9, 10/9], [8/3, 8/9, 16/9], [4/3, 4/9, 8/9]],
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
    GAUS.g9: {
        X: [[1/3, 1/3, 1/3]],
        Y: [[1/3], [1/3], [1/3]]
    },
    CUSTOM.breakdown1: {
        X: [[1, 1/3, 2/3]],
        Y: [[5/3], [8/3], [4/3]]
    }
}
