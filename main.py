import pygame

pygame.init()
pygame.display.set_caption('число')
display = pygame.display.set_mode((800, 600))
pygame.mouse.set_visible(True)

blue = (0, 0, 50)
red = (255, 0, 0)
white = (255, 255, 255)
yellow = (255, 230, 0)
text1_rect = (200, 300)
text2_rect = (300, 370)
kv_x = 360
kv_y = 230
font = pygame.font.SysFont('Calibri', 70, True, False)
font2 = pygame.font.SysFont('Arial', 28, False, False)


working = True
while working:
    for main_event in pygame.event.get():
        if main_event.type == pygame.QUIT:
            working = False
    display.fill(blue)
    pygame.draw.rect(display, red, (kv_x, kv_y, 60, 60))
    display.blit(font.render('Всем привет', True, white), (text1_rect))
    display.blit(font2.render('задание на урок', True, yellow), (text2_rect))
    kv_x =kv_x + 1
    if kv_x>800:
        kv_x=0
    pygame.display.update()
