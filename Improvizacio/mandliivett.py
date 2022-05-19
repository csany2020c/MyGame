class Golya:
    def __init__(self):
        self.tudrepulni = True
        self.csorhossz = 15
        self.suly = 120
        self.magassag = 100

    def __str__(self) -> str:
        return "Tud repülni = {a}; Csőr hosszúsága = {s}; Súly = {d}; Magasság = {f}".format(a=self.tudrepulni, s=self.csorhossz, d=self.suly, f=self.magassag)


X = Golya()

X.tudrepulni = True
X.csorhossz = 16
X.suly = 125
X.magassag = 105


# HF: + 2 osztaly


class Macska:
    def __init__(self):
        self.tudrepulni = False
        self.labakszama = 4
        self.utodokszama = 4
        self.elethossz = 17

    def __str__(self) -> str:
        return "Tud repülni = {a}; Lábak száma = {s}; Utódok száma = {d}; Élethossz = {f}".format(a=self.tudrepulni, s=self.labakszama, d=self.utodokszama, f=self.elethossz)


Y = Macska()

Y.tudrepulni = False
Y.labakszama = 4
Y.utodokszama = 5
Y.elethossz = 15


class busz:
    def __init__(self):
        self.ferohelyekszama = 50
        self.ulohelyekszama = 40
        self.hosszusag = 12
        self.suly = 10000

    def __str__(self) -> str:
        return "Férőhelyekszáma = {a}; Ülőhelyekszáma = {s}; Hosszúság = {d}; Súly = {f}".format(a=self.ferohelyekszama, s=self.ulohelyekszama, d=self.hosszusag, f=self.suly)


Z = busz()

Z.ferohelyekszama = 40
Z.ulohelyekszama = 30
Z.hosszusag = 11
Z.suly = 8500

H = busz()

H.ferohelyekszama = 50
H.ulohelyekszama = 30
H.hosszusag = 11
H.suly = 8500

P = busz()

P.ferohelyekszama = 50
P.ulohelyekszama = 30
P.hosszusag = 11
P.suly = 8500

#print(X.tudrepulni)
#print(Y.utodokszama)
#print(Z.suly)
# print(X)
# print(Y)
print(Z)
print(H)

k = busz()
print("Kérem a busz súlyát:")
strr = input()
k.suly = int(strr)

print(k)

