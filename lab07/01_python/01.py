import pygame
import datetime

pygame.init()
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Mouse Clock")
background = pygame.image.load("clock.png")
minute_hand = pygame.image.load("min_hand.png")
second_hand = pygame.image.load("sec_hand.png")

background = pygame.transform.scale(background, (WIDTH, HEIGHT))
center_x = WIDTH // 2
center_y = HEIGHT // 2

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    now = datetime.datetime.now()
    min_angle = -(now.minute * 6) 
    sec_angle = -(now.second * 6)  
    
    min_hand = pygame.transform.rotate(minute_hand, min_angle)
    sec_hand = pygame.transform.rotate(second_hand, sec_angle)
    
    min_rect = min_hand.get_rect()
    sec_rect = sec_hand.get_rect()
    min_rect.center = (center_x, center_y)
    sec_rect.center = (center_x, center_y)
    
    screen.blit(background, (0, 0))
    screen.blit(min_hand, min_rect)
    screen.blit(sec_hand, sec_rect)
    
    pygame.display.update()
    pygame.time.delay(1000) 

pygame.quit()
