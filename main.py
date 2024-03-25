import pygame
import math
from cfg import*
from loadVec import read

class Player:
    x, y   = 200, 200
    vx, vy = 0, 0

def setVecList(n, c):
    m = []
    for i in n:
        m.append(((i[0]+1)*c, (i[1]+1)*c))
    return list(reversed(m))

def physics():
    global p, t
    p.x += p.vx * t
    p.y += p.vy * t

def draws():
    global mx, my, lines, cub, figs, p
    sc.fill((255, 255, 255))
    sc.blit(playerSurf, (p.x-4*cub, p.y-2.5*cub))
    
def events():
    global p, t
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            return True
        elif event.type == pygame.MOUSEMOTION:
            if not (p.x-event.pos[0]==0 and p.y-event.pos[1]==0):
                pass
        elif event.type == pygame.KEYDOWN:
            pass
    return False

def MainLoop():
    global FPS, t
    Close = False
    while not Close:
        Close = events()
        physics()
        draws()
        
        pygame.display.update()
        t = 1/clock.tick(FPS)
    pygame.quit()

if __name__=="__main__":
    pygame.init()
    clock = pygame.time.Clock()
    sc = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    mx, my = sc.get_width(), sc.get_height()
    cub = (mx if mx>my else my)*.01
    lines, figs = read("bomb.vec")
    p = Player()
    
    playerSurf = pygame.Surface((int(8*cub), int(5*cub)))
    playerSurf.fill((1, 1, 1))
    playerSurf.set_colorkey((1, 1, 1))
    for i in figs:
        pygame.draw.polygon(playerSurf, i[0], setVecList(i[1], cub))
    for i in lines:
        pygame.draw.lines(playerSurf, i[0], False, setVecList(i[2], cub), int(cub*i[1]/256))
    
    MainLoop()

#surf = pygame.image.load("dog.png")
#surf.set_colorkey((0, 255, 0))
#surf = pygame.transform.scale(surf, (350, 350))

#font = pygame.font.SysFont('arial', 36)
#surf = font.render('Hello World!', True, (180, 0, 0))

