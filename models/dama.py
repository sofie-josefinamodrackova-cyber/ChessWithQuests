from models.figurka import Figurka
class Dama(Figurka):
    def __init__(self, barva):
        super().__init__("Dáma", barva)
        self.skok = False
        self.vektory = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
        self.vektory_utoku = self.vektory
