import pygame
import copy

pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 1400, 1020
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Advanced Paint App")
clock = pygame.time.Clock()

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
COLORS = [BLACK, RED, GREEN, BLUE, YELLOW, PURPLE, ORANGE]
color_index = 0
color = COLORS[color_index]

# Инструменты
tools = ["brush", "eraser", "rectangle", "circle", "square", "triangle", "eq_triangle", "rhombe"]
tool = "brush"
radius = 5
drawing = False
start_pos = None
last_pos = None
canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill(WHITE)
preview = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)

# История рисования для undo/redo
undo_stack = []
redo_stack = []

# Функция очистки холста
def clear_canvas():
    canvas.fill(WHITE)
    undo_stack.clear()  # Очищаем историю при очистке холста
    redo_stack.clear()

# Функция для сохранения состояния холста
def save_state():
    undo_stack.append(canvas.copy())

# Функция для отмены действия
def undo():
    if undo_stack:
        redo_stack.append(canvas.copy())
        canvas.blit(undo_stack.pop(), (0, 0))

# Функция для повтора действия
def redo():
    if redo_stack:
        undo_stack.append(canvas.copy())
        canvas.blit(redo_stack.pop(), (0, 0))

# Основной цикл программы
running = True
while running:
    screen.fill(WHITE)
    screen.blit(canvas, (0, 50))
    screen.blit(preview, (0, 50))
    preview.fill((0, 0, 0, 0))
    
    # Панель инструментов
    pygame.draw.rect(screen, (200, 200, 200), (0, 0, WIDTH, 50))
    font = pygame.font.Font(None, 26)
    labels = ["Brush (B)", "Eraser (E)", "Rect (R)", "Circle (C)", "Square (Q)", "Triangle (T)", 
              "Eq Triangle (H)", "Rhombe (D)", "Clear (X)", "Undo (Ctrl+Z)", "Redo (Ctrl+Y)", "Color (1-7)"]
    for i, label in enumerate(labels):
        text = font.render(label, True, BLACK)
        screen.blit(text, (10 + i * 110, 10))
    
    mouse_x, mouse_y = pygame.mouse.get_pos()
    adjusted_pos = (mouse_x, mouse_y - 50)  # Убираем смещение на панель инструментов
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                tool = "brush"
            elif event.key == pygame.K_e:
                tool = "eraser"
            elif event.key == pygame.K_r:
                tool = "rectangle"
            elif event.key == pygame.K_c:
                tool = "circle"
            elif event.key == pygame.K_q:
                tool = "square"
            elif event.key == pygame.K_t:
                tool = "triangle"
            elif event.key == pygame.K_h:
                tool = "eq_triangle"
            elif event.key == pygame.K_d:
                tool = "rhombe"
            elif event.key == pygame.K_x:
                clear_canvas()
            elif event.key == pygame.K_1:
                color_index = 0
                color = COLORS[color_index]
            elif event.key == pygame.K_2:
                color_index = 1
                color = COLORS[color_index]
            elif event.key == pygame.K_3:
                color_index = 2
                color = COLORS[color_index]
            elif event.key == pygame.K_4:
                color_index = 3
                color = COLORS[color_index]
            elif event.key == pygame.K_5:
                color_index = 4
                color = COLORS[color_index]
            elif event.key == pygame.K_6:
                color_index = 5
                color = COLORS[color_index]
            elif event.key == pygame.K_7:
                color_index = 6
                color = COLORS[color_index]
            elif event.key == pygame.K_z and pygame.key.get_mods() & pygame.KMOD_CTRL:
                undo()  # Ctrl+Z
            elif event.key == pygame.K_y and pygame.key.get_mods() & pygame.KMOD_CTRL:
                redo()  # Ctrl+Y
        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = adjusted_pos
            last_pos = adjusted_pos
            save_state()  # Сохраняем состояние перед рисованием
        elif event.type == pygame.MOUSEBUTTONUP:
            if start_pos != adjusted_pos:  # Проверяем, чтобы фигура не рисовалась в одной точке
                end_pos = adjusted_pos
                width = end_pos[0] - start_pos[0]
                height = end_pos[1] - start_pos[1]
                if tool == "rectangle":
                    pygame.draw.rect(canvas, color, pygame.Rect(start_pos, (width, height)), 2)
                elif tool == "circle":
                    radius = int((width ** 2 + height ** 2) ** 0.5 / 2)
                    center = (start_pos[0] + width // 2, start_pos[1] + height // 2)
                    pygame.draw.circle(canvas, color, center, radius, 2)
                elif tool == "square":
                    side = min(abs(width), abs(height))
                    pygame.draw.rect(canvas, color, pygame.Rect(start_pos, (side, side)), 2)
                elif tool == "triangle":
                    points = [start_pos, (start_pos[0] + width, start_pos[1] + height), (start_pos[0] - width, start_pos[1] + height)]
                    pygame.draw.polygon(canvas, color, points, 2)
                elif tool == "eq_triangle":
                    height = abs(width * (3 ** 0.5) / 2)
                    points = [start_pos, (start_pos[0] - width // 2, start_pos[1] + height), (start_pos[0] + width // 2, start_pos[1] + height)]
                    pygame.draw.polygon(canvas, color, points, 2)
                elif tool == "rhombe":
                    points = [start_pos, (start_pos[0] + width // 2, start_pos[1] + height // 2), 
                              (start_pos[0], start_pos[1] + height), (start_pos[0] - width // 2, start_pos[1] + height // 2)]
                    pygame.draw.polygon(canvas, color, points, 2)
            drawing = False
        elif event.type == pygame.MOUSEMOTION and drawing:
            end_pos = adjusted_pos
            width = end_pos[0] - start_pos[0]
            height = end_pos[1] - start_pos[1]
            if tool == "brush":
                pygame.draw.line(canvas, color, last_pos, adjusted_pos, radius * 2)
                last_pos = adjusted_pos
            elif tool == "eraser":
                pygame.draw.line(canvas, WHITE, last_pos, adjusted_pos, radius * 2)
                last_pos = adjusted_pos
            else:
                preview.fill((0, 0, 0, 0))
                if tool == "rectangle":
                    pygame.draw.rect(preview, color + (100,), pygame.Rect(start_pos, (width, height)), 2)
                elif tool == "circle":
                    radius = int((width ** 2 + height ** 2) ** 0.5 / 2)
                    center = (start_pos[0] + width // 2, start_pos[1] + height // 2)
                    pygame.draw.circle(preview, color + (100,), center, radius, 2)
                elif tool == "square":
                    side = min(abs(width), abs(height))
                    pygame.draw.rect(preview, color + (100,), pygame.Rect(start_pos, (side, side)), 2)
                elif tool == "triangle":
                    points = [start_pos, (start_pos[0] + width, start_pos[1] + height), (start_pos[0] - width, start_pos[1] + height)]
                    pygame.draw.polygon(preview, color + (100,), points, 2)
                elif tool == "eq_triangle":
                    height = abs(width * (3 ** 0.5) / 2)
                    points = [start_pos, (start_pos[0] - width // 2, start_pos[1] + height), (start_pos[0] + width // 2, start_pos[1] + height)]
                    pygame.draw.polygon(preview, color + (100,), points, 2)
                elif tool == "rhombe":
                    points = [start_pos, (start_pos[0] + width // 2, start_pos[1] + height // 2), 
                              (start_pos[0], start_pos[1] + height), (start_pos[0] - width // 2, start_pos[1] + height // 2)]
                    pygame.draw.polygon(preview, color + (100,), points, 2)

    pygame.display.flip()
    clock.tick(120)

pygame.quit()
