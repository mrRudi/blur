import random


def pp(matrix, space=3, divider=",", border="|", end=True):
    """
    beautiful print matrices
        matrix: Y x X
        default space [space]xxxx[dot][number] == 3 simbols
    """
    cellFormat = len(str(round(max(map(max, matrix))))) + space

    for mY in range(len(matrix)):
        ss = divider.join(
            ['{:{cF}.1f}'.format(matrix[mY][mX], cF=cellFormat) for mX in range(len(matrix[mY]))])
        print(border + ss + border)
    if end:
        print('')
