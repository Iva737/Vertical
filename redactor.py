import pygame
from loadVec import read, write

pygame.init()
clock = pygame.time.Clock()
sc = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame. mouse. set_visible(False)
mx, my = sc.get_width(), sc.get_height()

cub = (mx if mx>my else my)*.013
button = [False, False, False, False] # awsd
px, py = 30, 15
cursX, cursY = 0, 0
speed = .15
FPS = 30
Close = False
Grid = False

def getPos(pos):
    global px, py, cub
    return (pos[0]*cub+mx//2-px*cub, pos[1]*cub+my//2-py*cub)

def awsdKey(key, down):
    global button
    if key == pygame.K_a or key == pygame.K_LEFT:
        button[0] = down
    elif key == pygame.K_w or key == pygame.K_UP:
        button[1] = down
    elif key == pygame.K_s or key == pygame.K_DOWN:
        button[2] = down
    elif key == pygame.K_d or key == pygame.K_RIGHT:
        button[3] = down

def events():
    global Close, cursX, cursY, mx, my, px, py, Grid, cub
    for evt in pygame.event.get():
        if evt.type == pygame.QUIT or (evt.type == pygame.KEYDOWN and evt.key == pygame.K_ESCAPE):
            Close = True
        elif evt.type == pygame.MOUSEMOTION:
            cursX = round((evt.pos[0]-mx//2+px*cub)/cub)
            cursY = round((evt.pos[1]-my//2+py*cub)/cub)
        elif evt.type == pygame.MOUSEBUTTONDOWN:
            pass
        elif evt.type == pygame.KEYDOWN:
            if evt.key == pygame.K_F3:
                Grid = not Grid
            elif evt.key == pygame.K_PLUS or evt.key == pygame.K_EQUALS:
                cub*=1.2
            elif evt.key == pygame.K_MINUS:
                cub*=0.8
            else:
                awsdKey(evt.key, True)
        elif evt.type == pygame.KEYUP:
            awsdKey(evt.key, False)

def draws():
    global cub, cursX, cursY, Grid, px, py, mx, my
    sc.fill((185, 254, 194))
    if Grid:
        for x in range(int(mx/cub+1)):
            rx = (x-px%1)*cub
            pygame.draw.line(sc, (124, 165, 129), (rx, 0), (rx, my), 1)
        for y in range(int(my/cub+1)):
            ry = (y-py%1)*cub
            pygame.draw.line(sc, (124, 165, 129), (0, ry), (mx, ry), 1)
    
    pygame.draw.circle(sc, ( 70,  1 ,  61), getPos((cursX, cursY)), cub*.2)
    
    pygame.draw.line(sc, (255, 0, 0), (0, getPos((0, 0))[1]), (mx, getPos((0, 0))[1]), 1)
    pygame.draw.line(sc, (0, 255, 0), (getPos((0, 0))[0], 0), (getPos((0, 0))[0], my), 1)
    pygame.draw.circle(sc, (255, 255, 255), getPos((0, 0)), cub*.4)

def physics():
    global px, py, button, speed
    if button[0]: px-=speed
    if button[1]: py-=speed
    if button[2]: py+=speed
    if button[3]: px+=speed

while not Close:
    
    events()
    physics()
    draws()
    
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()

#surf = pygame.image.load("dog.png")
#surf.set_colorkey((0, 255, 0))
#surf = pygame.transform.scale(surf, (350, 350))

#font = pygame.font.SysFont('arial', 36)
#surf = font.render('Hello World!', True, (180, 0, 0))

