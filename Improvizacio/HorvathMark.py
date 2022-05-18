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
