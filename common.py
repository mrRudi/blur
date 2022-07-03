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


def make_matrix(type, **options):
    R = options.get('R', 4)
    if type == "1":
        return [[1 for _ in range(R)] for _ in range(R)]
    if type == "rand":
        Min = options.get('Min', 1)
        Max = options.get('Max', 10)
        return [[random.randint(Min, Max) for _ in range(R)] for _ in range(R)]
    if type == "up":
        return [[1+x+y*R for x in range(R)] for y in range(R)]
    raise Exception("setting type is required")
