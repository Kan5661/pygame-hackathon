import pygame as py
import time
import sys

py.init()
screen = py.display.set_mode((800, 500))
clock = py.time.Clock()

def draw_player():
    player_rect = py.image.load('./assets/player_assets/standing.png')
    screen.blit(player_rect, (0, 0))


RUN = True

while RUN:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit(), sys.exit()
    draw_player()
    
    py.display.update()
    clock.tick(60)