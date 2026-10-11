class RevizorTahu:
    def __init__(self, herni_plocha):
        self.herni_plocha = herni_plocha
        self.tah = None
    def simulate_move(self, tah):
        self.tah = tah
        return tah.proved_tah
    @property
    def check_sach(self, barva_hrace=None, figurka_barva=None):
        pozice_krale = None
        for y in range(8):
            for x in range(8):
                figurka = self.herni_plocha.vrat_obsah((x,y))
                if figurka is not None and figurka.nazev == "Kral" and figurka_barva == barva_hrace:
                    pozice_krale = (x,y)
                    break
            if pozice_krale:
                break
        if not pozice_krale:
            return False
        kx, ky = pozice_krale

        for y in range(8):
            for x in range(8):
                figurka = self.herni_plocha.figurka.vrat_obsah((x,y))
                if figurka is not None and figurka.barva != barva_hrace:
                    pass
        return False

    @property
    def check_mat(self, barva=None):
        is_sach = self.check_sach(barva.hrace)
        if not is_sach:
            return False
    def check_pat(self):
        is_sach = self.check_sach
        if is_sach:
            return False
        

    