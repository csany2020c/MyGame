#ar, szallitasi koltseg, szallitasi ido, tulajdonsag, termek neve
from typing import List

class Hangszoro:
    def __init__(self) -> None:
        self.ar: int = 0
        self.szallitasikoltseg:int = 0
        self.szallitasiido:str = ""
        self.tudnivalok:str = ""
        self.termeknev:str = ""
        self.hibase:bool = True

    def __str__(self) -> str:
        return "Termék neve: {x}, Ára: {a}, Szállításiköltség: {b}, Szállításiidő: {c}, Tudnivalók: {d}, Van-e valami hibája a terméknek?: {z}".format(x=self.termeknev,a=self.ar, b=self.szallitasiido, c=self.szallitasikoltseg, d=self.tudnivalok, z=self.hibase)

    def teljesar(self) -> int:
        return self.ar + self.szallitasikoltseg


def strtobool(value: str) -> bool:
    if value.upper() == "Igen" or value.upper() == "True":
        return True
    if value.upper() == "Nem" or value.upper() == "Hamis" or value.upper() == "False":
        return False
    return None


def boolbeolvas(prompt: str) -> bool:
    while True:
        be: str = input(prompt + " (I/N): ")
        if be.upper() == "I" or be.upper() == "Y":
            return True
        if be.upper() == "N":
            return False

def intbeolvas(prompt: str, min: int = 0, max: int = 100) -> int:
    while True:
        be: str = input(prompt + " (" + str(min) + " - " + str(max) + "): ")
        try:
            i: int = int(be)
            if i >= min and i <= max:
                return i
            else:
                print("Hibás érték! A szám túl nagy vagy túl kicsi!")
        except:
            print("Hibás érték! Ebbe a mezőbe csak szám kerülhet!")


lista: List[Hangszoro] = list()

while boolbeolvas("Akar hangszórót felvinni a rendszerbe?"):
    JBL = Hangszoro()
    JBL.ar = intbeolvas("Hangszóró ára:", 5000, 100000)
    JBL.szallitasikoltseg = input("Szállítási költség :")
    JBL.szallitasiido = intbeolvas("Szállítási idő(nap):")
    JBL.tudnivalok = input("tudnivalók")
    JBL.termeknev = input("Termék neve:")
    JBL.hibase = boolbeolvas("Van hibája?")
    lista.append(JBL)

for i in lista:
    print(i)
#exit()
fn = "KisKornel.txt"
fr = open(fn, mode="r", encoding="utf-8")
sorok = fr.read().strip().split("\n")
i:int=0
while i < len(sorok):
    a = Hangszoro()
    a.termeknev = sorok[i]
    i += 1
    a.ar = (sorok[i])
    i += 1
    a.szallitasikoltseg = (sorok[i])
    i += 1
    a.szallitasiido = (sorok[i])
    i += 1
    a.tudnivalok = sorok[i]
    i += 1
    a.hibase = (sorok[i])
    lista.append(a)
fr.close()
for i in lista:
    print(i)



MP3 = Hangszoro()
MP3.ar = 1300
MP3.szallitasikoltseg = 0
MP3.szallitasiido = "30 nap"
MP3.tudnivalok = "A termék világos kék, 80 mA akkumlátor, 48 órés készenléti idő"
MP3.termeknev = "USB in-line card MP3 player"
MP3.hibase = False
#print(MP3)
BoomBox = Hangszoro()
BoomBox.ar = 3500
BoomBox.szallitasikoltseg = 0
BoomBox.szallitasiido = "31 nap"
BoomBox.tudnivalok = "teljesitmény 60W, vízálló"
BoomBox.termeknev = "JBL Boombox Boom Box 3 2"
BoomBox.hibase = False
#print(BoomBox)
#print(JBL, MP3, BoomBox)
lista: List[Hangszoro] = list()
#lista.append(JBL)
#lista.append(BoomBox)
#lista.append(MP3)
#for i in lista:
#    print(i)
#    print(i.teljesar())
#print(lista)
#print(JBL)