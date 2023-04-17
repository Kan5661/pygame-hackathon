import pygame as py
import time
import sys
import math
from utils import *
from map import *

py.init()
# Initializing the screen and clock
screen_width = 800
screen_height = 500
screen_size = (screen_width, screen_height)
screen = py.display.set_mode(screen_size)
display = py.Surface((400, 250))
display = py.transform.scale(display, (400, 250))
clock = py.time.Clock()

# Initializing variables for the game

RUN = True
x, y = 0, 0
player_direction = 'right'
jump_height = -7
jump = False
player_run_frames = [py.image.load('./assets/player_assets/run1.png'), py.image.load('./assets/player_assets/run2.png'), py.image.load('./assets/player_assets/run3.png')]
player_rect = player_run_frames[0].get_rect()

frame = 0
backgrounds = [py.image.load('assets/background/0.png'), py.image.load('assets/background/1.png'), py.image.load('assets/background/2.png'), py.image.load('assets/background/3.png'), py.image.load('assets/background/4.png')]

# delta_x = player movement speed, delta_y = gravity/jumping
delta_x, delta_y = 0, 0
# Function to insert the player on the screen
def draw_player(x_pos, y_pos):
    global x, y, delta_y, frame, jump, player_rect

    # Player animation and face directions
    frame += 1
    if frame >= 30:
        frame = 0
    if delta_x == 0:
        player_image = py.image.load('./assets/player_assets/standing.png')
    elif delta_x != 0 and not jump:
        player_image = player_run_frames[math.floor(frame/10)]
    if jump:
        player_image = py.image.load('assets/player_assets/jumping.png')

    if player_direction == 'right':
        player_image = py.transform.flip(player_image, flip_x=False, flip_y=False)
    elif player_direction == 'left':
        player_image = py.transform.flip(player_image, flip_x=True, flip_y=False)

    # player_rect.x += x
    # player_rect.y += y
    # x += delta_x
    # y += delta_y

    player_position, collision_test = move(player=player_rect, movement=[delta_x, delta_y])

    # fall speed stop accelerating at 3px/frame
    delta_y += 0.3
    if delta_y > 3: 
        delta_y = 3
    
    if collision_test['bottom'] == True:
        delta_y = 0

    display.blit(player_image, player_position)

    # player_rect = player_position
    
    print(player_position)



# Game loop
while RUN:
    
    screen.fill('black')
    screen.blit(py.transform.scale(display, screen_size), (0, 0))
    display.fill('grey')
    draw_map(display)
    draw_player(x_pos=x, y_pos=y)

    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()
            RUN = False
        if event.type == py.KEYDOWN:
            if event.key == py.K_a:
                delta_x += -5
                player_direction = 'left'
        if event.type == py.KEYDOWN:
            if event.key == py.K_d:
                delta_x += 5
                player_direction = 'right'
        if event.type == py.KEYDOWN:
            if event.key == py.K_w:
                delta_y = 0
                delta_y += jump_height
                jump = True

        if event.type == py.KEYUP:
            if event.key == py.K_a:
                delta_x = 0
        if event.type == py.KEYUP:
            if event.key == py.K_d:
                delta_x = 0
    py.display.flip()
    clock.tick(60)
# After the game stop running
# message("Game Over", (255, 0, 0), screen, screen_width, screen_height)
# py.display.update()
# time.sleep(1)
# py.quit()
# sys.exit()
