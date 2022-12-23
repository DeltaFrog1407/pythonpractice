import pygame
import sys
import os

GREEN = (100, 200, 100)

pygame.init()
pygame.display.set_caption("Mouse Point")
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

current_path = os.path.dirname(__file__)
assets_path = os.path.join(current_path, 'assets')

mouse_image = pygame.image.load(os.path.join(assets_path, 'mouse.png'))
mouse_x = int(800 / 2)
mouse_y = int(600 / 2)
pygame.mouse.set_visible(False)
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()
            sys.exit()
    pos = pygame.mouse.get_pos()
    mouse_x = pos[0]
    mouse_y = pos[1]
    screen.fill(GREEN)
    
    screen.blit(mouse_image, [mouse_x, mouse_y])
    pygame.display.flip()
    
    clock.tick(60)