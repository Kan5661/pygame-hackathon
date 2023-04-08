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
    global x, y, delta_y, frame, jump, player_rect, counter

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
    player_position, collision = move(tile_rects, player=player_rect, movement=[delta_x, delta_y])
    #Moving bird in the screen and displaying it
    if (counter == 50):
        bird_position.x -= 1
        counter = 0
    else:
        counter+=1
    display.blit(bird_image, bird_position)
    if (abs(bird_position.x - player_position.x )< 15 and abs(bird_position.y - player_position.y )< 10):
        message("You won", (255, 0, 0), screen, screen_width, screen_height)
        py.display.update()
        time.sleep(1)
        py.quit()
        sys.exit()
    # fall speed stop accelerating at 3px/frame
    display.blit(player_image, player_position)
    delta_y += 0.3
    if delta_y > 3:
        delta_y = 3
map_x = 0
i = 0
# Init bird
global bird_position, bird_image, counter
counter = 0
bird_image = py.image.load('assets/player_assets/yellowbird2.png')
bird_position = bird_image.get_rect()
bird_position.x = screen_width /3
bird_position.y = 80
# Game loop
while RUN:
    screen.fill('black')
    screen.blit(py.transform.scale(display, screen_size), (0, 0))
    display.fill('grey')
    tile_rects=[]
    if player_direction == 'left':
        delta_x += -0.001
        map_x += 0.005
    if player_direction == 'right':
        delta_x += 0.001
        map_x += -0.005
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()
            RUN = False
        if event.type == py.KEYDOWN:
            if event.key == py.K_a:
#                delta_x += -4
#                map_x += +4
                player_direction = 'left'
        if event.type == py.KEYDOWN:
            if event.key == py.K_d:
#                delta_x += 4
#                map_x += -4
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
    if(i <= 5):
        i+=1
    else:
        i = 0
        map_x-=1
    move_map_x(display, map_x, tile_rects)
    draw_player(x_pos=x, y_pos=y)
    if (player_rect.x <0 or player_rect.y > screen_height/2):
        message("Game Over", (255, 0, 0), screen, screen_width, screen_height)
        py.display.update()
        time.sleep(1)
        py.quit()
        sys.exit()
    py.display.flip()
    clock.tick(60)
# After the game stop running
# message("Game Over", (255, 0, 0), screen, screen_width, screen_height)
# py.display.update()
# time.sleep(1)
# py.quit()
# sys.exit()
