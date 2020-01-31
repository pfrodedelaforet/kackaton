import sys
import pygame
from random import randrange 
from itertools import product
import numpy as np

class generate_salle:
  def __init__(self,coordonnées,name):
    self.a=coordonnées[0]
    self.b=coordonnées[1]
    self.c=coordonnées[2]
    self.d=coordonnées[3]
    self.name=name

class gener_carte:
  def actualisercarte(self,salle):
    for i in range(salle.a[0],salle.c[0]+1):
      for j in range(10):
        self.carte[i][salle.a[1]+j]=1
        self.carte[i][salle.d[1]-j]=1
    for i in range(salle.a[1],salle.b[1]+1):
      for j in range(10):
        self.carte[salle.a[0]+j][i]=1
        self.carte[salle.c[0]-j][i]=1
  
  def __init__(self,taille):
    self.carte=np.zeros(taille)
    salle1=generate_salle(((20,20),(20,450),(450,20),(450,450)),1)
    salle2=generate_salle(((500,500),(500,900),(900,500),(900,900)),2)
    #salle3=generate_salle(((50,1000),(50,1400),(300,1000),(300,1400)),3)
    salle4=generate_salle(((600,30),(600,300),(980,30),(980,300)),4)
    self.actualisercarte(salle1)
    self.actualisercarte(salle2)
    #self.actualisercarte(salle3)
    self.actualisercarte(salle4)

taille=(1000,1500)
M=gener_carte(taille)
carte = M.carte
# print(M.carte[700,30])


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
GREY = (142, 162, 198)
RED = (255,0,0)
BLUE=(0,0,255)
BROWN = (150, 75, 0)

clock = pygame.time.Clock()

BOARD_SIZE = (1000, 1000)
BOARD_WIDTH, BOARD_HEIGHT = BOARD_SIZE

color = {1 : WHITE, 2 : YELLOW } #dico couleur


pygame.init()

screen = pygame.display.set_mode(BOARD_SIZE)

screen.fill(BLACK)

for x in range(BOARD_WIDTH):
    for y in range(BOARD_HEIGHT):
        if carte[x,y] != 0 :
            screen.set_at((x, y), color[carte[x,y]] )

def proj_aff(monster, position):
    L = monster.projectile(position)
    for x in L : 
        if isinroom[x[0]][x[1]] : 
            screen.set_at((x[0], x[1]), BROWN)

for k in range(-10,10):
    for j in range (-10,10):
        screen.set_at((810+k,210+j), RED)

while True:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()



# def draw_cell(carte, color):
#     for x, y in product(range(BOARD_WIDTH), range(BOARD_HEIGHT)):
#         screen_coords = x, y
#         if 100<=x<=800 and 100<=y<=800 :
#             screen.set_at(screen_coords, RED)
#     pygame.display.update()


## SALLE 1
# when joueur in salle 1 :

# for k in range(-10,10):
#     for j in range (-10,10):
#         screen.set_at((210+k,210+j), RED)

# ### SALLE 2 

# for k in range(-10,10):
#     for j in range (-10,10):
#         screen.set_at((810+k,210+j), RED)

# ### SALLE 3

# for k in range(-10,10):
#     for j in range (-10,10):
#         screen.set_at((810+k,610+j), RED)