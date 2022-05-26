class Rendeles:
    def __init__(self):
        super().__init__()
        self.termeknev: str="asd"
        self.ar: int
        self.szallitasikoltseg: int
        self.kiszallitasiido: int

    def __str__(self) -> str:
        return "Termék neve: {a}; Ár: {b}; Szalltási Költség: {c};  Kiszallítási idő: {d};".format(a=self.termeknev,b=self.ar,c=self.szallitasikoltseg,d=self.kiszallitasiido)


Rendeles()

termek1 = Rendeles()
termek1.termeknev = "Szemüveg"
termek1.ar = 6127
termek1.szallitasikoltseg = 555
termek1.kiszallitasiido = 30
termek1.szin = "fekete"
termek1.suly = 24
print(termek1)

termek2 = Rendeles()
termek2.termeknev = "Telefon"
termek2.ar = 101709
termek2.szallitasikoltseg = 0
termek2.kiszallitasiido = 30
termek2.akummlator = 5000
termek2.screen = 6.43
print(termek2)

termek3 = Rendeles()
termek3.termeknev = "Hangszoró"
termek3.ar = 5827
termek3.szallitasikoltseg = 1638
termek3.kiszallitasiido = 15
termek3.vizallosag = True
termek3.bluetoothversion = 5.0
print(termek3)

termek4 = Rendeles()
termek4.termeknev = "Drón"
termek4.ar = 59242
termek4.szallitasikoltseg = 0
termek4.kiszallitasiido = 60
termek4.zoom = "50x"
termek4.remotecontroldistance = 1200
print(termek4)

termek5 = Rendeles()
termek5.termeknev = "Okos Óra"
termek5.ar = 21863
termek5.szallitasikoltseg = 0
termek5.kiszallitasiido = 85
termek5.type = "Lithium polymer"
termek5.chargingtime = 2
print(termek5)











