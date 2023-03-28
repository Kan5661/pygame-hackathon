import pygame as py
import time
import sys

py.init()
screen = py.display.set_mode((800, 500))
clock = py.time.Clock()

def draw_player(x_pos, y_pos):
    global x
    x += delta_x
    player_rect = py.image.load('./assets/player_assets/standing.png')
    screen.blit(player_rect, (x_pos, y_pos))


RUN = True
x, y = 0, 250
delta_x, delta_y = 0, 0

while RUN:
    screen.fill('black')
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit(), sys.exit()

        if event.type == py.KEYDOWN:
            if event.key == py.K_a:
                delta_x = -5
        if event.type == py.KEYDOWN:
            if event.key == py.K_d:
                delta_x = 5

        if event.type == py.KEYUP:
            if event.key == py.K_a:
                delta_x = 0
        if event.type == py.KEYUP:
            if event.key == py.K_d:
                delta_x = 0
    draw_player(x_pos=x, y_pos=y)
    
    py.display.update()
    clock.tick(60)