from models.figurka import Figurka
class Strelec(Figurka):
    def __init__(self, barva):
        super().__init__("Střelec", barva)
        self.skok = False
        self.vektory = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        self.vektory_utoku = self.vektory

