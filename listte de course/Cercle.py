import math
class Cercle:
    def __init__(self,rayon):
        self.rayon=rayon
    def aire(self):
        return math.pi*self.rayon**2
    def perimetre(self):
        return 2*math.pi*self.rayon


mon_cercle=Cercle(5)
print("la surface de mon cercle est:", round(mon_cercle.aire(),2))
print("le perimètre de mon cercle est:",round(mon_cercle.perimetre(),2))