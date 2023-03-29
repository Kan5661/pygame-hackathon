import pygame as py
import time
import sys
from utils import *

py.init()
# Initializing the screen and clock
screen_width = 800
screen_height = 500
screen = py.display.set_mode((screen_width, screen_height))
clock = py.time.Clock()
# Function to insert the player on the screen


def draw_player(x_pos, y_pos):
    global x, y, delta_y
    x += delta_x
    y += delta_y
    player_rect = py.image.load('./assets/player_assets/standing.png')
    player_rect = py.transform.scale_by(player_rect, 2)

    # player gravity
    if y_pos <= 210:
        delta_y += 0.1

    if y_pos > 210:
        delta_y = 0
        y = 210

    if player_direction == 'right':
        player_rect = py.transform.flip(player_rect, flip_x=False, flip_y=False)
    elif player_direction == 'left':
        player_rect = py.transform.flip(player_rect, flip_x=True, flip_y=False)
    screen.blit(player_rect, (x_pos, y_pos))


# Initializing variables for the game

RUN = True
x, y = 0, 0
player_direction = 'right'

# delta_x = player movement speed, delta_y = gravity/jumping
delta_x, delta_y = 0, 0
# Game loop
while RUN:
    screen.fill('black')
    for event in py.event.get():
        if event.type == py.QUIT:
            RUN = False
        if event.type == py.KEYDOWN:
            if event.key == py.K_a:
                delta_x = -5
                player_direction = 'left'
        if event.type == py.KEYDOWN:
            if event.key == py.K_d:
                delta_x = 5
                player_direction = 'right'
        if event.type == py.KEYDOWN:
            if event.key == py.K_w:
                delta_y = 0
                delta_y -= 5

        if event.type == py.KEYUP:
            if event.key == py.K_a:
                delta_x = 0
        if event.type == py.KEYUP:
            if event.key == py.K_d:
                delta_x = 0
    draw_player(x_pos=x, y_pos=y)
    py.display.flip()
    clock.tick(60)
# After the game stop running
message("Game Over", (255, 0, 0), screen, screen_width, screen_height)
py.display.update()
time.sleep(1)
py.quit()
