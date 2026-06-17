Class GameManager:
    def init(self ):
        self.plocha = Herni_plocha()
        self.aktivni_hrac=0
        self.hraci=[]
        self.aktualni_tah = none
        self.casovac= GameTimer()
        self.game_logger = GameLogger(None)
        self.revizor_tahu= RevizorThu(self.plocha)
    def zacni_tah(self, tah):
        self.aktualni_tah = tah
        return tah
    def proved_tahu(self):
        if self.aktualni_tah is None:
            return False
        if not self.aktualni_tah.over_platnost():
            return False
        self.plocha_figurky(self.aktualni_tah)
        self.game_logger.uloz_tah(self.aktualni_tah)
        return True
    def mozne_tahy(self):
        return[]
    def zrus_tah(self):
        self.aktualni_tah= None
    def uloz_tah(self):
        pass
    def najdi_uzivatele(self, uzivatel_id):
        for hrac in self.hraci:
            if hrac.id == uzivatel_id:
                return hrac
            return None


