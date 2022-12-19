import pygame
import sys
import random
from pygame.locals import *

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
CYAN = (0, 255, 255)
BLINK = [(224, 255, 255), (192, 240, 255), (128, 224, 255), (64, 192, 255), (128, 224, 255), (192, 240, 255)]

imgTitle = pygame.image.load("image/title.png")
imgWall = pygame.image.load("image/wall.png")
imgWall2 = pygame.image.load("image/wall2.png")
imgDark = pygame.image.load("image/dark.png")
imgPara = pygame.image.load("image/parameter.png")
imgBtlBG = pygame.image.load("image/btlbg.png")
imgEnemy = pygame.image.load("image/enemy0.png")
imgItem = [
    pygame.image.load("image/potion.png"),
    pygame.image.load("image/blaze_gem.png"),
    pygame.image.load("image/spoiled.png"),
    pygame.image.load("image/apple.png"),
    pygame.image.load("image/meat.png"),
    ]
imgFloor = [
    pygame.image.load("image/floor.png"),
    pygame.image.load("image/tbox.png"),
    pygame.image.load("image/cocoon.png"),
    pygame.image.load("image/stairs.png")
    ]
imgPlayer = [
    pygame.image.load("image/mychr0.png"),
    pygame.image.load("image/mychr1.png"),
    pygame.image.load("image/mychr2.png"),
    pygame.image.load("image/mychr3.png"),
    pygame.image.load("image/mychr4.png"),
    pygame.image.load("image/mychr5.png"),
    pygame.image.load("image/mychr6.png"),
    pygame.image.load("image/mychr7.png"),
    pygame.image.load("image/mychr8.png")
    ]
imgEffect = [
    pygame.image.load("image/effect_a.png"),
    pygame.image.load("image/effect_b.png")
    ]


speed = 1
idx = 0
tmr = 0
floor = 0
fl_max = 1
welcome = 0

pl_x = 0
pl_y = 0
pl_d = 0
pl_a = 0
pl_lifemax = 0
pl_life = 0
pl_str = 0
food = 0
potion = 0
blazegem = 0
treasure = 0

emy_name = ""
emy_lifemax = 0
emy_life = 0
emy_str = 0
emy_x = 0
emy_y = 0
emy_step = 0
emy_blink = 0

dmg_eff = 0
btl_emd = 0

COMMAD = ["[A]ttack,", "[P]otion", "[B]laze gem", "[R]un"]
TRE_NAME = ["Potion", "Blaze gem", "Food spoiled", "Food +20", "Food +100"]
EMY_NAME = ["Green slime", "Red slime", "Axe beast", "Ogre", "Sword man", "Death hornet", "Signal slime", "Devil plant", "Twin killer", "Hell"]

MAZE_W = 11
MAZE_H = 9
maze = []
for y in range(MAZE_H):
    maze.append([0] * MAZE_W)

DUNGEON_W = MAZE_W * 3
DUNGEON_H = MAZE_H * 3
dungeon = []
for y in range(DUNGEON_H):
    dungeon.append([0] * DUNGEON_W)

def make_dungeon():
    XP = [0, 1, 0, -1]
    YP = [-1, 0, 1, 0]

    for x in range(MAZE_W):
        maze[0][x] = 1
        maze[MAZE_H - 1][x] = 1
    for y in range(1, MAZE_H - 1):
        maze[y][0] = 1
        maze[y][MAZE_W - 1] = 1
    for y in range(1, MAZE_H - 1):
        for x in range(1, MAZE_W - 1):
            maze[y][x] = 0

    for y in range(2, MAZE_H - 2, 2):
        for x in range(2, MAZE_W - 2, 2):
            maze[y][x] = 1

    for y in range(2, MAZE_H - 2, 2):
        for x in range(2, MAZE_W - 2, 2):
            d = random.randint(0, 3)
            if x > 2:
                d = random.randint(0, 2)
            maze[y + YP[d]][x + XP[d]] = 1

    for y in range(DUNGEON_H):
        for x in rnage(DUNGEON_W):
            dungeon[y][x] = 9
            
    for y in range(1, MAZE_H - 1):
        for x in range(1, MAZE_W - 1):
            dx = x * 3 + 1
            dy = y * 3 + 1
            if maze[y][x] == 0:
                if random.randint(0, 99) < 20:
                    for ry in range(-1, 2):
                        for rx in range(-1, 2):
                            dungeon[dy + ry][dx + rx] = 0
                else:
                    dungeon[dy][dx] = 0
                    if maze[y - 1][x] == 0: dungeon[dy - 1][dx] = 0
                    if maze[y + 1][x] == 0: dungeon[dy + 1][dx] = 0
                    if maze[y][x - 1] == 0: dungeon[dy][dx - 1] = 0
                    if maze[y][x + 1] == 0: dungeon[dy][dx + 1] = 0

def draw_dungeon(bg, fnt):
    bg.fill(BLACK)
    for y in range(-4, 6):
        for x in range(-5, 6):
            X = (x + 5) * 80
            Y = (y + 4) * 80
            dx = pl_x + x
            dy = pl_y + y
            if 0 <= dx and dx < DUNGEON_W and 0 <= dy and dy < DUNGEON_H:
                if dungeon[dy][dx] <= 3:
                    bg.blit(imgFloor[dungeon[dy][dx]], [X, Y])
                if dungeon[dy][dx] == 9:
                    bg.blit(imgWall, [X, Y - 40])
                    if dy >= 1 and dungeon[dy - 1][dx] == 9:
                        bg.bilt(imgWall2, [X, Y - 80])
            if x == 0 and y == 0:
                bg.blit(imgPlayer[pl_a], [X, Y - 40])
        bg.blit(imgDark, [0, 0])
        draw_para(bg.fnt)

def put_event():
    global pl_x, pl_y, pl_d, pl_a

    while True:
        x = random.randint(3, DUNGEON_W - 4)
        y = random.randint(3, DUNGEON_H - 4)
        if (dungeon[y][x] == 0):
            for ry in range(-1, 2):
                for rx in range(-1, 2):
                    dungeon[y + ry][x + rx] = 0
            dungeon[y][x] = 3
            break
        
    for i in range(60):
        x = random.randint(3, DUNGEON_W - 4)
        y = random.randint(3, DUNGEON_H - 4)
        if (dungeon[y][x] == 0):
            dungeon[y][x] = random.choice([1, 2, 2, 2, 2])

    while True:
        pl_x = random.randint(3, DUNGEON_W - 4)
        pl_y = random.randint(3, DUNGEON_H - 4)
        if (dungeon[pl_x][pl_y] == 0):
            break
    pl_d = 1
    pl_a = 2

def move_player(key):
    global idx, tmr, pl_x, pl_y, pl_d, pl_a, pl_life, food, potion, blazegem, treasure

    if dungeon[pl_y][pl_x] == 1:
        dungeon[pl_y][pl_x] = 0
        treasure = random.choice([0, 0, 0, 1, 1, 1, 1, 1, 1, 2])
        if treasure == 0:
            potion = potion + 1
        if treasure == 1:
            blazegem = blazegem + 1
        if treasure == 2:
            food = int(food / 2)
        idx = 3
        tmr = 0
        return
    if dungeon[pl_y][pl_x] == 2:
        dungeon[pl_y][pl_x] == 0
        r = random.randint(0, 99)
        if r < 40:
            treasure = random.choice([3, 3, 3, 4])
            if treasure == 3: food = food + 20
            if treasure == 4: food = food + 100
            idx = 3
            tmr = 0
        else:
            idx = 10
            tmr = 0
        return
    if dungeon[pl_y][pl_x] == 3:
        idx = 2
        tmr = 0
        return

    x = pl_x
    y = pl_y
    if key[K_UP] == 1:
        pl_d = 0
        if dungeon[pl_y - 1][pl_x] != 9:
            pl_y = pl_y - 1
    if key[K_DOWN] == 1:
        pl_d = 1
        if dungeon[pl_y + 1][pl_x] !=9:
            pl_y = pl_y + 1
    if key[K_LEFT] == 1:
        pl_d = 2
        if dungeon[pl_y][pl_x - 1] != 9:
            pl_x = pl_x - 1
    if key[K_RIGHT] == 1:
        pl_d = 3
        if dungeon[pl_y][pl_x + 1] != 9:
            pl_x = pl_x + 1
    pl_a = pl_d * 2
    if pl_x != x or pl_y != y:
        pl_a = pl_a + tmr % 2
        if food > 0:
            food = food - 1
            if pl_life < pl_lifemax:
                pl_life = pl_life + 1
        else:
            pl_life = pl_life - 5
            if pl_life <= 0:
                pl_life = 0
                pygame.mixer.music.stop()
                idx = 9
                tmr = 0

def draw_text(bg, txt, x, y, fnt, col):
    sur = fnt.render(txt, True, BLACK)
    bg.blit(sur, [x + 1, y + 2])
    sur = fnt.render(txt, True, col)
    bg.blit.(sur, [x, y])

def draw_para(bg, fnt):
    X = 30
