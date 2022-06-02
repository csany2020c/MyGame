class Kerekpar():
    def __init__(self):
        super().__init__()
        self.elsovalto: int = 3
        self.hatsovalto: int = 7
        self.szin: str = "piros"
        self.szin2: str = "kék"
        self.fajta: str = "terep"
        self.kulacstarto: int = 1
        self.csengo: bool = False

    def __str__(self) -> str:
        return "Elsőváltó = {a}; Hátsóváltó = {b}; Szín = {c}; Szín2 = {d}; Fajtája = {e}; Kulacstartó szám = {f}; Van-e csengő = {g}".format(a = self.elsovalto, b = self.hatsovalto, c = self.szin, d = self.szin2, e = self.fajta, f = self.kulacstarto, g = self.csengo)

def boololvasas(prompt: str) -> bool:
    while True:
        be: str = input(prompt + "(I/N):")
        if be.upper() == "I" or be.upper() == "Y":
            return True
        if be.upper() == "N":
            return False

def intbeolvasas(prompt = str, min:int = 0, max:int = 100) -> int:
    while True:
        be: str = input(prompt + " (" + str(min) + " - " + str(max) + "): ")
        try:
            i: int = int(be)
            if i >= min and i <= max:
                return i
        except:
            pass


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
felhasznalokerekpar.elsovalto = intbeolvasas("Hány fokozatú az első váltó? ", 1, 3)
felhasznalokerekpar.hatsovalto = intbeolvasas("Hány fokozatú a hátsó váltó? ", 1, 8)
felhasznalokerekpar.szin = input("Milyen színű?(1. szín) ")
felhasznalokerekpar.szin2 = input("Milyen színű?(2. szín) ")
felhasznalokerekpar.fajta = input("Milyen fajtájú a kerékpár? ")
felhasznalokerekpar.kulacstarto = intbeolvasas("Mennyi kulacstartója van? ", 0, 5)
felhasznalokerekpar.csengo = boololvasas("Van rajta csengő?")

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

