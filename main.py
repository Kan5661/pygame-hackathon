import pygame as py
import time
import sys

py.init()
screen = py.display.set_mode((800, 500))

RUN = True

while RUN:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit(), sys.exit()