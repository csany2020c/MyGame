from typing import List


class AliExpress:

    def __init__(self) -> None:
        super().__init__()
        self.hangszer : str = "transparent"
        self.vankolts: bool = True
        self.szallkolts : int =0
        self.ar: int = 0
        self.szallido: int = 0
        self.honnanjon: str = "transparent"
        #self.teljesar: int = self.ar + self.szallkolts

    def __str__(self) -> str:
        return "Tárgy : {a}, Van kiszállítási díj : {b}, Szállítási költség = {c}, Ár : {d} Ft, Teljes ár: {x}, Kiszállítási idő : {e} hónap, Innen érkezik : {f}".format(x = self.teljesar, a = self.hangszer, b = self.vankolts, c = self.szallkolts, d = self.ar, e = self. szallido, f = self.honnanjon)

#AliExpress()

dob = AliExpress()
dob.hangszer = "Dobkészlet"
dob.vankolts = True
dob.ar = 24330
dob.szallkolts = 34941
dob.szallido = 3
dob.honnanjon = "Kína"
dob.teljesar = dob.ar + dob.szallkolts

klarinet = AliExpress()
klarinet.hangszer = "Klarinét bambusz kiegészítő"
klarinet.vankolts = False
klarinet.ar = 1145
klarinet.szallido = 3.5
klarinet.honnanjon = "Kanada"
klarinet.teljesar = klarinet.ar + klarinet.szallkolts

hegedu = AliExpress()
hegedu.hangszer = "Hegedű"
hegedu.vankolts = True
hegedu.ar = 178669
hegedu.szallkolts = 17630
hegedu.szallido = 3
hegedu.honnanjon = "Ismeretlen"
hegedu.teljesar = hegedu.ar + hegedu.szallkolts

print(dob)
print(klarinet)
print(hegedu)

list = AliExpress()
lista: list = []
lista.append(dob)
lista.append(klarinet)
lista.append(hegedu)

#print(lista)

#for i in lista:
    #print(i)

#print(len(lista),"tárgy van a bevásárlókocsiban.")

#if len(lista) >= 2:
    #print("A kosárba csak 2 tárgy fér el.")
    #lista.remove(dob)

#print(len(lista),"tárgy van a bevásárlókocsiban. Egy tárgy ell lett távolítva.")
#print("")

