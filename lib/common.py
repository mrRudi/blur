from .constant import make_random, make_arithmetic_progression, make_full


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
        return make_full(R, 1)
    if type == "rand":
        return make_random(R, options.get('Min', 1), options.get('Max', 10))
    if type == "up":
        return make_arithmetic_progression(R)
    raise Exception("setting type is required")
