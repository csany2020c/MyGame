class cipo:
    def __init__(self) -> None:
        super().__init__()
        self.gyarto: str = " "
        self.meret: int = 0
        self.szin: str = " "
        self.stopli: bool = False
        self.anyag: str = " "

    def __str__(self) -> str:
        return "Gyártó: {a}, Méret: {b}, Szín: {c}, FG stoplis?: {d}, Anyaga: {e}".format(a=self.gyarto, b=self.meret, c=self.szin, d=self.stopli, e=self.anyag)

csuka = cipo()
csuka.gyarto = "Nike"
csuka.meret = 41
csuka.szin = "Fekete"
csuka.stopli = False
csuka.anyag = "Bor"
print(csuka)

csuka = cipo()
csuka.gyarto = "Adidas"
csuka.meret = 40
csuka.szin = "Fehér"
csuka.stopli = True
csuka.anyag = "Műanyag"
print(csuka)

csuka = cipo()
csuka.gyarto = "Puma"
csuka.meret = 42
csuka.szin = "Neonzöld, Neonsárga"
csuka.stopli = False
csuka.anyag = "Műbőr"
print(csuka)
cipo()