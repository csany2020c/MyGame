class earphone():
    def __int__(self):
        super().__init__()
        self.ar: int
        self.szallitas: int
        self.hany_nap: int
        self.nev: str
        self.szin: str
        self.wireless: bool

F9 = earphone()
F9.ar = 5098
F9.szallitas = 253
F9.hany_nap = 31
F9.nev = "F9 TWS Headphones"
F9.szin = "black"

PCS = earphone()
PCS.ar = 4
PCS.hany_nap = 61
PCS.nev = "PCS Portable Sport Earphone"
PCS.szin = "gray"
PCS.wireless = False

TWS = earphone()
TWS.ar = 1870
TWS.hany_nap = 41
TWS.nev = "Original Tws I12 Earphone"
TWS.szin = "white"

MSR = earphone()
TWS.ar = 965
TWS.hany_nap = 41
TWS.nev = "Magnetic Sports Running Earphone"
TWS.szin = "black"

QKZ = earphone()
QKZ.ar = 965
QKZ.szallitas = 385
QKZ.hany_nap = 61
QKZ.nev = "AK6 Copper Driver HiFi Sport Earphone"
QKZ.szin = "red and blue"
QKZ.wireless = False
