from figurka import Figurka
class Strelec(Figurka):
    def __init__(self, barva):
        super().__init__("Střelec", barva)
        self.skok = False
