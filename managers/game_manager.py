class GameManager:
    def __init__(self):
        self.plocha = None
        self.aktivni_hrac= 0
        self.hraci= []
        self.aktualni_tah = None
        self.casovac= None
        self.game_logger = None
        self.revizor_tahu= None
    def zacni_tah(self, tah):
        self.aktualni_tah = tah
        return tah
    def proved_tah(self):
        if self.aktualni_tah is None:
            return False
        if not self.aktualni_tah.over_platnost(self.plocha):
            return False
        self.aktualni_tah.proved_tah(self.plocha)
        if self.game_logger is not None:
            self.game_logger.uloz_tah(self.aktualni_tah
                                    )
        else:
            pass
        return True
    def mozne_tahy(self):
        return []
    def zrus_tah(self):
        self.aktualni_tah= None
    def uloz_tah(self):
        pass
    def najdi_uzivatele(self, uzivatel_id):
        for hrac in self.hraci:
            if hrac.id == uzivatel_id:
                return hrac
            return None


