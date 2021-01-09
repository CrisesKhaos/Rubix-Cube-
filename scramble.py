import numpy as np
import random
from moves import Moves


def scramble(tempcube):
    # assigning the colors to the array of zeroes
    for i in range(6):
        for j in range(3):
            for k in range(3):
                tempcube[i][j][k] = i + 1

    # scrambling the array by turning random faces
    for i in range(20):
        face = random.randrange(0, 6)
        Moves.turnFront(face, tempcube)


'''
    for i in range(6):
        for j in range(3):
            for k in range(3):
                if (j == 1 and k == 1):
                    tempcube[i][j][k] = i + 1
                else:
                    while True:
                        a = random.randrange(6)
                        b = random.randrange(3)
                        c = random.randrange(3)
                        if (b != 1 and c != 1):
                            break
                    temp = tempcube[i][j][k]
                    tempcube[i][j][k] = tempcube[a][b][c]
                    tempcube[a][b][c] = temp

    return tempcube
'''
