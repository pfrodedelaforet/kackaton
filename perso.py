class Perso : 
    def __init__(self, pos, pdv, armure):
        self.pos = pos
        self.pdv = pdv
        self.armure = armure
    def __depl__(delta_x, delta_y) : 
        (x, y) = self.pos
        self.pos = (x + delta_x, y + delta_y)
        

    @property
    def pos(self):
        return self._pos
    @pos.setter 
    def pos(self, position):
        if len(position) == 2 : 
            self._pos = position
        else : 
            raise TypeError("c'est pas une position")
    