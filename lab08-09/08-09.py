import pygame

pygame.init()


WIDTH, HEIGHT = 1400, 1020 # Создаёт разрешение для окна 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock() # Управляет частотой кадров в окне. Если ее не будет то игра будет слишком плавной и не будет ограничений из за этого может привести к лагам

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
COLORS = [BLACK, RED, GREEN, BLUE, YELLOW, PURPLE, ORANGE] # Список цветов
color_index = 0
color = COLORS[color_index] # Обращение к каждому цвету через индекс

tools = ["brush", "eraser", "rectangle", "circle", "square", "triangle", "eq_triangle", "rhombe"] # Список инструментов
tool = "brush" # Инструмент по умолчанию
radius = 5 # размер кисти
drawing = False # Проверка что на экране вообще что то рисуется
start_pos = None
last_pos = None

canvas = pygame.Surface((WIDTH, HEIGHT)) # Основной холст для рисования, оно имеет размер всего экрана
canvas.fill(WHITE) # Белым цветом
preview = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA) # Будет нужна в будущем чтобы при рисовании фигуры было видно предварительный слой для фигур

undo_stack = []
redo_stack = []
# Для хранения истории изменений

def clear_canvas():
    canvas.fill(WHITE) # закрашивает экран белым
    undo_stack.clear()  # очищает стек отмены через clear()
    redo_stack.clear() # Очищает стек повтора

def save_state():
    undo_stack.append(canvas.copy()) # Добавляет копию холста в стек отмены

def undo():
    if undo_stack: # Проверка, что есть ли что то на холсте 
        redo_stack.append(canvas.copy()) # Сохраняет текущее положение в redo_stack
        canvas.blit(undo_stack.pop(), (0, 0)) # Восстанавливает прошлый кадр

def redo():
    if redo_stack: # Проверяет, на то что можно ли что то восстановить
        undo_stack.append(canvas.copy()) # Аналогично но с undo_stack
        canvas.blit(redo_stack.pop(), (0, 0)) # Восстанавливает действие 

running = True  
while running:
    screen.fill(WHITE) # Заливает экран белым цветом
    screen.blit(canvas, (0, 50)) # размещяет холст чуть ниже из за панели для инструментов
    screen.blit(preview, (0, 50)) # Аналогично
    preview.fill((0, 0, 0, 0)) # очищает слой preview делая его полностью прозрачным после нанесения фигуры

    pygame.draw.rect(screen, (200, 200, 200), (0, 0, WIDTH, 50)) # Рисует серый прямоугольник сверху экрана
    font = pygame.font.Font(None, 26) # Размер шрифта 26, там стоит None потому что там будет использован дефолтный шрифт
    labels = ["Brush (B)", "Eraser (E)", "Rect (R)", "Circle (C)", "Square (Q)", "Triangle (T) ", 
              "Eq Triangle (H)"," ", "Rhombe (D)", "Clear (X)", "Undo (Ctrl+Z)", "Redo (Ctrl+Y)", "Color (1-7)"] # Список инструментов и с его горячими клавишами
    for i, label in enumerate(labels):
        text = font.render(label, True, BLACK) # Делает текст инструмента и цвет Черный.
        screen.blit(text, (10 + i * 110, 10)) # Рисует текст на экране, следуя этому правилу screen.blit(text, (x, y)), берем текст и сдвигаем на позицию по х и у
    
    mouse_x, mouse_y = pygame.mouse.get_pos() # возвращает координаты х и у
    adjusted_pos = (mouse_x, mouse_y - 50)  # рисование происходит ниже панели, поэтому мы корректируем координаты чтобы мышь работала с холстом а не с панелью
    
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
                undo()  # Выполняет функцию возврата прошлого кадра
            elif event.key == pygame.K_y and pygame.key.get_mods() & pygame.KMOD_CTRL:
                redo()  # Восстанавливает действие 
        elif event.type == pygame.MOUSEBUTTONDOWN: # Событие срабатывает когда пользователь нажимает на левую кнопку выше
            drawing = True # Флаг который указывает что пользователь начал рисовать. Он используется для управления состоянием рисования, чтобы можно было отслеживать, рисуется ли что-то в данный момент.
            start_pos = adjusted_pos
            last_pos = adjusted_pos
            save_state()  
        elif event.type == pygame.MOUSEBUTTONUP:
            if start_pos != adjusted_pos: 
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
