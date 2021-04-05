import numpy as np
from scramble import scramble
import random
import pygame
import sys
import time
from moves import Moves

pygame.init()
pygame.display.init

S_WIDTH = 1800
S_HEIGHT = 900

cube = np.zeros((6, 3, 3))

# Constants
# Colors
BLAC = (0, 0, 0)
YELLOW = (237, 231, 43)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
ORANGE = (255, 123, 0)
colors = (BLAC, YELLOW, BLUE, WHITE, GREEN, RED, ORANGE)

# Initializing various icons and resizing them to a 95 x 95 image
UP = pygame.image.load(r"Images\up_arrow.png")
UP = pygame.transform.scale(UP, (95, 95))
DOWN = pygame.image.load(r"Images\down_arrow.png")
DOWN = pygame.transform.scale(DOWN, (95, 95))
LEFT = pygame.image.load(r"Images\left_arrow.png")
LEFT = pygame.transform.scale(LEFT, (95, 95))
RIGHT = pygame.image.load(r"Images\right_arrow.png")
RIGHT = pygame.transform.scale(RIGHT, (95, 95))
FRONT = pygame.image.load(r"Images\turn_front.png")
FRONT = pygame.transform.scale(FRONT, (95, 95))
FRONT_INVERTED = pygame.image.load(
    r"Images\turn_front_inverted.png")
FRONT_INVERTED = pygame.transform.scale(FRONT_INVERTED, (95, 95))
FACE_UP = pygame.image.load(r"Images\face_top.png")
FACE_UP = pygame.transform.scale(FACE_UP, (95, 95))
FACE_BOT = pygame.image.load(r"Images\face_bot.png")
FACE_BOT = pygame.transform.scale(FACE_BOT, (95, 95))
FACE_RIGHT = pygame.image.load(
    r"Images\face_right.png")
FACE_RIGHT = pygame.transform.scale(FACE_RIGHT, (95, 95))
FACE_LEFT = pygame.image.load(r"Images\face_left.png")
FACE_LEFT = pygame.transform.scale(FACE_LEFT, (95, 95))


screen = pygame.display.set_mode(size=(S_WIDTH, S_HEIGHT))
screen.fill((100, 100, 100))


# drawing the UV index of the cube
def drawColors():
    for zAxis in range(6):
        for yAxis in range(3):
            for xAxis in range(3):
                if zAxis < 4:
                    rectPoints = (600 + (300*zAxis + xAxis * 100) + 3,
                                  (300 + yAxis*100) + 3, 95, 95)
                else:
                    rectPoints = (600 + (300 + xAxis * 100) + 3, 300 *
                                  ((zAxis-4)*2) + 100 * yAxis + 3, 95, 95)
                color = colors[cube[zAxis][yAxis][xAxis]]
                pygame.draw.rect(screen, color,
                                 rectPoints)


def drawFace(this_face):
    for yAxis in range(3):
        for xAxis in range(3):
            rectPoints = (100+100*xAxis + 3, 300 + 100*yAxis+3, 95, 95)
            color = colors[cube[zAxis][yAxis][xAxis]]
            pygame.draw.rect(screen, color,
                             rectPoints)


# drawing the buttons for the cube movement
def drawButtons():
    screen.blit(FRONT_INVERTED, (3, 203))
    screen.blit(FRONT, (403, 203))
    screen.blit(FACE_UP, (103, 103))
    screen.blit(FACE_BOT, (303, 103))
    screen.blit(FACE_LEFT, (103, 703))
    screen.blit(FACE_RIGHT, (303, 703))
    for i in range(3):
        if i != 1:
            screen.blit(UP,  (100+100*i+3, 200+3))
            screen.blit(RIGHT, (400+3, 300+100*i+3))
            screen.blit(DOWN, (100+100*i+3, 600+3))
            screen.blit(LEFT, (3, 300+100*i+3))


# checing where the mouse button was clicked and performing the moves accordingly
def doMove(xPos, yPos, this_face):

    global face
    # getting the adjacent faces for the current face showing
    top, right, bot, left = Moves.adjacentFaces(this_face)

    # checking if the center of any face in the UV index is clicked and showing that face accordingly
    if 700 < xPos < 800 and 400 < yPos < 500:
        face = 0
    if 1000 < xPos < 1100 and 400 < yPos < 500:
        face = 1
    if 1300 < xPos < 1400 and 400 < yPos < 500:
        face = 2
    if 1600 < xPos < 1700 and 400 < yPos < 500:
        face = 3
    if  1000 < xPos < 1100 and 100 < yPos < 200:
        face = 4
    if 1000 < xPos < 1100 and 700 < yPos < 800:
        face = 5

    # front turn
    if (xPos > 400 and xPos < 500 and yPos > 200 and yPos < 300):
        Moves.turnFront(this_face, cube)
    if (xPos > 0 and xPos < 100 and yPos > 200 and yPos < 300):
        Moves.turnFront(this_face, cube, True)

    # top row
    if (xPos > 100 and xPos < 200 and yPos > 200 and yPos < 300):
        Moves.turnLeft(this_face, cube)
    if (xPos > 300 and xPos < 400 and yPos > 200 and yPos < 300):
        Moves.turnRight(this_face, cube)

    # bot row:
    if (xPos > 100 and xPos < 200 and yPos > 600 and yPos < 700):
        Moves.turnLeft(this_face, cube, True)
    if (xPos > 300 and xPos < 400 and yPos > 600 and yPos < 700):
        Moves.turnRight(this_face, cube, True)

    # right row:
    if (xPos > 400 and xPos < 500 and yPos > 300 and yPos < 400):
        Moves.turnTop(this_face, cube, True)
    if (xPos > 400 and xPos < 500 and yPos > 500 and yPos < 600):
        Moves.turnBot(this_face, cube)

    # left row:
    if (xPos > 0 and xPos < 100 and yPos > 300 and yPos < 400):
        Moves.turnTop(this_face, cube)
    if (xPos > 0 and xPos < 100 and yPos > 500 and yPos < 600):
        Moves.turnBot(this_face, cube, True)

    # turn faces:
    if (xPos > 100 and xPos < 200 and yPos > 100 and yPos < 200):
        face = top
    if (xPos > 300 and xPos < 400 and yPos > 100 and yPos < 200):
        face = bot
    if (xPos > 100 and xPos < 200 and yPos > 700 and yPos < 800):
        face = left
    if (xPos > 300 and xPos < 400 and yPos > 700 and yPos < 800):
        face = right


# drawing the lines on the screen
def drawLines():
    for i in range(18):
        pygame.draw.line(screen, (50, 50, 50),
                         (100*i, 0), (100*i, 900), width=3)
    for i in range(10):
        pygame.draw.line(screen, (50, 50, 50), (0, 100*i),
                         (1800, 100*i), width=3)


face = 1
running = True

# scrambling the cube using the scramble function in scramble.oy file
scramble(cube)

# printin the cube for debugging purposes
print(cube)
drawButtons()
drawLines()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(),
            sys.exit()

        if event.type == pygame.MOUSEBUTTONUP:
            mouseX = event.pos[0]
            mouseY = event.pos[1]
            doMove(mouseX, mouseY, face)

        drawColors()
        drawFace(face)

        pygame.display.update()
