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
pygame.display.set_icon(pygame.image.load('робот.png')) 
pygame.display.set_caption('Стёпа-робот')

i = [False, True]
q = [False, True]
w = [False, True]
B = 0
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


part3 = pygame.Surface((WIDTH_WIN // 2, HEIGHT_WIN // 6))
part3_rect = part3.get_rect(topleft=(WIDTH_WIN // 2, 0))
part3.fill(BG_COLOR2)


image_btn = pygame.image.load('start_button.png')
image_btn = pygame.transform.scale(image_btn, (100, 100))
image_btn_rect = image_btn.get_rect(center = (100, 100))

st_btn = pygame.image.load('pause_button.png')
st_btn = pygame.transform.scale(st_btn, (90, 90))
st_btn_rect = st_btn.get_rect(center = (100, 100))

speed = pygame.image.load('speed_button.png')
speed = pygame.transform.scale(speed, (100, 100))
speed_rect = speed.get_rect(center=(500, 90))

speed1 = pygame.image.load('inv_speed_button.png')
speed1 = pygame.transform.scale(speed1, (100, 100))
speed1_rect = speed1.get_rect(center=(505, 90))

res= pygame.image.load('restart_button.png')
res = pygame.transform.scale(res, (100, 100))
res_rect = res.get_rect(center=(200, 90))

res1= pygame.image.load('inv_restart_button.png')
res1 = pygame.transform.scale(res1, (100, 100))
res1_rect = res1.get_rect(center=(205, 90))

BG_map= pygame.image.load('коридор.jpg')
BG_map = pygame.transform.scale(BG_map, (part2.get_width(), part2.get_height() - part3.get_height()))
BG_map_rect = BG_map.get_rect(topleft=(0, part3.get_height()))


def line1():
    pygame.draw.rect(part1, pygame.Color('black'), [0, 0, WIDTH_WIN // 6 - 1, HEIGHT_WIN - 1], 3)


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
        elif e.type == pygame.MOUSEBUTTONDOWN:
            if e.button == 1:
                if btn1.collidepoint(e.pos):
                    i.reverse()
                if btn2.collidepoint(e.pos):
                    w.reverse()
                if btn3.collidepoint(e.pos):
                    q.reverse()

    screen.fill(BG_COLOR)
    screen.blit(part1, part1_rect)
    screen.blit(part2, part2_rect)
    screen.blit(part3, part3_rect)
    part2.blit(BG_map, BG_map_rect)
    line1()
    line2()
    line3()
    line4()
    btn1 = screen.blit(st_btn if i[0] else image_btn, (990,40))
    btn3 = screen.blit(res1 if q[0] else res, (1100,40))
    btn2 = screen.blit(speed1 if w[0] else speed, (1800,40))
    pygame.display.update()
    if q[0] == True:
        pygame.time.delay(250)
        q.reverse()
    
        