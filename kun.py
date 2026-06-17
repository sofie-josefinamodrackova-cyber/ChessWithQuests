from figurka import Figurka
from vektor import Vektor
class Kun(Figurka, Vektor):
    def __init__(self, barva):
        super().__init__("kun", barva)
        self.skok = True
