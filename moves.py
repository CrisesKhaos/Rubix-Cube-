import numpy as np


class Moves:

    # getting the adjacent faces of the face argument and returing them
    @staticmethod
    def adjacentFaces(face):
        if face == 0:     # yellow
            top = 4
            bot = 5
            right = 1
            left = 3
        elif face == 1:   # blue
            top = 4
            bot = 5
            right = 2
            left = 0
        elif face == 2:   # white
            top = 4
            bot = 5
            right = 3
            left = 1
        elif face == 3:  # green
            top = 4
            bot = 5
            left = 2
            right = 0
        elif face == 4:  # red
            top = 3
            bot = 1
            right = 2
            left = 0
        elif face == 5:   # orange
            top = 1
            bot = 3
            right = 2
            left = 0
        return(top, right, bot, left)

# turning the front of the face
    @staticmethod
    def turnFront(face, cube, inverted=False):
        top, right, bot, left = Moves.adjacentFaces(face)
        # checking if the move is inveted
        if not inverted:
            inv = 1
        else:
            inv = 3
        # idek whats going on here😐
        for turns in range(inv):
            cube[face] = np.transpose(cube[face])
            cube[face] = np.flip(cube[face], axis=1)

            if face == 0:
                for flip in range(3):
                    cube[top] = np.transpose(cube[top])
                    cube[top] = np.flip(cube[top], axis=1)
                cube[bot] = np.transpose(cube[bot])
                cube[bot] = np.flip(cube[bot], axis=1)
                for i in range(3):
                    temp = cube[left][2-i][2]
                    cube[left][2-i][2] = cube[bot][0][2-i]
                    temp1 = cube[top][2][i]
                    cube[top][2][i] = temp
                    temp = cube[right][i][0]
                    cube[right][i][0] = temp1
                    cube[bot][0][2-i] = temp
                cube[top] = np.transpose(cube[top])
                cube[top] = np.flip(cube[top], axis=1)
                for flip in range(3):
                    cube[bot] = np.transpose(cube[bot])
                    cube[bot] = np.flip(cube[bot], axis=1)

            elif face == 1:
                for i in range(3):
                    temp = cube[left][2-i][2]
                    cube[left][2-i][2] = cube[bot][0][2-i]
                    temp1 = cube[top][2][i]
                    cube[top][2][i] = temp
                    temp = cube[right][i][0]
                    cube[right][i][0] = temp1
                    cube[bot][0][2-i] = temp

            elif face > 1 and face < 4:
                for flip in range(face - 1):
                    cube[top] = np.transpose(cube[top])
                    cube[top] = np.flip(cube[top], axis=1)
                for flip in range(4-(face-1)):
                    cube[bot] = np.transpose(cube[bot])
                    cube[bot] = np.flip(cube[bot], axis=1)
                for i in range(3):
                    temp = cube[left][2-i][2]
                    cube[left][2-i][2] = cube[bot][0][2-i]
                    temp1 = cube[top][2][i]
                    cube[top][2][i] = temp
                    temp = cube[right][i][0]
                    cube[right][i][0] = temp1
                    cube[bot][0][2-i] = temp
                for flip in range(face - 1):
                    cube[bot] = np.transpose(cube[bot])
                    cube[bot] = np.flip(cube[bot], axis=1)
                for flip in range(4-(face-1)):
                    cube[top] = np.transpose(cube[top])
                    cube[top] = np.flip(cube[top], axis=1)

            elif face == 4:
                for i in range(3):
                    temp = cube[left][0][i]
                    cube[left][0][i] = cube[bot][0][i]
                    temp1 = cube[top][0][i]
                    cube[top][0][i] = temp
                    temp = cube[right][0][i]
                    cube[right][0][i] = temp1
                    cube[bot][0][i] = temp

            else:
                for i in range(3):
                    temp = cube[left][2][i]
                    cube[left][2][i] = cube[bot][2][i]
                    temp1 = cube[top][2][i]
                    cube[top][2][i] = temp
                    temp = cube[right][2][i]
                    cube[right][2][i] = temp1
                    cube[bot][2][i] = temp

    @staticmethod
    def turnRight(face, cube, inverted=False):
        _, right, _, _ = Moves.adjacentFaces(face)
        Moves.turnFront(right, cube, inverted)

    @staticmethod
    def turnLeft(face, cube, inverted=False):
        _, _, _, left = Moves.adjacentFaces(face)
        Moves.turnFront(left, cube, inverted)

    @staticmethod
    def turnTop(face, cube, inverted=False):
        top, _, _, _ = Moves.adjacentFaces(face)
        Moves.turnFront(top, cube, inverted)

    @staticmethod
    def turnBot(face, cube, inverted=False):
        _, _, bot, _,  = Moves.adjacentFaces(face)
        Moves.turnFront(bot, cube, inverted)
