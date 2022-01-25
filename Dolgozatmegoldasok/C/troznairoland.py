class Barlang:

    def __init__(self, parsestring: str):
        darabol: list[str] = parsestring.strip().split("\t")
        self.nev: str = darabol[1]
        self.hossz: float = float(darabol[2])
        self.kiterjedes: float = float(darabol[3])
        self.melyseg: float = float(darabol[4])
        self.magassag: float = float(darabol[5])
        self.telepules: str = str(darabol[6])

    def __str__(self) -> str:
        return "{nev}\t{hossz}\t{kiterjedes}\t{melyseg}\t{magassag}\t{telepules}".format(nev=self.nev, hossz=self.hossz, kiterjedes=self.kiterjedes, melyseg=self.melyseg, magassag=self.magassag, telepules=self.telepules)

def Main()
    adat = list[Barlang] = []
    sor: list[str] = open("barlang.txt", mode="r", encoding="utf-8").read().strip().split("\n")
    for i in range(1, len(sor)):
        adat.append(Barlang(sor[i]))
        print()

Main()