class Artwork:
    def __init__(self, cim, szerzo, ev):
        self.cim = cim
        self.szerzo = szerzo
        self.ev = ev

class Sculpture(Artwork):
    def __init__(self, cim, szerzo, ev, anyag):
        super().__init__(cim, szerzo, ev)
        self.anyag = anyag

class Painting(Artwork):
    def __init__(self, cim, szerzo, ev, technika):
        super().__init__(cim, szerzo, ev)
        self.technika = technika

class Building:
    def __init__(self, nev, epitesz, ev, helyszin):
        self.nev = nev
        self.epitesz = epitesz
        self.ev = ev
        self.helyszin = helyszin
