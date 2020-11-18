import pygame
from settings import *
from scripts import *

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