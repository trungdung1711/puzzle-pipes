import pygame
import sys
from state.grid import Grid
from state.pipe import Pipe
from state.type import PipeType

WIDTH, HEIGHT = 600, 600
GRID_SIZE = 4
CELL_SIZE = 100
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
IMAGES = {
    'D' : pygame.image.load('./pipes/D.PNG'),
    'L' : pygame.image.load('./pipes/L.PNG'),
    'S' : pygame.image.load('./pipes/S.PNG'),
    'T' : pygame.image.load('./pipes/T.PNG')
}


pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('puzzle pipe')
clock = pygame.time.Clock()


def display(grid : 'Grid'):
    draw_grid(grid)
    running(grid)


def draw_grid(grid : 'Grid'):
    for x in range(100, 500, CELL_SIZE):
        for y in range(100, 500, CELL_SIZE):
            location = int((x / 100)) - 1, int((y / 100) - 1)
            pipe = grid.get_pipe(location)
            image = pygame.transform.rotate(pygame.transform.scale(get_image(pipe), (CELL_SIZE, CELL_SIZE)), -90 * pipe.get_direction().value)
            window.blit(image, (y, x, CELL_SIZE, CELL_SIZE))


def running(grid : 'Grid'):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                location = clicked_pipe(pos)
                if location:
                    rotate(grid, location)
                    

        window.fill(WHITE)
        draw_grid(grid)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
    sys.exit()


def get_image(pipe : 'Pipe'):
    if pipe.get_type() == PipeType.D:
        return IMAGES['D']
    elif pipe.get_type() == PipeType.L:
        return IMAGES['L']
    elif pipe.get_type() == PipeType.S:
        return IMAGES['S']
    else:
        return IMAGES['T']
    

def clicked_pipe(location: 'tuple') -> 'tuple':
    x, y = location
    if (x >= 100 and x <= 500 and y >= 100 and y <= 500):
        row = int((y // CELL_SIZE) - 1)
        col = int((x // CELL_SIZE) - 1)
        return (row, col)
    return None


def rotate(grid: 'Grid', location : 'tuple'):
    grid.get_pipe(location).change_direction()