from figurka import Figurka
class Pesak(Figurka):
    def __init__(self, barva):
        super().__init__("Pěšák", barva)
        self.skok = False
