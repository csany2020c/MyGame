from typing import TextIO
from typing import List

class cipo:
    def __init__(self) -> None:
        super().__init__()
        self.meret: int
        self.szin: str
        self.fajta: str
        self.fuzos: bool

    def __str__(self) -> str:
        return "Méret: {a}, Szín: {s}, Fajta: {d}, Fűzős-e: {f}".format(a=self.meret, s=self.szin, d=self.fajta, f=self.fuzos)


# asd = cipo()
# asd.meret = 40
# asd.szin = "fekete"
# asd.fajta = "futócipő"
# asd.fuzos = True
#
# print(asd)

def strtobool(value: str) -> bool:
    if value.upper() == "I" or value.upper() == "Y" or value.upper() == "TRUE":
        return True
    if value.upper() == "N" or value.upper() == "FALSE":
        return False
    return None


def boolbeolvas(prompt: str) -> bool:
    while True:
        be: str = input(prompt + " (Aha/Nemkösz): ")
        if be.upper() == "AHA" or be.upper() == "JA":
            return True
        if be.upper() == "NEMKÖSZ":
            return False

def boolbeolvasfuzonel(prompt: str) -> bool:
    while True:
        be: str = input(prompt + " (Igen/Nem): ")
        if be.upper() == "IGEN" or be.upper() == "PERSZE":
            return True
        if be.upper() == "Nem":
            print("Jó béna vagy")
            return False


def intbeolvas(prompt: str, min: int = 30, max: int = 50) -> int:
    while True:
        be: str = input(prompt + " (" + str(min) + " - " + str(max) + "): ")
        try:
            i: int = int(be)
            if i >= min and i<=max:
                return i
        except:
            pass


l: List['cipo'] = list()


while boolbeolvas("Kell cipő testvérem?"):
    hi = cipo()
    hi.meret = intbeolvas("Csapasd a méretet: ")
    hi.szin = input("Most jöhet a szín: ")
    hi.fajta = input("Fajtája: ")
    hi.fuzos = boolbeolvasfuzonel("Tudsz kötni?")
    l.append(hi)