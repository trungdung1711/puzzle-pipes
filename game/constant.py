import pygame


WIDTH, HEIGHT = 600, 600
GRID_SIZE = 4
CELL_SIZE = 100
BUTTON_SIZE = 50
BUTTON_RECT_BACKWARD = pygame.Rect(25, 525, BUTTON_SIZE, BUTTON_SIZE)
BUTTON_RECT_FORWARD = pygame.Rect(525, 525, BUTTON_SIZE, BUTTON_SIZE)
BUTTON_RECT_LEFT = pygame.Rect(200, 525, BUTTON_SIZE, BUTTON_SIZE)
BUTTON_RECT_RIGHT = pygame.Rect(350, 525, BUTTON_SIZE, BUTTON_SIZE)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (229, 229, 16)
BLUE = (24, 24, 129)
STEP_LOCATION = (100, 50)
IMAGES = {
    'D' : pygame.image.load('./game/images/D.PNG'),
    'L' : pygame.image.load('./game/images/L.PNG'),
    'S' : pygame.image.load('./game/images/S.PNG'),
    'T' : pygame.image.load('./game/images/T.PNG'),
    'BF' : pygame.image.load('./game/images/forward.png'),
    'BB' : pygame.image.load('./game/images/backward.png'),
    'Left' : pygame.image.load('./game/images/left.png'),
    'Right' : pygame.image.load('./game/images/right.png')
}