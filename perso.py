class Perso : 
    def __init__(self, pos, pdv, armure, moulah):
        self._pos = pos
        self.pdv = pdv
        self.armure = armure
        self.moulah = moulah
   
    def __depl__(delta_x, delta_y): 
        (x, y) = self.pos
        self.pos = (x + delta_x, y + delta_y)

    def __reward__(self, rewardtype, value):
        if rewardtype == 'coin' : 
            self.moulah += value
        if rewardtype == 'armure':
            self.armure += value
        if rewardtype == 'potion':
            self.pdv += value

    @property
    def pos(self):
        return self._pos
    @pos.setter 
    def pos(self, position):
        if len(position) == 2 and isinroom[position[0]][position[1]]: 
            self._pos = position
        elif len(position) != 2 :  
            raise TypeError("c'est pas une position")
        elif not isinroom[position[0]][position[1]] : 
            raise ValueError("il est pas dans la salle")

    