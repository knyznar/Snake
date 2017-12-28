import random
from MatrixBuilder import *

def putApple(matrix):
    while True:
        appleRow = random.randrange(len(matrix))
        appleColumn = random.randrange(len(matrix[appleRow]))
        if matrix[appleRow][appleColumn] == MapState.EMPTY:
            break

    matrix[appleRow][appleColumn] = MapState.APPLE
