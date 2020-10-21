import pygame
import random
import sys
import os
import time

pygame.init()
os.environ['SDL_VIDEO_WINDOW_POS'] = '0,30'
info = pygame.display.Info()
WIDTH_WIN, HEIGHT_WIN = info.current_w, info.current_h

screen = pygame.display.set_mode((WIDTH_WIN, HEIGHT_WIN))
##pygame.display.set_icon(pygame.image.load(saturn)) здесь вставить картинку главного персонажа
pygame.display.set_caption('Стёпа-робот')

FPS = 60
clock = pygame.time.Clock()
BG_COLOR = (255,255,200)
com_BG = (255,255,255)

part1 = pygame.Surface((WIDTH_WIN // 5, HEIGHT_WIN))
part1. = '0,30'


run = True
while run: 
    for e in pygame.event.get():
        if e.type == pygame.QUIT or e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            run = False
    screen.fill(BG_COLOR)
    part1.fill(com_BG)
    pygame.display.update()