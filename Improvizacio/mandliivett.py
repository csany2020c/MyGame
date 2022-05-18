class Golya:
    def __init__(self):
        self.tudrepulni = True
        self.csorhossz = 15
        self.suly = 120
        self.magassag = 100


X = Golya()

X.tudrepulni = True
X.csorhossz = 16
X.suly = 125
X.magassag = 105

print(X.tudrepulni)


# HF: + 2 osztaly


class Macska:
    def __init__(self):
        self.tudrepulni = False
        self.labakszama = 4
        self.utodokszama = 4
        self.elethossz = 17


Y = Macska()

Y.tudrepulni = False
Y.labakszama = 4
Y.utodokszama = 5
Y.elethossz = 15

print(Y.utodokszama)


class busz:
    def __init__(self):
        self.ferohelyekszama = 50
        self.ulohelyekszama = 40
        self.hosszusag = 12
        self.suly = 10000


Z = busz()

Z.ferohelyekszama = 40
Z.ulohelyekszama = 30
Z.hosszusag = 11
Z.suly = 8500

print(Z.suly)

