from figurka import Figurka
from managers.vektor import Vektor
class Kun(Figurka, Vektor):
    def __init__(self, barva):
        super().__init__("kun", barva)
        self.skok = True
        self.vektory = [(1,2),(2,1),(-1,2),(-2,1),(1,-2),(2,-1),(-1,-2),(-2,-1)]
        self.vektory_utoku = self.vektory

