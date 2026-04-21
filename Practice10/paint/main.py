import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()

drawing = False
mode = "draw"
color = (0,0,0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r: color = (255,0,0)
            if event.key == pygame.K_g: color = (0,255,0)
            if event.key == pygame.K_b: color = (0,0,255)
            if event.key == pygame.K_e: mode = "eraser"
            if event.key == pygame.K_c: mode = "circle"
            if event.key == pygame.K_q: mode = "rect"
            if event.key == pygame.K_d: mode = "draw"

        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True

        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False

        if event.type == pygame.MOUSEMOTION and drawing:
            x, y = event.pos

            if mode == "draw":
                pygame.draw.circle(screen, color, (x,y), 5)

            elif mode == "eraser":
                pygame.draw.circle(screen, (255,255,255), (x,y), 10)

            elif mode == "circle":
                pygame.draw.circle(screen, color, (x,y), 20)

            elif mode == "rect":
                pygame.draw.rect(screen, color, (x,y,30,30))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()