from models.figurka import Figurka
class Vez(Figurka):
    def __init__(self, barva):
        super().__init__("Věž", barva)
        self.skok = False
        self.vektory = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        self.vektory_utok = self.vektory