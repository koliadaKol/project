import pygame
import random
import os
from scripts import *
from settings import *
from Back_Ground import *


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
                    r.reverse()
                if btn5.collidepoint(e.pos):
                    t.reverse()

    screen.fill(BG_COLOR)
    for k, v in dict_draw.items():
        screen.blit(k, v) if k != BG_map else part2.blit(k, v)
    draw()
    btn1 = screen.blit(st_btn if i[0] else image_btn, (990, 40))
    btn3 = screen.blit(res1 if q[0] else res, (1100, 40))
    btn2 = screen.blit(speed1 if w[0] else speed, (1500, 40))
    btn4 = screen.blit(inv_lamp if r[0] else lamp, (1650, 40))
    btn5 = screen.blit(inv_task if t[0] else task, (1800, 40))
    pygame.display.update()
    if q[0]:
        pygame.time.wait(250)
        q.reverse()
    if r[0]:
        pygame.time.wait(250)
        r.reverse()
    if t[0]:
        pygame.time.wait(250)
        t.reverse()
