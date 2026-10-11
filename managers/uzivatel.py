class Uzivatel:
    def __init__(self, uzivatelske_jmeno, jmeno, email):
        self.uzivatelske_jmeno = uzivatelske_jmeno
        self.jmeno = jmeno
        self.email = email
        self.splnene_kwesty=[]

    def pridej_kwest(self,kwest):
        self.splnene_kwesty.append(kwest)