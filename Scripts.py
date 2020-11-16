import pygame

image_btn = pygame.image.load('start_button.png')
image_btn = pygame.transform.scale(image_btn, (100, 100))
image_btn_rect = image_btn.get_rect(center=(100, 100))

st_btn = pygame.image.load('pause_button.png')
st_btn = pygame.transform.scale(st_btn, (90, 90))
st_btn_rect = st_btn.get_rect(center=(100, 100))

speed = pygame.image.load('speed_button.png')
speed = pygame.transform.scale(speed, (100, 100))
speed_rect = speed.get_rect(center=(500, 90))

speed1 = pygame.image.load('inv_speed_button.png')
speed1 = pygame.transform.scale(speed1, (100, 100))
speed1_rect = speed1.get_rect(center=(505, 90))

res = pygame.image.load('restart_button.png')
res = pygame.transform.scale(res, (100, 100))
res_rect = res.get_rect(center=(200, 90))

res1 = pygame.image.load('inv_restart_button.png')
res1 = pygame.transform.scale(res1, (100, 100))
res1_rect = res1.get_rect(center=(205, 90))

lamp = pygame.image.load('lamp_button.png')
lamp = pygame.transform.scale(lamp, (100, 100))
lamp_rect = lamp.get_rect(center=(500, 90))

BG_map = pygame.image.load('коридор.jpg')
