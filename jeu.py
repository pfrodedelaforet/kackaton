import sys
import pygame
from random import randrange 
from itertools import product
import numpy as np
import time
from monstre import Monster
from perso import Perso
WHITE = (255, 255, 255) 
GREEN = (0, 255, 0) 
BLUE= (0, 0, 128) 
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
# la taille du jeu en nombre de cellules
BOARD_SIZE = (100, 100)
BOARD_WIDTH, BOARD_HEIGHT = BOARD_SIZE

# la taille d'une cellule en nombre de pixels
CELL_SIZE = (10, 10)
CELL_WIDTH, CELL_HEIGHT = CELL_SIZE


def draw_cell(board_x, board_y, color=WHITE):
    screen_x, screen_y = CELL_WIDTH * board_x, CELL_HEIGHT * board_y
    for x, y in product(range(CELL_WIDTH), range(CELL_HEIGHT)):
        screen_coords = screen_x + x, screen_y + y
        screen.set_at(screen_coords, color)

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
      self.carte[i][salle.a[1]]=1
      self.carte[i][salle.d[1]]=1
    for i in range(salle.a[1],salle.b[1]+1):
      self.carte[salle.a[0]][i]=1
      self.carte[salle.c[0]][i]=1

  def escalier1(self,sallea,salleb):
    for i in range(sallea.c[0],salleb.a[0]):
      self.carte[i][sallea.c[1]+5]=3
  
  def escalier2(self,sallea,salleb):
    for i in range(sallea.b[1],salleb.a[1]):
      self.carte[sallea.b[0]+2][i]=3
  
  
  def __init__(self,taille):
    self.carte=np.zeros(taille)
    salle1=generate_salle(((2,2),(2,45),(45,2),(45,45)),1)
    salle2=generate_salle(((60,3),(60,30),(98,3),(98,30)),2)
    salle3=generate_salle(((50,50),(50,90),(90,50),(90,90)),3)
    self.actualisercarte(salle1)
    self.actualisercarte(salle2)
    self.actualisercarte(salle3)
  

taille=(100,100)
M=gener_carte(taille)
carte = M.carte
print(M.carte)



class Perso : 
    def __init__(self, pos, pdv, moulah):#pos 100 * 100
        self._pos = pos
        self.pdv = pdv
        self.moulah = moulah
        self.insalle=1

   
    def depl(self, delta_x, delta_y): #toujours des cases 
        (x, y) = self.pos
        self.pos = (x + delta_x, y + delta_y)

    def reward(self, rewardtype, value):
        if rewardtype == 'coin' : 
            self.moulah += value
        if rewardtype == 'armure':
            self.armure += value
        if rewardtype == 'potion':
            self.pdv += value
    def buy_pdv(self, coin):
        self.moulah -= coin
        self.pdv += coin//10
    """
    def quellesalle(self,salle1,salle2,salle3):
        if salle1.c[0]<=self.pos[0]<=salle1.a[0] and salle1.a[1]<=self.pos[1]<=salle1.c[1]:
            self.insalle=1
        elif salle2.c[0]<=self.pos[0]<=salle2.a[0] and salle2.a[1]<=self.pos[1]<=salle2.c[1]:
            self.insalle=2        
        elif salle3.c[0]<=self.pos[0]<=salle3.a[0] and salle3.a[1]<=self.pos[1]<=salle3.c[1]:
            self.insalle=3
    
    def buy_armure(self, coin):
        self.moulah -= coin
        self.pdv += coin//10
"""
    @property
    def pos(self):
        return self._pos
    @pos.setter 
    def pos(self, position):
        if len(position) == 2 and carte[position[0]][position[1]] == 0: 
            self._pos = position
        elif len(position) != 2 :  
            raise TypeError("c'est pas une position")
        elif carte[position[0]][position[1]] != 0 :  
            raise ValueError("il est pas dans la salle")


class Monster :
    def __init__(self, monster_pos):
        self._monster_pos = monster_pos
    @property
    def monster_pos(self):
        return self._monster_pos
    @monster_pos.setter
    def monster_pos(self, newpos) : 
        if len(newpos) == 2 and carte[newpos[0]][newpos[1]]==0 : 
            self._monster_pos = newpos
        else : 
            raise ValueError()

    def you_can_fight(self, position):
        return (self.monster_pos[0]-position[0])**2 + (self.monster_pos[1]-position[1])**2 <= 1

    def deplacement(self, position): #ce programme permet de faire déplacer le monstre jusqu'au
    #personnage
        while self.monster_pos != position and not self.you_can_fight(position):
            (x,y) = self.monster_pos
            if position[0] <= x :
                self.monster_pos = (x-1, y)
            elif position[0] > x :
                self.monster_pos = (x+1, y)
            if position[1] <= y :
                self.monster_pos = (x, y-1)
            elif position[1] > y :
                self.monster_pos = (x, y+1)
    def projectile(self, position):
        return [(int(x * position[0] + (1-x) * self.monster_pos[0]), int(x * position[1] + (1-x) * self.monster_pos[1])) for x in np.arange(0, 1, 0.01)]
    #pour coder si le monstre croise un mur on peut utiliser le code de pierrot
   
        
            

    def generator(n): # génère un str de taille n
        s = ""
        for k in range(n):
            s = s + chr(97+randrange(26))
        return s

    
    def fight(self, n = 0) : 
        t_0 = time.time()
        s= generator(6)
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render(s, True, green, blue)
        textRect.center = (1000 // 2, 1000 // 2) 
        #il faut fermer la fenetre?
        i=0; win = True
        while time.time()-t_0 < 4 and i<6:
            a = chr(pygame.event.wait())
            if a != s[i] :
                win = False
                break
            i += 1
        if win == False : 
            font = pygame.font.Font('freesansbold.ttf', 32)
            text = font.render('LOSER', True, red, yellow)
            textRect.center = (1000 // 2, 1000 // 2)
            n+=1
            fight(n)
        else : 
            return n 
        
            

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
GREY = (142, 162, 198)
RED = (255,0,0)
BLUE=(0,0,255)
BROWN = (150, 75, 0)

clock = pygame.time.Clock()


color = {1 : RED, 2 : YELLOW, 3 : BLUE} #dico couleur


pygame.init()
screen = pygame.display.set_mode((1000, 1000))
screen.fill(BLACK)
## Pavage
for x in range(100):
    for y in range(100):
        if carte[x,y] != 0 :
            draw_cell(x, y, WHITE)

perso = Perso((10,10),5,0)
### Apparition perso
def apparition_perso(perso):
    draw_cell(perso.pos[0], perso.pos[1], BROWN)

### Apparition monstre 1
monstre = Monster((21,21)) 
def apparition_monstre(monstre):
    draw_cell(monstre.monster_pos[0], monstre.monster_pos[1], RED)

# while True:
#     for event in pygame.event.get(): 
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#     pygame.display.update()



def redraw():
  screen.fill(BLACK)
  print("ahhhhhhhhh")
  for x in range(100):
    for y in range(100):
        if carte[x,y] != 0 :
            draw_cell(x, y, WHITE)
  apparition_perso(perso)
  apparition_monstre(monstre)





running = True

while running:
  (dx, dy) = (0,0)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False   
    elif event.type == pygame.KEYDOWN:
      if event.key == K_q:
        running = False
      elif event.key == K_UP:
        (dx, dy) = (0, -1)
      elif event.key == K_RIGHT:
        (dx, dy) = (1, 0)
      elif event.key == K_DOWN:
        (dx, dy) = (0, 1)
      elif event.key == K_LEFT:
        (dx, dy) = (-1, 0)
    print(dx, dy)
  perso.depl(dx,dy)
  monstre.deplacement(perso.pos)
  redraw()



carte.escalier1(salle1,salle2)
carte.escalier2(salle2,salle3)

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
# 
# """ le monstre envoie un projectile,scenario """
# L = monster.projectile(perso.pos)
# for x in L : 
#     if isinroom[x[0]][x[1]] : 
#         screen.set_at((x[0], x[1]), BROWN)
#         if perso.pos == x : 
#             perso.reward("pdv", -5)
#         time.delay(0.5)

# """c'était l'envoi du projectile"""