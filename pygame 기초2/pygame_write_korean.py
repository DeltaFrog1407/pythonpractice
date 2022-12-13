import pygame
import sys

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def main():
    pygame.init()
    pygame.display.set_caption("Pygame에서 한국어 표시")
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("malgungothic", 80)
    tmr = 0

    while True:
        tmr = tmr + 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        txt = font.render("한국어 표시 " + str(tmr), True, WHITE)
        screen.fill(BLACK)
        screen.blit(txt, [100, 200])
        pygame.display.update()
        clock.tick(10)

if __name__ == '__main__':
    main()




#font = pygame.font.SysFont("malgungothic", 80) 시스템 폰트 사용 시
#font = pygame.font.Font({위치}/{폰트이름}.ttf, 80) 개인 소장 폰트 사용 시
