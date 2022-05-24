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

    def kifizetes(self):
        return self.talalat * self.nyeremeny

    def dontetlen(self):
        a = 0
        for i in self.eredmenyek:
            if i == "X":
                a += 1
        return a

class Fajlokolvasasa:
    def __init__(self, ujdolog: str):
        super().__init__()
        self.ujlista: List[Adatkezeles] = list()
        olvasom = open(ujdolog, "r", encoding="utf-8").read().strip().split("\n")
        for i in olvasom:
            a = Adatkezeles(i)
            self.ujlista.append(a)

        for i in self.ujlista:
            print(i)

        print(f"3. feladat: {len(self.ujlista)}")

        valtozo = 0
        for i in range(0, len(self.ujlista)):
            valtozo += self.ujlista[i].talalat
        print("4. feladat: {a}".format(a=valtozo))

        print("5. feladat: " + self.ujlista[9].kifizetes().__str__())

    def maximum(self):
        maximum: Adatkezeles = self.ujlista[0]
        for i in range(1, len(self.ujlista)):
            if self.ujlista[i].nyeremeny > maximum.nyeremeny:
                maximum = self.ujlista[i]
        return maximum

    def minimum(self):
        minimum: Adatkezeles = None
        for i in range(1, len(self.ujlista)):
            if self.ujlista[i].nyeremeny != 0:
                if min == None:
                    minimum = self.ujlista[i]
            if minimum is not None:
                if self.ujlista[i].nyeremeny > minimum.nyeremeny:
                    minimum = self.ujlista[i]
        return minimum

    def hetesfeladat(self):
        print("{ev} {het}".format(ev=self.maximum().ev, het=self.maximum().het))
        print("{ev} {het}".format(ev=self.minimum().ev, het=self.minimum().het))

    def nyolcas(self):
        print("8. feladat: " + self.ujlista[0].dontetlen().__str__())

    def dontetlen2(self):
        asd1 = 0
        for i in range(0, len(self.ujlista)):
            if self.ujlista[i].dontetlen() == 0:
                asd1 += 1
                if asd1 == 1:
                    print("Nem volt döntetlen nélküli forduló")
                    break
                else:
                    print("Volt döntetlen nélüli forduló")



asd = Fajlokolvasasa("toto.txt")
# asd.hetesfeladat() nem jó
asd.hetesfeladat()
