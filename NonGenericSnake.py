import pygame
import sys
import random #
import os #

#The basic game template is from the baraltech YouTube channel. However, the variable names, the colors*, the code for the colors, and the grid size randomization are all my unique work.
#Note: I modified many of the fixed variable values for aesthetic reasons, and I reduced the frame rate from 20/second to 16/second for gameplay reasons.
#*The template used words for preset colors (e.g: "red"), while I used code for my own custom colors (e.g: (24, 101, 77)).
#Note #2: Lines of code marked with # are also unique to me.
pygame.init()

XLIMIT, YLIMIT = random.randint(17, 19)*50, random.randint(10, 14)*50 #My unique code, which randomizes the game's grid size every time the game is entered.
RECTANGLE_SCALE = 50
FONT = pygame.font.Font("font.ttf", RECTANGLE_SCALE*3) #Font is from the Fontspace website.
END_GAME_SCREEN = pygame.image.load(os.path.join('GameOverScreen.png')) #Both code and image are my unique work.

snakealive = 1 #

screen = pygame.display.set_mode((XLIMIT, YLIMIT))
pygame.display.set_caption("Generic Snake Game But With Randomized Grid Size")
clock = pygame.time.Clock()

class SnakeySnake:
    def __init__(self):
        self.x, self.y = RECTANGLE_SCALE, RECTANGLE_SCALE
        self.xdir = 1
        self.ydir = 0
        self.head = pygame.Rect(self.x, self.y, RECTANGLE_SCALE, RECTANGLE_SCALE)
        self.body = [pygame.Rect(self.x-RECTANGLE_SCALE, self.y, RECTANGLE_SCALE, RECTANGLE_SCALE)]
        self.dead = False
    def update(self):
        global theobject
        for square in self.body:
            if self.head.x == square.x and self.head.y == square.y:
                self.dead = True
            if self.head.x not in range(0, XLIMIT) or self.head.y not in range (0, YLIMIT):
                self.dead = True
        if self.dead:
            self.x, self.y = RECTANGLE_SCALE, RECTANGLE_SCALE
            self.head = pygame.Rect(self.x, self.y, RECTANGLE_SCALE, RECTANGLE_SCALE)
            self.body = [pygame.Rect(self.x-RECTANGLE_SCALE, self.y, RECTANGLE_SCALE, RECTANGLE_SCALE)]
            self.xdir = 1
            self.ydir = 0
            self.dead = False
            global snakealive #
            snakealive = 0 #
            theobject = GenericCube()
        self.body.append(self.head)
        for i in range(len(self.body)-1):
            self.body[i].x, self.body[i].y = self.body[i+1].x, self.body[i+1].y
        self.head.x += self.xdir*RECTANGLE_SCALE
        self.head.y += self.ydir*RECTANGLE_SCALE
        self.body.remove(self.head)

class GenericCube:
    def __init__(self):
        self.x = int(random.randint(0, XLIMIT)/RECTANGLE_SCALE)*RECTANGLE_SCALE
        self.y = int(random.randint(0, YLIMIT)/RECTANGLE_SCALE)*RECTANGLE_SCALE
        self.rect = pygame.Rect(self.x, self.y, RECTANGLE_SCALE, RECTANGLE_SCALE)
    def update(self):
        pygame.draw.rect(screen, (24, 101, 77), self.rect)
        

        
def GridRender():
    for x in range(0, XLIMIT, RECTANGLE_SCALE):
        for y in range(0, YLIMIT, RECTANGLE_SCALE):
            rect = pygame.Rect(x, y, RECTANGLE_SCALE, RECTANGLE_SCALE)
            pygame.draw.rect(screen, (97, 253, 250), rect, 1)
        global snakealive #
        if snakealive == 0: #
            screen.blit(END_GAME_SCREEN, (0, 0)) #

score = FONT.render("0", True, (50, 75, 100))
score_rect = score.get_rect(center=(XLIMIT/2, YLIMIT/7))

GridRender()

thesnake = SnakeySnake()

theobject = GenericCube()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                thesnake.ydir = 1
                thesnake.xdir = 0
            elif event.key == pygame.K_UP:
                thesnake.ydir = -1
                thesnake.xdir = 0
            elif event.key == pygame.K_LEFT:
                thesnake.ydir = 0
                thesnake.xdir = -1
            elif event.key == pygame.K_RIGHT:
                thesnake.ydir = 0
                thesnake.xdir = 1
            elif event.key == pygame.K_SPACE: #
                snakealive = 1 #
    if snakealive == 1: #
        thesnake.update()
        score = FONT.render(f"{len(thesnake.body) - 1}", True, (50, 75, 100)) #I moved this line of code
    screen.fill((0, 0, 0))
    theobject.update()
    pygame.draw.rect(screen, (168, 190, 111), thesnake.head)
    GridRender() #I moved this line of code
    for square in thesnake.body:
        pygame.draw.rect(screen, (168, 190, 111), square)
    screen.blit(score, score_rect)
    if thesnake.head.x == theobject.x and thesnake.head.y == theobject.y:
        thesnake.body.append(pygame.Rect(square.x, square.y, RECTANGLE_SCALE, RECTANGLE_SCALE))
        theobject = GenericCube()
    pygame.display.update()
    clock.tick(16)
