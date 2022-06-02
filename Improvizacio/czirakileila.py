# szállítási költség, ár, szállítási idő

class markers:
    def __init__(self) -> None:
        super().__init__()
        self.szallitasingyenes: bool = False
        self.ar = 0
        self.ido = 0

    def __str__(self) -> bool:
        return strtobool(self.szallitasingyenes) + "\n" + str(self.ar) + "\n" + str(self.ido)


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


# arany
Z = markers()

Z.szallitas = 0
Z.ar = 3
Z.ido = 66

# metal
Y = markers()

Y.szallitas = 301
Y.ar = 3
Y.ido = 66

# feher
S = markers()

S.szallitas = 433
S.ar = 3
S.ido = 46

# fekete
V = markers()

V.szallitas = 0
V.ar = 3
V.ido = 66

# tukor
T = markers()

T.szallitas = 0
T.ar = 3
T.ido = 66

#print(Z)
#print(Y)
#print(S)
#print(V)
#print(T)
