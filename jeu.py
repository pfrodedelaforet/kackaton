import sys
import pygame
from random import randrange 
from itertools import product
import numpy as np
import time
from monstre import Monster
from perso import Perso


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

  def escalier1(self,sallea,salleb):
    for i in range(sallea.c[0]-9,salleb.a[0]+10):
      for j in range(10):
        self.carte[i][sallea.c[1]+j+50]=3
  
  def escalier2(self,sallea,salleb):
    for i in range(sallea.b[1]-9,salleb.a[1]+10):
      for j in range(10):
        self.carte[sallea.b[0]+20+j][i]=3
  
  
  def __init__(self,taille):
    self.carte=np.zeros(taille)
    salle1=generate_salle(((20,20),(20,450),(450,20),(450,450)),1)
    salle2=generate_salle(((600,30),(600,300),(980,30),(980,300)),2)
    salle3=generate_salle(((500,500),(500,900),(900,500),(900,900)),3)
    self.actualisercarte(salle1)
    self.actualisercarte(salle2)
    self.actualisercarte(salle3)
    self.escalier1(salle1,salle2)
    self.escalier2(salle2,salle3)

taille=(1000,1000)
M=gener_carte(taille)
carte = M.carte
# print(M.carte[700,30])

class Perso : 
    def __init__(self, pos, pdv, moulah):
        self._pos = pos
        self.pdv = pdv
        self.moulah = moulah
        self.insalle=1

   
    def depl(self, delta_x, delta_y): 
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
    def __init__(self, monster_pos, isinroom):
        self.isinroom = isinroom
        self._monster_pos = monster_pos
    @property
    def monster_pos(self):
        return self._monster_pos
    @monster_pos.setter
    def monster_pos(self, newpos) : 
        if len(newpos) == 2 and self.isinroom[newpos[0]][newpos[1]]==0 : 
            self._monster_pos = newpos
        else : 
            raise ValueError()

    def you_can_fight(self, position):
        return (self.monster_pos[0]-position[0])**2 + (self.monster_pos[1]-position[1])**2 <= 30

    def deplacement(self, position): #ce programme permet de faire déplacer le monstre jusqu'au
    #personnage
        while self.monster_pos != position and not self.you_can_fight(position):
            (x,y) = self.monster_pos
            if position[0] <= x :
                self.monster_pos = (x-10, y)
            elif position[0] > x :
                self.monster_pos = (x+10, y)
            if position[1] <= y :
                self.monster_pos = (x, y-10)
            elif position[1] > y :
                self.monster_pos = (x, y+10)
    def projectile(self, position):
        return [(int(x * position[0] + (1-x) * self.monster_pos[0]), int(x * position[1] + (1-x) * self.monster_pos[1])) for x in np.arange(0, 1, 0.001)]
    #pour coder si le monstre croise un mur on peut utiliser le code de pierrot
   
        
            

    def generator(n): # génère un str de taille n
        s = ""
        for k in range(n):
            s = s + chr(97+randrange(26))
        return s
# white = (255, 255, 255) 
# green = (0, 255, 0) 
# blue = (0, 0, 128) 
# red = (255, 0, 0)
# yellow = (255, 255, 0)
    
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

BOARD_SIZE = (1000, 1000)
BOARD_WIDTH, BOARD_HEIGHT = BOARD_SIZE

color = {1 : RED, 2 : YELLOW, 3 : BLUE} #dico couleur


pygame.init()
screen = pygame.display.set_mode(BOARD_SIZE)
screen.fill(BLACK)
## Pavage
for x in range(1000):
    for y in range(1000):
        if carte[x,y] != 0 :
            screen.set_at((x, y), color[carte[x,y]] )

perso = Perso((100,100),5,0)
### Apparition perso
def apparition_perso(perso):
  for k in range(-10,10):
      for j in range (-10,10):
          screen.set_at((perso.pos[0]+k,perso.pos[1]+j), BROWN)

### Apparition monstre 1
monstre = Monster((210,210),carte) 
def apparition_monstre(monstre):
  for k in range(-10,10):
      for j in range (-10,10):
          screen.set_at((monstre.monster_pos[0]+k,monstre.monster_pos[1]+j), RED)

# while True:
#     for event in pygame.event.get(): 
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#     pygame.display.update()



def redraw():
  screen.fill(BLACK)
  for x in range(1000):
    for y in range(1000):
        if carte[x,y] != 0 :
            screen.set_at((x, y), color[carte[x,y]] )
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
        (dx, dy) = (0, -10)
      elif event.key == K_RIGHT:
        (dx, dy) = (10, 0)
      elif event.key == K_DOWN:
        (dx, dy) = (0, 10)
      elif event.key == K_LEFT:
        (dx, dy) = (-10, 0)
  perso.depl(dx,dy)
  monstre.deplacement(perso.pos)
  redraw()


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
#             perso.reward()
#         time.delay(0.5)

# """c'était l'envoi du projectile"""