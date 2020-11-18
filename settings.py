import pygame
import os

pygame.init()
os.environ['SDL_VIDEO_WINDOW_POS'] = '0,30'
info = pygame.display.Info()
WIDTH_WIN, HEIGHT_WIN = info.current_w, info.current_h
i = [False, True]
q = [False, True]
w = [False, True]
r = [False, True]
t = [False, True]
B = 0
FPS = 60
BG_COLOR = (255, 255, 255)
BG_COLOR1 = (200, 200, 200)
BG_COLOR2 = (255, 255, 255)
com_BG = (220, 220, 220)
