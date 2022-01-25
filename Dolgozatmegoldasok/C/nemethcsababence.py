class barlang:

    def __init__(self, parseString : str):
        eldarabolt: list[str] = parseString.strip().split('\t')
        self.nev:str = str(eldarabolt[1])
        self.hossz:float = float(eldarabolt[2])
        self.kiterjedes:float = float(eldarabolt[3])
        self.melyseg:float = float(eldarabolt[4])
        self.magassag:float = float(eldarabolt[5])
        self.telepulesneve:str = str(eldarabolt[6])

    def __str__(self):
        return "{nev}\t{hossz}\t{kiterjedes}\t{melyseg}\t{magassag}\t{telepulesneve}".format(nev=self.nev, hossz=self.hossz, kiterjedes=self.kiterjedes, melyseg=self.melyseg, magassag=self.magassag, telepulesneve=self.telepulesneve)


def main():
    sorok :list[str] = open('barlang.txt', 'r', encoding='utf-8').read().strip().split("\n")
    adatok:list[barlang] = []
    print(sorok)

main()