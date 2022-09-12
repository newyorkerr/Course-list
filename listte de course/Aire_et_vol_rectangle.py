from curses.textpad import rectangle


class Rectangle:
    def __init__(self,ma_long,ma_larg):
        self.longueur=ma_long
        self.largeur=ma_larg

    def perimetre(self):
        return (self.longeur+self.largeur)*2
    
    def air(self):
        return self.longeur*self.largeur

class Parallepipede(Rectangle):
    def __init__(self,ma_long,ma_larg,ma_hauteur):
        Rectangle.__init__(self,ma_larg,ma_long)
        self.hauteur=ma_hauteur
    def volume(self):
        return self.largueur*self.longueur*self.hauteur

mon_rect=Rectangle(10,5)
print("le périmètre de mon rectangle est",mon_rect.perimetre())
print("l'air de mon rectangle est" ,mon_rect.air())

mon_para=Parallepipede(20,8,3)
print("Le permiètre de mon Parallepidepe est",mon_para.premiètre())
print("l'air de mon Parall est",mon_para.air())
print("le volume de mon Para est",mon_para.volume())