from figurka import Figurka
class Kral(Figurka):
    def __init__(self, barva):
        super().__init__("Král", barva)
        self.skok = False