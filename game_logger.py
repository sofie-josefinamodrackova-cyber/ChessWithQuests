class GameLogger:
    def __init__(self,soubor):
        self.soubor = soubor
    def vytvor_soubor(self,cesta):
        self.soubor=open(cesta,"r", encoding="utf-8")
    def uloz_tah(self, tah):
        if self.soubor:
            self.soubor.close()
            self.soubor=open(tah,"r", encoding="utf-8")