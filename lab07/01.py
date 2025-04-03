import pygame
import datetime

pygame.init()

# Размер окна
WIDTH, HEIGHT = 1400, 1020
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Mouse Clock")

# Загружаем картинки
background = pygame.image.load("clock.png")
minute_hand = pygame.image.load("min_hand.png")
second_hand = pygame.image.load("sec_hand.png")

# Масштабируем фон до размера окна
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Центр экрана
center = (WIDTH // 2, HEIGHT // 2)

running = True
while running:
    # Проверяем события (например, выход из игры)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Получаем текущее время
    now = datetime.datetime.now()
    min_angle = -now.minute * 6  # 6 градусов на каждую минуту
    sec_angle = -now.second * 6   # 6 градусов на каждую секунду
    
    # Поворачиваем стрелки
    rotated_min = pygame.transform.rotate(minute_hand, min_angle)
    rotated_sec = pygame.transform.rotate(second_hand, sec_angle)
    
    # Получаем новые прямоугольники (чтобы правильно разместить стрелки)
    min_rect = rotated_min.get_rect(center=center)
    sec_rect = rotated_sec.get_rect(center=center)
    
    # Рисуем фон и стрелки
    screen.blit(background, (0, 0))
    screen.blit(rotated_min, min_rect.topleft)
    screen.blit(rotated_sec, sec_rect.topleft)
    
    # Обновляем экран
    pygame.display.update()
    
    # Ждем 1 секунду перед следующим обновлением
    pygame.time.delay(1000)

pygame.quit()
