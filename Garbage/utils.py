import pygame


def write_text(msg, color, screen, x, y):
    font_style = pygame.font.SysFont(None, 50)
    text = font_style.render(msg, True, color)
    screen.blit(text, (x, y))