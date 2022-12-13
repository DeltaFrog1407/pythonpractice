import pygame
import sys
def main():
    pygame.init
    pygame.display.set_caption("이미지 확대")
    screen = pygame.display.set_mode((640, 360))
    clock = pygame.time.Clock()
    img_bg = pygame.image.load("pg_bg.png")
    img_chara = pygame.image.load("pg_chara0.png")
    rt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        for i in range(4):
            screen.blit(img_bg, [i*160, 0])
        img_chara_s = pygame.transform.scale(img_chara, [300, 150])
        screen.blit(img_chara_s, [224, 160])
        pygame.display.update()

if __name__ == '__main__':
    main()
        




"""
import pygame
import sys
def main():
    pygame.init
    pygame.display.set_caption("이미지 회전/확대")
    screen = pygame.display.set_mode((640, 360))
    clock = pygame.time.Clock()
    img_bg = pygame.image.load("pg_bg.png")
    img_chara = pygame.image.load("pg_chara0.png")
    rt = 0
    while True:
        rt = rt+1
        if rt > 12:
            rt = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        for i in range(4):
            screen.blit(img_bg, [i*160, 0])
        img_chara_s = pygame.transform.rotozoom(img_chara, 30*rt, 2.0)
        screen.blit(img_chara_s, [224, 160])
        pygame.display.update()
        clock.tick(2)

if __name__ == '__main__':
    main()
"""





"""
import pygame
import sys
def main():
    pygame.init
    pygame.display.set_caption("이미지 회전")
    screen = pygame.display.set_mode((640, 360))
    clock = pygame.time.Clock()
    img_bg = pygame.image.load("pg_bg.png")
    img_chara = pygame.image.load("pg_chara0.png")
    rt = 0
    while True:
        rt = rt+1
        if rt > 12:
            rt = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        for i in range(4):
            screen.blit(img_bg, [i*160, 0])
        img_chara_s = pygame.transform.rotate(img_chara, 30*rt)
        screen.blit(img_chara_s, [224, 160])
        pygame.display.update()
        clock.tick(2)

if __name__ == '__main__':
    main()
        
"""
