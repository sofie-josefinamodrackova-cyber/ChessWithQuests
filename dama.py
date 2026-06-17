from figurka import Figurka
class Dama(Figurka):
    def __init__(self, barva):
        super().__init__("Dáma", barva)
        self.skok = False