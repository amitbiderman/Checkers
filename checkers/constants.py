import pygame

"""
* Constant values for the checkers game
* Width and height of the game board
* Number of rows and columns
* Each square will have the size of the width of the board integer divided by the number of columns
* Defining the colors of the pieces according the RGB standards
"""

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)

CROWN = pygame.transform.scale(pygame.image.load('checkers/asserts/crown.png'), (44, 25))
