class Kerekpar():
    def __init__(self):
        super().__init__()
        self.elsovalto: int = 3
        self.hatsovalto: int = 7
        self.szin: str = "piros"
        self.szin2: str = "kék"
        self.fajta: str = "terep"
        self.kulacstarto: int = 1

    def __str__(self) -> str:
        return "Elsőváltó = {a}; Hátsóváltó = {b}; Szín = {c}; Szín2 = {d}; Fajtája = {e}; Kulacstartó szám = {f}".format(a = self.elsovalto, b = self.hatsovalto, c = self.szin, d = self.szin2, e = self.fajta, f = self.kulacstarto)


enkerekpar = Kerekpar()
enkerekpar.hatsovalto = 6
enkerekpar.szin = "fekete"
enkerekpar.szin2 = "narancs"


randomkerekpar = Kerekpar()
randomkerekpar.kulacstarto = 5
randomkerekpar.hatsovalto = 8
randomkerekpar.szin = "zöld"
randomkerekpar.szin2 = "narancs"
randomkerekpar.fajta = "országúti"

felhasznalokerekpar = Kerekpar()
felhasznalokerekpar.elsovalto = int(input("Hány fokozatú az első váltó? "))
felhasznalokerekpar.hatsovalto = int(input("Hány fokozatú a hátsó váltó? "))
felhasznalokerekpar.szin = input("Milyen színű?(1. szín) ")
felhasznalokerekpar.szin2 = input("Milyen színű?(2. szín) ")
felhasznalokerekpar.fajta = input("Milyen fajtájú a kerékpár? ")
felhasznalokerekpar.kulacstarto = int(input("Mennyi kulacstartója van? "))

print(felhasznalokerekpar)
#print(Kerekpar())
#print(enkerekpar)
#print(randomkerekpar)
#HF még 2 osztály, példányok belőlük


class Telefon():
    def __init__(self):
        super().__init__()
        self._5G: bool = True
        self.keret: bool = False
        self.szin: str = "fekete"
        self.ram_GB: int = 4

    def __str__(self) -> str:
        return "5G = {g}; Keret = {h}; Szín = {i}; Ram GB-ban = {j}".format(g = self._5G, h = self.keret, i = self.szin, j = self.ram_GB)


entelefon = Telefon()
entelefon.szin = "white"
entelefon.keret = True

#print(Telefon())
#print(entelefon)

class TV():
    def __init__(self):
        super().__init__()
        self.smartTV: bool = False
        self.radio: bool = True
        self.ID_channel: bool = False
        self.szin: str = "gray"

    def __str__(self) -> str:
        return "SmartTV = {k}; Radio = {l}; ID channel = {m}; Szín = {n}".format(k = self.smartTV, l = self.radio, m = self.ID_channel, n = self.szin)


enTV = TV()
enTV.smartTV = True
enTV.ID_channel = True
enTV.szin = "black"

#print(enTV)
#print(TV())

