import pygame
import datetime

pygame.init()

WIDTH, HEIGHT = 1400, 1020
screen = pygame.display.set_mode((WIDTH, HEIGHT))
background = pygame.image.load("clock.png")
minute_hand = pygame.image.load("min_hand.png")
second_hand = pygame.image.load("sec_hand.png")

background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Центр экрана
center = (WIDTH // 2, HEIGHT // 2)

running = True
while running:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
    
    now = datetime.datetime.now()
    min_angle = -now.minute * 6  
    sec_angle = -now.second * 6   
    
    rotated_min = pygame.transform.rotate(minute_hand, min_angle)
    rotated_sec = pygame.transform.rotate(second_hand, sec_angle)
    

    min_rect = rotated_min.get_rect(center=center)
    sec_rect = rotated_sec.get_rect(center=center)

    screen.blit(background, (0, 0))
    screen.blit(rotated_min, min_rect.topleft)
    screen.blit(rotated_sec, sec_rect.topleft)

    pygame.display.update()
    pygame.time.delay(1000)

pygame.quit()
