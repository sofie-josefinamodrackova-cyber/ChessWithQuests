class HerniPlocha:
    def __init__(self):
        self.rozmery =(8, 8)
        self.herni_deska = []
        self.vyhozene_figurky_b = []
        self.vyhozene_figurky_c = []
    def vrat_obsah(self, souradnice):
        x,y = souradnice
        return self.herni_deska[x][y]
    def posun_figurky(self, tah):
        x1, y1 = tah.vychozi_pozice
        x2, y2 = tah.cilova_pozice
        figurka = self.herni_deska[y1][x1]
        self.herni_deska[y1][x1] = None
        self.herni_deska[y2][x2] = figurka
        return True
    def nahtrad_figurku(self, nova_figurka, tah):
        x,y= tah.cilova_pozice
        self.herni_deska[y][x] = nova_figurka
