import pygame
import sys
from utils import *
import random
import math

pygame.init()
clock = pygame.time.Clock()

screen_size = [screen_width, screen_height] = [800, 500]
screen = pygame.display.set_mode(screen_size)

# Event timer
SPAWN_BOULDER = pygame.USEREVENT
pygame.time.set_timer(SPAWN_BOULDER, 4000)  # Trigger spawn boulder event every 4 seconds

INCREASE_GAME_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INCREASE_GAME_SPEED, 20000)


# Create surfaces/images and rect
menu_screen = pygame.image.load('assets/menu_background.png')
game_bg = pygame.image.load('assets/game_bg.png')
game_bg_rect, game_bg_rect.x, game_bg_rect.y = game_bg.get_rect(), 0, 0

bottle_select1 = pygame.image.load('assets/bottle_select1.png')
bottle_select1_rect, bottle_select1_rect.x, bottle_select1_rect.y = bottle_select1.get_rect(), 135, 100
bottle_select2 = pygame.image.load('assets/bottle_select2.png')
bottle_select2_rect, bottle_select2_rect.x, bottle_select2_rect.y = bottle_select2.get_rect(), 235, 100
bottle2 = pygame.image.load('assets/bottle2.png')
pygame.Surface.set_colorkey(bottle2, (255, 255, 255))

pause_play = pygame.image.load('assets/pause_play.png')
pause_play_rect, pause_play_rect.x, pause_play_rect.y = pause_play.get_rect(), 225, 130
pause_menu = pygame.image.load('assets/pause_menu.png')
pause_menu_rect, pause_menu_rect.x, pause_menu_rect.y = pause_menu.get_rect(), 125, 130
pause_screen = pygame.image.load('assets/pause_screen.png')
pause_screen_rect = pause_screen.get_rect()
pygame.Surface.set_colorkey(pause_screen, (255, 255, 255))

playBtn = pygame.image.load('assets/playBtn.png')
playBtn_rect, playBtn_rect.x, playBtn_rect.y = playBtn.get_rect(), 145, 170

bottle1 = pygame.image.load('assets/bottle1.png')
player = bottle1
pygame.Surface.set_colorkey(bottle1, (255, 255, 255))  # set white rgb value to transparent
player_rect, player_rect.x, player_rect.y = player.get_rect(), 150, 110

turtle_seeking = pygame.image.load('assets/bottle_searching_turtle.png')
turtle_found = pygame.image.load('assets/bottle_eaten_turtle.png')
pygame.Surface.set_colorkey(turtle_seeking, (255, 255, 255))
pygame.Surface.set_colorkey(turtle_found, (255, 255, 255))
turtle_rect, turtle_rect.x, turtle_rect.y = turtle_seeking.get_rect(), 0, 0

boulder_img = pygame.image.load('assets/boulder.png')
pygame.Surface.set_colorkey(boulder_img, (255, 255, 255))

splash_effects = [splash1, splash2, splash3, splash4] = [pygame.image.load('assets/effect/splash.png'), pygame.image.load('assets/effect/splash2.png'), pygame.image.load('assets/effect/splash3.png'), pygame.image.load('assets/effect/splash2.png')]
splash_rect = splash1.get_rect()

for effect in splash_effects:
    pygame.Surface.set_colorkey(effect, (255, 255, 255))


def draw_player():
    global FRAME
    FRAME += 2
    if FRAME >= 60:
        FRAME = 0
    splash = splash_effects[math.floor(FRAME/15)]

    display.blit(player, player_rect)
    display.blit(splash, (player_rect.centerx - splash_rect.w / 2, player_rect.centery - splash_rect.h / 2))
    player_rect.x += player_mov_x
    player_rect.y += player_mov_y


def draw_turtle(turtle_img):
    turtle_rect.y = player_rect.y - turtle_rect.h / 2
    display.blit(turtle_img, turtle_rect)


def create_boulder():
    random.shuffle(boulder_spawn_locations)
    number_of_boulders_to_spawn = random.randint(2, 4)

    for i in range(number_of_boulders_to_spawn):
        boulder_rect = boulder_img.get_rect()
        boulder_rect.y = boulder_spawn_locations[i]
        boulder_rect.x = random.randrange(500, 800, 50)
        boulder_rects.append(boulder_rect)


def draw_boulders():
    # Move boulders
    for boulder in boulder_rects:
        boulder.x -= GAME_SPEED

    # Draw boulder
    for boulder_position in boulder_rects:
        display.blit(boulder_img, boulder_position)
    
    # Remove off screen  boulders
    for boulder in boulder_rects:
        if boulder.x < -100:
            boulder_rects.remove(boulder)


def player_collision():
    global GAME1, MENU, player_mov_x, player_mov_y, turtle, G1PAUSE, GAME_SPEED, boulder_rects, SCORE
    if player_rect.colliderect(turtle_rect):
        turtle = turtle_found
        G1PAUSE = True
        GAME_SPEED = 0
        SCORE = 0

    if player_rect.collidelist(boulder_rects) != -1:
        boulder_collided = boulder_rects[player_rect.collidelist(boulder_rects)]
        if boulder_collided.collidepoint(player_rect.midbottom):
            player_rect.bottom = boulder_collided.top - 1
        elif boulder_collided.collidepoint(player_rect.midtop):
            player_rect.top = boulder_collided.bottom + 1
        elif boulder_collided.collidepoint(player_rect.midleft):
            player_rect.left = boulder_collided.right + 1
        else:
            player_rect.right = boulder_collided.left - 1
    if player_rect.top <= 5:
        player_rect.top = 5
    if player_rect.bottom >= 245:
        player_rect.bottom = 245
    if player_rect.right >= 395:
        player_rect.right = 395


def g1pause():
    global player_mov_x, player_mov_y
    if G1PAUSE:
        player_mov_x, player_mov_y = 0, 0
        display.blit(pause_screen, (200 - (pause_screen_rect.w / 2), 125 - (pause_screen_rect.h / 2)))
        display.blit(pause_menu, pause_menu_rect)
        display.blit(pause_play, pause_play_rect)
        write_text(msg='Game Over!', color=(0, 0, 255), screen=display, location=(145, 80), font_size=30)


def move_bg():
    if game_bg_rect.x <= -400:
        game_bg_rect.x = 0
    else:
        game_bg_rect.x -= GAME_SPEED


# Game States/variables
[RUN, MENU, GAME1, G1PAUSE] = [True, True, False, False]
GAME_SPEED = 1
SCORE = 0
FRAME = 0
player_mov_x, player_mov_y, player_speed = 0, 0, 2
turtle = turtle_seeking
boulder_rects = []
boulder_spawn_locations = [0, 50, 100, 150, 200, 250]


while RUN:
    while MENU:
        # draw surfaces
        display = pygame.Surface((400, 250))
        display.blit(menu_screen, (0, 0))
        display.blit(bottle_select1, bottle_select1_rect)
        display.blit(bottle_select2, bottle_select2_rect)
        display.blit(playBtn, playBtn_rect)
        display = pygame.transform.scale(display, (800, 500))  # make every thing scale by 2x
        screen.blit(display, (0, 0))

        for event in pygame.event.get():
            mouse_x_pos, mouse_y_pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                RUN = False
            if playBtn_rect.collidepoint((mouse_x_pos/2, mouse_y_pos/2)) and event.type == pygame.MOUSEBUTTONDOWN:
                GAME1 = True
                MENU = False
                G1PAUSE = False
            if bottle_select1_rect.collidepoint((mouse_x_pos/2, mouse_y_pos/2)) and event.type == pygame.MOUSEBUTTONDOWN:
                player = bottle1
                print('select cola')
            if bottle_select2_rect.collidepoint((mouse_x_pos/2, mouse_y_pos/2)) and event.type == pygame.MOUSEBUTTONDOWN:
                player = bottle2
                print('select water')
        clock.tick(60)
        pygame.display.update()

    while GAME1:
        display = pygame.Surface((400, 250))
        display.blit(game_bg, game_bg_rect)
        draw_turtle(turtle_img=turtle)
        draw_player()
        draw_boulders()
        move_bg()
        player_collision()
        g1pause()
        write_text(msg='Score: ' + str(SCORE), color=(0, 0, 0), location=(5, 5), screen=display, font_size=24)
        SCORE += GAME_SPEED

        display = pygame.transform.scale(display, (800, 500))
        screen.blit(display, (0, 0))
        for event in pygame.event.get():
            mouse_x_pos, mouse_y_pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                RUN = False

            if event.type == SPAWN_BOULDER:
                create_boulder()
            if event.type == INCREASE_GAME_SPEED:
                GAME_SPEED += 0.5

            if event.type == pygame.KEYDOWN and not G1PAUSE:
                if event.key == pygame.K_a:
                    player_mov_x = -player_speed
                if event.key == pygame.K_d:
                    player_mov_x = player_speed
                if event.key == pygame.K_w:
                    player_mov_y = -player_speed
                if event.key == pygame.K_s:
                    player_mov_y = player_speed

            if event.type == pygame.KEYUP and not G1PAUSE:
                if event.key == pygame.K_a:
                    player_mov_x = 0
                if event.key == pygame.K_d:
                    player_mov_x = 0
                if event.key == pygame.K_w:
                    player_mov_y = 0
                if event.key == pygame.K_s:
                    player_mov_y = 0

            if pause_menu_rect.collidepoint((mouse_x_pos / 2, mouse_y_pos / 2)) and event.type == pygame.MOUSEBUTTONDOWN and G1PAUSE:
                GAME1 = False
                G1PAUSE = False
                MENU = True
                turtle = turtle_seeking
                player_rect.x, player_rect.y = 150, 110
                GAME_SPEED = 1
                boulder_rects = []
            if pause_play_rect.collidepoint((mouse_x_pos / 2, mouse_y_pos / 2)) and event.type == pygame.MOUSEBUTTONDOWN and G1PAUSE:
                turtle = turtle_seeking
                player_rect.x, player_rect.y = 150, 110
                G1PAUSE = False
                GAME_SPEED = 1
                boulder_rects = []

        clock.tick(60)
        pygame.display.update()
