import pygame
import random

# ПРАВИЛЬНО: Инициализация библиотеки Pygame
pygame.init()
pygame.font.init()

# Размеры окна игры
WIDTH = 600
HEIGHT = 400

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🌌 Space Snake: Galaxy Journey 🌌")

# ЦВЕТА (Космический стиль)
SPACE_BLACK = (5, 5, 15)       # Фон космоса
NEON_BLUE = (0, 191, 255)      # Неоново-синяя змейка
STAR_YELLOW = (255, 215, 0)    # Жёлтая звезда (еда)
NEON_PURPLE = (148, 0, 211)    # Фиолетовые препятствия (метеориты)
TEXT_COLOR = (240, 248, 255)   # Цвет текста

# Настройки игры
score = 0
speed = 10
clock = pygame.time.Clock()

font = pygame.font.SysFont("Arial", 22, bold=True)

# Змейка и еда
snake = [[100, 50], [90, 50], [80, 50]]
direction = "RIGHT"
food = [random.randrange(0, WIDTH, 10), random.randrange(0, HEIGHT, 10)]

# Метеориты (Препятствия)
meteors = [[200, 200], [210, 200], [220, 200], [300, 100], [300, 110]]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # Управление
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and direction != "DOWN": direction = "UP"
    if keys[pygame.K_DOWN] and direction != "UP": direction = "DOWN"
    if keys[pygame.K_LEFT] and direction != "RIGHT": direction = "LEFT"
    if keys[pygame.K_RIGHT] and direction != "LEFT": direction = "RIGHT"

    # Движение головы
    head = list(snake[0])
    if direction == "UP": head[1] -= 10
    if direction == "DOWN": head[1] += 10
    if direction == "LEFT": head[0] -= 10
    if direction == "RIGHT": head[0] += 10

    snake.insert(0, head)

    # Проверка: съела ли змейка звезду
    if head == food:
        score += 10
        speed += 1  
        food = [random.randrange(0, WIDTH, 10), random.randrange(0, HEIGHT, 10)]
        while food in meteors:
            food = [random.randrange(0, WIDTH, 10), random.randrange(0, HEIGHT, 10)]
    else:
        snake.pop()

    # Проверка столкновений (Конец игры)
    if (head[0] < 0 or head[0] >= WIDTH or 
        head[1] < 0 or head[1] >= HEIGHT or 
        head in snake[1:] or 
        head in meteors):
        running = False

    screen.fill(SPACE_BLACK)
    
    # Рисуем фиолетовые метеориты
    for meteor in meteors:
        pygame.draw.rect(screen, NEON_PURPLE, pygame.Rect(meteor[0], meteor[1], 10, 10))
    
    # Рисуем синюю змейку
    for block in snake:
        pygame.draw.rect(screen, NEON_BLUE, pygame.Rect(block[0], block[1], 10, 10))
        
    # Рисуем жёлтую звезду (еду)
    pygame.draw.rect(screen, STAR_YELLOW, pygame.Rect(food[0], food[1], 10, 10))

    # Вывод счёта на экран
    score_surface = font.render(f"🚀 Stars Collected: {score}", True, TEXT_COLOR)
    screen.blit(score_surface, (15, 15))

    pygame.display.flip()
    clock.tick(speed)

pygame.quit()
