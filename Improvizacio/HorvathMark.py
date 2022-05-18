class Kerekpar():
    def __init__(self):
        super().__init__()
        self.elsovalto: int = 3
        self.hatsovalto: int = 7
        self.szin: str = "piros"
        self.szin2: str = "kek"
        self.fajta: str = "terep"
        self.kulacstarto: int = 1


enkerekpar = Kerekpar()
enkerekpar.hatsovalto = 6
enkerekpar.szin = "fekete"
enkerekpar.szin2 = "narancs"

print(enkerekpar.fajta)

#HF még 2 osztály, példányok belőlük


class Telefon():
    def __init__(self):
        super().__init__()
        self._5G: bool = True
        self.keret: bool = False
        self.szin: str = "fekete"
        self.ram_GB: int = 4

entelefon = Telefon()
entelefon.szin = "white"
entelefon.keret = True

#print(entelefon._5G)

class TV():
    def __init__(self):
        super().__init__()
        self.smartTV: bool = False
        self.radio: bool = True
        self.ID_channel: bool = False
        self.szin: str = "gray"

enTV = TV()
enTV.smartTV = True
enTV.ID_channel = True
enTV.szin = "black"

#print(enTV.radio)

