from typing import List


class Adatkezeles:
    def __init__(self, szoveg: str) -> None:
        super().__init__()
        kitolt: List['str'] = szoveg.strip().split(" ")
        self.ev: int = int(kitolt[0])
        self.het: int = int(kitolt[1])
        self.fordulo: int = int(kitolt[2])
        self.talalat: int = int(kitolt[3])
        self.nyeremeny: int = int(kitolt[4])
        self.eredmenyek: str = kitolt[5]

    def __str__(self) -> str:
        return "Év = {a}, Hét = {b}, Forduló = {c}, Találat = {d}, Nyeremény = {e}, Eredmények = {f}".format(a=self.ev, b=self.het, c=self.fordulo, d=self.talalat, e=self.nyeremeny, f=self.eredmenyek)

class Fajlokolvasasa:
    def __init__(self, ujdolog: str):
        super().__init__()
        ujlista: List[Adatkezeles] = list()
        olvasom = open(ujdolog, "r", encoding="utf-8").read().strip().split("\n")
        for i in olvasom:
            a = Adatkezeles(i)
            ujlista.append(a)

        for i in ujlista:
            print(i)



Fajlokolvasasa("toto.txt")