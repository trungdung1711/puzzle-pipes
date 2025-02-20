import pygame
from pygame import Surface
from .constant import *
from state.grid import Grid
from state.type import PipeType
from state.pipe import Pipe


def draw_grid(window : 'Surface', grid : 'Grid'):
    for x in range(100, 500, CELL_SIZE):
        for y in range(100, 500, CELL_SIZE):
            location = int((x / 100)) - 1, int((y / 100) - 1)
            pipe = grid.get_pipe(location)
            image = pygame.transform.rotate(pygame.transform.scale(get_image(pipe), (CELL_SIZE, CELL_SIZE)), -90 * pipe.get_direction().value)
            window.blit(image, (y, x, CELL_SIZE, CELL_SIZE))


def get_image(pipe : 'Pipe'):
    if pipe.get_type() == PipeType.D:
        return IMAGES['D']
    elif pipe.get_type() == PipeType.L:
        return IMAGES['L']
    elif pipe.get_type() == PipeType.S:
        return IMAGES['S']
    else:
        return IMAGES['T']
    

def right_rotate(grid: 'Grid', location : 'tuple'):
    grid.get_pipe(location).right_rotate()


def left_rotate(grid : 'Grid', location : 'tuple'):
    grid.get_pipe(location).left_rotate()