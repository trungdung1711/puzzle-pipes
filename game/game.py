import pygame
from state.grid import Grid
from util import Stack
from pygame import Surface
from .constant import *
from .grid import *
from .button import *


def ui(grid : 'Grid', actions : Stack ):
    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('puzzle pipe')

    # shallow copy
    action_list = actions.reversed()
    draw_grid(window, grid)
    draw_start_button(window)
    running(window, grid, action_list)


def running(window : 'Surface', grid : 'Grid', action_list : 'list'):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                location = clicked_pipe(pos)

                if BUTTON_RECT_FORWARD.collidepoint(event.pos):
                    start_button(window, grid, action_list)

                elif BUTTON_RECT_BACKWARD.collidepoint(event.pos):
                    reverse_button(window, grid, action_list)

                elif BUTTON_RECT_RIGHT.collidepoint(event.pos):
                    right_button(window, grid, action_list)

                elif BUTTON_RECT_LEFT.collidepoint(event.pos):
                    left_button(window, grid, action_list)
                    
                elif location:
                    right_rotate(grid, location)

        window.fill(WHITE)
        draw_grid(window, grid)
        draw_start_button(window)
        draw_reverse_button(window)
        draw_right_button(window)
        draw_left_button(window)
        pygame.display.flip()
    pygame.quit()
    

def clicked_pipe(location: 'tuple') -> 'tuple':
    x, y = location
    if (x >= 100 and x <= 500 and y >= 100 and y <= 500):
        row = int((y // CELL_SIZE) - 1)
        col = int((x // CELL_SIZE) - 1)
        return (row, col)
    return None