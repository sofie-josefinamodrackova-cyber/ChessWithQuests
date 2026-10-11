class Tah:
    def __init__(self, vychozi_pozice, cilova_pozice, figurka, typ_tahu):
        self.vychozi_pozice = vychozi_pozice
        self.cilova_pozice = cilova_pozice
        self.figurka = figurka
        self.typ_tahu = typ_tahu
    def over_platnost(self):
        return True if self.figurka == self.cilova_pozice else False
    def proved_tah(self):
        x1,y1 = self.cilova_pozice
        x2,y2 = self.cilova_pozice

