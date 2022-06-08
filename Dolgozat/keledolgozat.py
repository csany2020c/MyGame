from random import randint


def elso():
    elsoi = input()
    asd = int(elsoi)
    masodik = input()
    fakt = int
    fakt = int(masodik)
    szam = 1
    for i in range(int(masodik)):
        asd = asd * szam
        szam = szam + 1
        print(asd)
        asd = int(elsoi)

def masodik():
    nevlista = []
    while True:
        nev = input("Írj egy nevet:")
        if nev != "":
            nevlista.append(nev)
        else:
            aaaa = (len(nevlista))
            pontaz =randint(1, aaaa)
            print(nevlista[pontaz])
            break



def harmadik():

    class Eger():
        def __init__(self):
            self.gombo : int
            self.vgorgo : bool
            self.fgorgo : bool
            self.gyarto : str

        def __str__(self) -> str:
            return "Gombok száma: {a}, Vízszintes görgő: {b}, Függőleges görgő: {c}, Gyártó: {d}".format(a = self.gombo, b = self.vgorgo, c = self.fgorgo, d = self.gyarto)




    egereklist = []


    eger1: Eger = Eger()
    eger1.gombo = input("Gombok száma:")
    eger1.vgorgo = input("Van vízszintes görgő?:")
    eger1.fgorgo = input("Van függőleges görgő?:")
    eger1.gyarto = input("Gyártó:")
    egereklist.append(eger1)


    eger2: Eger = Eger()
    eger2.gombo = input("Gombok száma:")
    eger2.vgorgo = input("Van vízszintes görgő?:")
    eger2.fgorgo = input("Van függőleges görgő?:")
    eger2.gyarto = input("Gyártó:")
    egereklist.append(eger2)

    eger3: Eger = Eger()
    eger3.gombo = input("Gombok száma:")
    eger3.vgorgo = input("Van vízszintes görgő?:")
    eger3.fgorgo = input("Van függőleges görgő?:")
    eger3.gyarto = input("Gyártó:")
    egereklist.append(eger3)

    for i in egereklist:
        print(i)






harmadik()