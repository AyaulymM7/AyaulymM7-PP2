import pygame, random

pygame.init()

W, H = 600, 600
screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

snake = [(300,300)]
dx, dy = 20, 0

food = (random.randint(0,29)*20, random.randint(0,29)*20)

score = 0
level = 1
speed = 10

font = pygame.font.Font(None, 36)

def new_food():
    while True:
        f = (random.randint(0,29)*20, random.randint(0,29)*20)
        if f not in snake:
            return f

running = True
while running:
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP: dx, dy = 0, -20
            if event.key == pygame.K_DOWN: dx, dy = 0, 20
            if event.key == pygame.K_LEFT: dx, dy = -20, 0
            if event.key == pygame.K_RIGHT: dx, dy = 20, 0

    head = (snake[0][0] + dx, snake[0][1] + dy)

    # проверка стены
    if head[0] < 0 or head[0] >= W or head[1] < 0 or head[1] >= H:
        break

    snake.insert(0, head)

    if head == food:
        score += 1
        food = new_food()

        if score % 3 == 0:
            level += 1
            speed += 2
    else:
        snake.pop()

    # рисуем
    for s in snake:
        pygame.draw.rect(screen, (0,255,0), (*s,20,20))

    pygame.draw.rect(screen, (255,0,0), (*food,20,20))

    text = font.render(f"Score: {score}  Level: {level}", True, (255,255,255))
    screen.blit(text, (10,10))

    pygame.display.flip()
    clock.tick(speed)

pygame.quit()