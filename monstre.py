from time import time

class Monster :
    def __init__(self, monster_pos, position):
        self.position = position
        self._monster_pos = monster_pos
    @property
    def monster_pos(self):
        return self._monster_pos
    @monster_pos.setter
    def monster_pos(self, newpos) : 
        if len(newpos) == 2 and isinroom[newpos[0]][newpos[1]] : 
            self._monster_pos = newpos
        else : 
            raise ValueError()

    def random_monster(self, position):
        monster = randrange(BOARD_WIDTH), randrange(BOARD_HEIGHT)
        return monster if monster!=position and salle(monstre) == salle(position) and if 
        (monster[0]-position[0])**2 + (monster[1] - position[1])**2 <= 8 else random_monster(position)
    def you_can_fight(self, position):
        return (self.monster_pos[0]-position[0])**2 + (self.monster_pos[1]-position[1])**2 <= 10

    def deplacement(self, position): #ce programme permet de faire déplacer le monstre jusqu'au
    #personnage
        while self.monster_pos != position and not you_can_fight:
            (x,y) = monster.monster_pos
            if position[0] <= x :
                self.monster_pos = (x-1, y)
            elif position[0] > x :
                self.monster_pos = (x+1, y)
            elif position[1] <= y :
                self.monster_pos = (x, y-1)
            elif position@[1] > y :
                self.monster_pos = (x, y+1)
    def projectile(self, position):
        return [(int(x * position[0] + (1-x) * self.monster_pos[0]), int(x * position[1] + (1-x) * self.monster_pos[1])) for x in np.arange(0, 1, 0.001)]
    #pour coder si le monstre croise un mur on peut utiliser le code de pierrot
   
        
            

    def generator(n): # génère un str de taille n
        s = ""
        for k in range(n):
            s = s + chr(97+randrange(26))
        return s
white = (255, 255, 255) 
green = (0, 255, 0) 
blue = (0, 0, 128) 
red = (255, 0, 0)
yellow = (255, 255, 0)
    
    def fight(self, n = 0) : 
        t_0 = time.time()
        s= generator(6)
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render(s, True, green, blue)
        textRect.center = (1500 // 2, 1000 // 2) 
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
            text = font.render('WRONG', True, red, yellow)
            textRect.center = (1500 // 2, 1000 // 2)
            n+=1
            fight(n)
        else : 
            return n 
        
            
    
        
                        
        #on recommencer


#chronométrer
#afficher le titre
#tester even keydown

    #on génère un string de 5-6 lettres et on laisse 4 sec au mec pour bien le recopier 
    #je fais k down : event.key rajoute à la liste et le dernier event.key doit etre entrer (voir raccourci)
    #si il dépasse les 4 sec : on repart à 0

    

     


                

    
