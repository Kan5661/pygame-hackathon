import pygame as py
import pytmx
import time
import sys
import math
from utils import *

py.init()
# Initializing the screen and clock
screen_width = 960
screen_height = 640
screen = py.display.set_mode((screen_width, screen_height))
clock = py.time.Clock()

# Given a loaded pytmx map, create a single image which holds a
# rendered version of the whole map.
def renderTmxMap( tmx_map ):
    width  = tmx_map.tilewidth  * tmx_map.width
    height = tmx_map.tileheight * tmx_map.height

    # This surface size
    surface = py.Surface( ( width, height ) )
    for layer in tmx_map.visible_layers:
        # if the Layer is a grid of tiles, get tiles grid and render it
        if ( isinstance( layer, pytmx.TiledTileLayer ) ):
            for x, y, gid in layer:
                tile_bitmap = tmx_map.get_tile_image_by_gid(gid)
                if ( tile_bitmap ):
                    surface.blit( tile_bitmap, ( x * tmx_map.tilewidth, y * tmx_map.tileheight ) )
    return surface
tmx_map   = pytmx.load_pygame( "untitled5.tmx", pixelalpha=True )
map_image = renderTmxMap( tmx_map )
tmx_map   = pytmx.load_pygame( "untitled5.tmx")
#-----------------------------COLLISION NOT WORKING WELL---
#def check_collisions(player_rect, tile_rects)
# Create a player rect
map_objects = py.sprite.Group()
player_group= py.sprite.Group()
player_rect = py.image.load('./assets/player_assets/standing.png')
player_rect = py.sprite.Sprite()
player_rect.image = py.Surface((32, 32))
player_rect.rect = py.Rect(32, 32, 32, 32)
player_group.add(player_rect)
for layer in tmx_map.visible_layers:
    if isinstance(layer, pytmx.TiledObjectGroup):
        for obj in layer:
            print(layer)
            sprite = py.sprite.Sprite()
            sprite.image = py.Surface((obj.width, obj.height))
            sprite.rect = py.Rect(obj.x, obj.y, obj.width, obj.height)
            map_objects.add(sprite)
#for layer in tmx_map.visible_layers:
'''for x, y, gid in tmx_map.layers[0].data:
        tile = py.sprite.Sprite()
        tile.image = tmx_map.get_tile_image_by_gid(gid)
        tile.rect = tile.image.get_rect()
        tile.rect.x = x * tmx_map.tilewidth
        tile.rect.y = y * tmx_map.tileheight
        map_objects.add(tile)'''
#-----------------------------COLLISION NOT WORKING WELL---

# Initializing variables for the game
RUN = True
x, y = 0, 0
player_direction = 'right'
jump_height = 7
jump = False
player_run_frames = [py.image.load('./assets/player_assets/run1.png'), py.image.load('./assets/player_assets/run2.png'), py.image.load('./assets/player_assets/run3.png')]
frame = 0
backgrounds = [py.image.load('assets/background/0.png'), py.image.load('assets/background/1.png'), py.image.load('assets/background/2.png'), py.image.load('assets/background/3.png'), py.image.load('assets/background/4.png')]

# delta_x = player movement speed, delta_y = gravity/jumping
delta_x, delta_y = 0, 0
# Function to insert the player on the screen
sprite1 = py.sprite.Sprite()
def draw_player(player_rect, x_pos, y_pos):
    global x, y, delta_y, frame, jump
    x += delta_x
    y += delta_y
    frame += 1
    if frame >= 30:
        frame = 0
    if delta_x == 0:
        player_rect = py.image.load('./assets/player_assets/standing.png')
    elif delta_x != 0 and not jump:
        player_rect = player_run_frames[math.floor(frame/10)]
    if jump:
        player_rect = py.image.load('assets/player_assets/jumping.png')
    player_rect = py.transform.scale_by(player_rect, 2)
    # player gravity
    if y_pos <= 210:
        delta_y += 0.3
    if y_pos > 210:
        delta_y = 0
        jump = False
        y = 210
    if player_direction == 'right':
        player_rect = py.transform.flip(player_rect, flip_x=False, flip_y=False)
    elif player_direction == 'left':
        player_rect = py.transform.flip(player_rect, flip_x=True, flip_y=False)
    screen.blit(player_rect, (x_pos, y_pos))
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
                delta_y -= jump_height
                jump = True
        if event.type == py.KEYUP:
            if event.key == py.K_a:
                delta_x = 0
        if event.type == py.KEYUP:
            if event.key == py.K_d:
                delta_x = 0
    screen.blit(map_image, (0, 0))
    draw_player(player_rect, x_pos=x, y_pos=y)
    player_group.update()
    map_objects.update()
    if (py.sprite.groupcollide(player_group, map_objects, False, False)):
        print('Collision detected!')
    py.display.flip()
    clock.tick(60)
# After the game stop running
message("Game Over", (255, 0, 0), screen, screen_width, screen_height)
py.display.update()
time.sleep(1)
py.quit()
