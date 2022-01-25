class Adat:
    def __init__(self, parseString: str) -> str:
        sajatsorom: list['str'] = parseString.strip().split("\t")
        self.id: int = int(sajatsorom[0])
        self.nev: str = sajatsorom[1]
        self.hossz: float = float(sajatsorom[2])
        self.kiterjedes: float = float(sajatsorom[3])
        self.melyseg: float = float(sajatsorom[4])
        self.magassag: float = float(sajatsorom[5])
        self.telepules: str = sajatsorom[6]


    def __str__(self) -> str:
        return "{id}; {nev}; {hossz}; {kiterjedes}; {melyseg}; {magassag}; {telepules}".format(id=self.id, hossz=self.hossz, kiterjedes=self.kiterjedes, melyseg=self.melyseg, magassag=self.magassag, telepules=self.telepules)

class beolvasom:
    def __init__(self):
        fajlolvasas = open("barlang.txt", mode="r", encoding="utf-8")
        adatok: list[Adat] = []
        for i in range(1, len(fajlolvasas)):
            fajl: Adat = Adat(fajlolvasas[i])
            adatok.apppend(fajl)
            print(i)
