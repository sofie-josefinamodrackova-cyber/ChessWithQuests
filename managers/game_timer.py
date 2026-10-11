class GameTimer:
    def __init__(self):
        self.cas_hrace= []
    def nuluj_cas(self):
        self.cas_hrace=[0,0]
    def pocitej_cas(self, hrac_id):
        self.cas_hrace[hrac_id]=hrac_id
