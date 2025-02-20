import pygame
from pygame import Surface
from .constant import *
from util import Stack
from state.grid import Grid
from .grid import right_rotate
from .grid import draw_grid
from .grid import left_rotate


current_action_index = 0


def draw_start_button(window : 'Surface'):
    image = pygame.transform.scale(IMAGES['BF'], (BUTTON_SIZE, BUTTON_SIZE))
    window.blit(image, BUTTON_RECT_FORWARD)


def draw_reverse_button(window : 'Surface'):
    image = pygame.transform.scale(IMAGES['BB'], (BUTTON_SIZE, BUTTON_SIZE))
    window.blit(image, BUTTON_RECT_BACKWARD)


def draw_right_button(window : 'Surface'):
    image = pygame.transform.scale(IMAGES['Right'], (BUTTON_SIZE, BUTTON_SIZE))
    window.blit(image, BUTTON_RECT_RIGHT)


def draw_left_button(window : 'Surface'):
    image = pygame.transform.scale(IMAGES['Left'], (BUTTON_SIZE, BUTTON_SIZE))
    window.blit(image, BUTTON_RECT_LEFT)


def start_button(window : 'Surface', grid : 'Grid', action_list : 'list'):
    global current_action_index
    for index in range(current_action_index, len(action_list)):
        right_rotate(grid, action_list[index])
        window.fill(WHITE)
        draw_grid(window, grid)
        draw_step(window)
        pygame.display.flip()
        pygame.time.delay(500)
        current_action_index += 1


def reverse_button(window : 'Surface', grid : 'Grid', action_list : 'list'):
    global current_action_index
    while current_action_index > 0:
        left_rotate(grid, action_list[current_action_index - 1])
        window.fill(WHITE)
        draw_grid(window, grid)
        draw_step(window)
        pygame.display.flip()
        pygame.time.delay(500)
        current_action_index -= 1


def right_button(window : 'Surface', grid : 'Grid', action_list : 'list'):
    global current_action_index
    if current_action_index > len(action_list) - 1 or current_action_index < 0:
        return
    right_rotate(grid, action_list[current_action_index])
    current_action_index += 1

    window.fill(WHITE)
    draw_grid(window, grid)
    draw_left_button(window)
    draw_right_button(window)
    draw_start_button(window)
    draw_reverse_button(window)
    draw_step(window)
    pygame.display.flip()
    pygame.time.delay(500)


def left_button(window : 'Surface', grid : 'Grid', action_list : 'list'):
    global current_action_index
    if current_action_index > len(action_list) or current_action_index < 1:
        return
    left_rotate(grid, action_list[current_action_index - 1])
    current_action_index -= 1

    window.fill(WHITE)
    draw_grid(window, grid)
    draw_left_button(window)
    draw_right_button(window)
    draw_start_button(window)
    draw_reverse_button(window)
    draw_step(window)
    pygame.display.flip()
    pygame.time.delay(500)


def draw_step(window : 'Surface'):
    font = pygame.font.Font(None, 30)
    step = font.render('Step: ' + str(current_action_index), True, BLUE)
    window.blit(step, STEP_LOCATION)