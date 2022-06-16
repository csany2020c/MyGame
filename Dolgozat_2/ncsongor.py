def szamol(a: int, b: int):
    c: int = 0
    if a < 0 and a < b:
        for i in range(0, a * -1 + 1):
            print("1. feladat: " + str(c))
            c = c - 1
    if b < 0 and b < a:
        for i in range(0, b * -1 + 1):
            print("1. feladat: " + str(c))
            c = c - 1
    else:
        if a < b:
            for i in range(0, a + 1):
                print("1. feladat: " + str(c))
                c = c + 1
        if b < a:
            for i in range(0, b + 1):
                print("1. feladat: " + str(c))
                c = c + 1


szamol(16, 6)


def bemenet():
    lista = []
    a = 0
    b = 0
    while a >= 0:
        a = int(input())
        lista.append(a)
    for i in lista:
        b += 1
    else:
        print("2. feladat: " + str(lista[0]), str(lista[b - 2]))


bemenet()


class Bevasarlo:
    def __init__(self):
        super().__init__()
        self.ar: int = 0
        self.nev: str = ""
        self.tomeg: int = 0

    def __str__(self) -> str:
        return "{a}; {n}; {t}".format(a=self.nev, n=self.nev, t=self.tomeg)


bevlista = []
osszar: int = 0

vaj = Bevasarlo()
vaj.nev = "Ráma"
vaj.tomeg = 250
vaj.ar = 500

tej = Bevasarlo()
tej.nev = "Pilos"
tej.tomeg = 1000
tej.ar = 249

kenyer = Bevasarlo()
kenyer.nev = "Komáromi"
kenyer.tomeg = 1000
kenyer.ar = 201

bevlista.append(tej)
bevlista.append(vaj)
bevlista.append(kenyer)
for k in bevlista:
    osszar += k.ar
print("3. feladat: " + str(osszar))
