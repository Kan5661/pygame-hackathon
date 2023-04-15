import pygame


def write_text(msg, color, screen, location, font_size):
    font_style = pygame.font.SysFont(None, font_size)
    text = font_style.render(msg, True, color)
    screen.blit(text, location)