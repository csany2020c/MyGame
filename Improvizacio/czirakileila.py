# szállítási költség, ár, szállítási idő
from typing import List


class filcek:
    def __init__(self) -> None:
        super().__init__()
        self.fajta: str = ""
        self.szallitasingyenes: bool = False
        self.ar = 0
        self.ido = 0

    def __str__(self) -> str:
        return self.fajta + "\n" + str(self.szallitasingyenes) + "\n" + str(self.ar) + "\n" + str(self.ido)


def strtobool(value: str) -> bool:
    if value.upper() == "I":
        return True
    if value.upper() == "N":
        return False
    return None


def beolvasas(prompt: str) -> bool:
    while True:
        be: str = input(prompt + " (I/N): ")
        if be.upper() == "I":
            return True
        if be.upper() == "N":
            return False


def intbeolvasas(prompt: str, min: int = 0, max: int = 100) -> int:
    while True:
        be: str = input(prompt + " (" + str(min) + " - " + str(max) + "): ")
        try:
            i: int = int(be)
            if i >= min and i <= max:
                return i
        except:
            pass


A = filcek()

A.fajta = "Arany"
A.szallitas = True
A.ar = 3
A.ido = 66


M = filcek()

M.fajta = "Metálos"
M.szallitas = False
M.ar = 3
M.ido = 66


H = filcek()

H.fajta = "Fehér"
H.szallitas = False
H.ar = 3
H.ido = 46


K = filcek()

K.fajta = "Fekete"
K.szallitas = True
K.ar = 3
K.ido = 66


T = filcek()

T.fajta = "Tükröződő"
T.szallitas = True
T.ar = 3
T.ido = 66

l: List['Filcek'] = list()

l.append(A)
l.append(M)
l.append(H)
l.append(K)
l.append(T)

for i in l:
    print(i)


#print(A)
#print(M)
#print(H)
#print(K)
#print(T)
