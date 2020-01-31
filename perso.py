class Perso : 
    def __init__(self, pos, pdv, armure, moulah):
        self._pos = pos
        self.pdv = pdv
        self.armure = armure
        self.moulah = moulah
   
    def depl(delta_x, delta_y): 
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
    
    def buy_armure(self, coin):
        self.moulah -= coin
        self.pdv += coin//10

    @property
    def pos(self):
        return self._pos
    @pos.setter 
    def pos(self, position):
        
        if len(position) == 2 and isinroom[position[0]][position[1]] != 0 and (self.pos[0]-position[0])**2 + (self.pos[1]-position[1])**2: 
            self._pos = position
        elif len(position) != 2 :  
            raise TypeError("c'est pas une position")
        elif isinroom[position[0]][position[1]] == 0 :  
            raise ValueError("il est pas dans la salle")

"""{pygame.K_a : 'a', pygame.K_b : 'b', pygame.K_c : 'c', pygame.K_d : 'd', pygame.K_e : 'e',
 pygame.K_f : 'f', pygame.K_g : 'g', pygame.K_h : 'h', pygame.K_i : 'i', pygame.K_j : 'j', 
 pygame.K_k : 'k', pygame.K_l : 'l', pygame.K_m : 'm', pygame.K_n : 'n', pygame.K_o : 'o', 
 pygame.K_p : 'p', pygame.K_q : 'q', pygame.K_r : 'r', pygame.K_s : 's', pygame.K_t : 't',
 pygame.K_u : 'u', pygame.K_v : 'v', pygame.K_w : 'w', pygame.K_x : 'x', pygame.K_y : 'y', 
 pygame.K_z : 'z'}"""
