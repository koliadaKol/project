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
BG_COLOR = (255,255,255)
BG_COLOR1 = (200,200,200)
BG_COLOR2 = (255,255,255)
com_BG = (220,220,220)

part1 = pygame.Surface((WIDTH_WIN // 6, HEIGHT_WIN))
part1_rect = part1.get_rect(topleft=(0, 0))
part1.fill(com_BG)

part2 = pygame.Surface((WIDTH_WIN // 2, HEIGHT_WIN))
part2_rect = part2.get_rect(topleft=(WIDTH_WIN // 2, 0))
part2.fill(BG_COLOR1)

part3 = pygame.Surface((WIDTH_WIN // 2, HEIGHT_WIN // 5))
part3_rect = part3.get_rect(topleft=(WIDTH_WIN // 2, 0))
part3.fill(BG_COLOR2)

k = pygame.image.load('start_button.png')
k = pygame.transform.scale(k, (100, 100))
k_rect = k.get_rect(center=(100, 100))
part3.blit(k, k_rect)


def line1():
    pygame.draw.rect(part1, pygame.Color('black'), [0, 0, WIDTH_WIN // 6 - 1.5, HEIGHT_WIN - 1.5], 3)
    

def line2():
    pygame.draw.rect(part2, pygame.Color('black'), [0, 0, WIDTH_WIN // 2, HEIGHT_WIN], 3)


def line3():
    pygame.draw.rect(screen, pygame.Color('black'), [WIDTH_WIN // 6, 0, WIDTH_WIN // 3, HEIGHT_WIN], 3)


def line4():
    pygame.draw.rect(part3, pygame.Color('black'),[0, 0, WIDTH_WIN, HEIGHT_WIN], 3)

run = True
while run: 
    for e in pygame.event.get():
        if e.type == pygame.QUIT or e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            run = False
    screen.fill(BG_COLOR)
    screen.blit(part1, part1_rect)
    screen.blit(part2, part2_rect)
    screen.blit(part3, part3_rect)
    line1()
    line2()
    line3()
    line4()

    pygame.display.update()
