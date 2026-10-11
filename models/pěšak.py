from figurka import Figurka
class Pesak(Figurka):
    def __init__(self, barva):
        super().__init__("Pesak", barva)
        self.skok = False
        self.vektory = [(0, 1)]
        self.vektory_utoku = [(1, 1), (-1, 1)]