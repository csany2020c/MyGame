#szállítási költség, ár, szállítási idő

class markers:
    def __init__(self) -> None:
        self.szallitas = 0
        self.ar = 3
        self.ido = 66

    def __str__(self) -> str:
        return "Szállítási költség = {a}; Ár = {s}; Szállítási idő = {d}".format(a=self.szallitas, s=self.ar, d=self.ido)

    #def osszesen(self) ->int:
        #return self.szallitas + self.ar



#arany
Z = markers()

Z.szallitas = 0
Z.ar = 3
Z.ido = 66

#metal
Y = markers()

Y.szallitas = 301
Y.ar = 3
Y.ido = 66

#feher
S = markers()

S.szallitas = 433
S.ar = 3
S.ido = 46

#fekete
V = markers()

V.szallitas = 0
V.ar = 3
V.ido = 66

#tukor
T = markers()

T.szallitas = 0
T.ar = 3
T.ido = 66

print(Z)
print(Y)
print(S)
print(V)
print(T)



