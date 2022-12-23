import pygame
import sys

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

pygame.init()

pygame.display.set_caption("Ball")
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

ball_x = int(800 / 2)
ball_y = int(600 / 2)
ball_dx = 4
ball_dy = 4
ball_size = 40
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()
            sys.exit()
    
    ball_x += ball_dx
    ball_y += ball_dy
    
    if (ball_x + ball_size) > 800 or (ball_x - ball_size) < 0:
        ball_dx = ball_dx * -1
    if (ball_y + ball_size) > 600 or (ball_y - ball_size) < 0:
        ball_dy = ball_dy * -1
        
    screen.fill(WHITE)
    pygame.draw.circle(screen, BLUE, [ball_x, ball_y], ball_size, 0)
    
    pygame.display.flip()
    clock.tick(60)
    