from figurka import Figurka
class Vez(Figurka):
    def __init__(self, barva):
        super().__init__("Věž", barva)
        self.skok = False