import pygame as py
import time
import sys

#message when leaving the game
def message(msg,color, screen, screen_width, screen_height):
    font_style = py.font.SysFont(None, 50)
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [screen_width/2 - 100, screen_height/2])
