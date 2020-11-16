import pygame
import random
import os
from scripts import *
from settings import *

pygame.init()
os.environ['SDL_VIDEO_WINDOW_POS'] = '0,30'
info = pygame.display.Info()
WIDTH_WIN, HEIGHT_WIN = info.current_w, info.current_h

screen = pygame.display.set_mode((WIDTH_WIN, HEIGHT_WIN))
pygame.display.set_icon(pygame.image.load('робот.png'))
pygame.display.set_caption('Стёпа-робот')
clock = pygame.time.Clock()

part1 = pygame.Surface((WIDTH_WIN // 6, HEIGHT_WIN))
part1_rect = part1.get_rect(topleft=(0, 0))
part1.fill(com_BG)

part2 = pygame.Surface((WIDTH_WIN // 2, HEIGHT_WIN))
part2_rect = part2.get_rect(topleft=(WIDTH_WIN // 2, 0))
part2.fill(BG_COLOR1)


part3 = pygame.Surface((WIDTH_WIN // 2, HEIGHT_WIN // 6))
part3_rect = part3.get_rect(topleft=(WIDTH_WIN // 2, 0))
part3.fill(BG_COLOR2)

BG_map = pygame.transform.scale(
    BG_map, (part2.get_width(), part2.get_height() - part3.get_height()))
BG_map_rect = BG_map.get_rect(topleft=(0, part3.get_height()))

dict_draw = {
    part1: part1_rect, part2: part2_rect,
    part3: part3_rect, BG_map: BG_map_rect
}


def draw():
    pygame.draw.rect(part1, pygame.Color('black'),
                     [0, 0, WIDTH_WIN // 6 - 1, HEIGHT_WIN - 1], 3)

    pygame.draw.rect(part2, pygame.Color('black'),
                     [0, 0, WIDTH_WIN // 2, HEIGHT_WIN], 3)

    pygame.draw.rect(screen, pygame.Color('black'),
                     [WIDTH_WIN // 6, 0, WIDTH_WIN // 3, HEIGHT_WIN], 3)

    pygame.draw.rect(part3, pygame.Color('black'),
                     [0, 0, WIDTH_WIN, HEIGHT_WIN], 3)


run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT or \
                e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            run = False
        elif e.type == pygame.MOUSEBUTTONDOWN:
            if e.button == 1:
                if btn1.collidepoint(e.pos):
                    i.reverse()
                if btn2.collidepoint(e.pos):
                    w.reverse()
                if btn3.collidepoint(e.pos):
                    q.reverse()
                if btn4.collidepoint(e.pos):
                    q.reverse()

    screen.fill(BG_COLOR)
    for k, v in dict_draw.items():
        screen.blit(k, v) if k != BG_map else part2.blit(k, v)
    draw()
    btn1 = screen.blit(st_btn if i[0] else image_btn, (990, 40))
    btn3 = screen.blit(res1 if q[0] else res, (1100, 40))
    btn2 = screen.blit(speed1 if w[0] else speed, (1500, 40))
    btn4 = screen.blit(lamp (1800, 40))
    pygame.display.update()
    if q[0]:
        pygame.time.wait(250)
        q.reverse()
