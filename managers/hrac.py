class Hrac:
    def __init__(self, uzivatel, barva):
        self.uzivatel = uzivatel
        self.barva = barva
    def get_elo_rating(self):
        return self.uzivatel.elo