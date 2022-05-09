from typing import List


class Data:

    def __init__(self, parsestring: str) -> None:
        super().__init__()
        fields: List['str'] = parsestring.split(" ")
        self.ev: int = int(fields[0])
        self.het: int = int(fields[1])
        self.fordulo: int = int(fields[2])
        self.t13p1: int = int(fields[3])
        self.ny13p1: int = int(fields[4])
        self.eredmenyek: str = str(fields[5])

    def __str__(self) -> str:
        return "ev = {ev}; het = {het}; fordulo = {fordulo}; t13p1 = {t13p1}; ny13p1 = {ny13p1};  eredmenyek = {eredmenyek}".format(ev=self.ev, het=self.het, fordulo=self.fordulo, t13p1=self.t13p1, ny13p1=self.ny13p1, eredmenyek=self.eredmenyek)


class Main:
    def __init__(self) -> None:
        super().__init__()
        #2.feladat
        olvasas: List['str'] = open("toto.txt", 'r', encoding="utf-8").read().strip().split(sep="\n")
        lista: List[Data] = list()
        for i in range(1, len(olvasas)):
            lista.append(Data(olvasas[i]))

        print("Az egyes és a kettes feladat már megoldva! ☺☻☺")

        #3. feladat
        print("3. feladat ☻")
        self.valt = 0
        for j in range(len(lista)):
            self.valt += lista[j].fordulo
        print(f"{self.valt} forduló adatai találhatók az állományban.")

        #4. feladat
        print("4. feladat ☻")
        self.valt2 = 0
        for k in range(len(lista)):
            self.valt2 += lista[k].t13p1
        print(f"{self.valt2} db telitalálatos szelvény van.")

        #5. feladat
        print("5. feladat ☻")
        valtkettoesfel = 0
        for l in range(len(lista)):
            valtkettoesfel += lista[l].t13p1 * lista[l].ny13p1
        print(f"{valtkettoesfel} Ft a kifizetett pénz mennyisége.")

        #nincs 6. feladat ☻☻☻

        #7. feladat
        print("7. feladat ☻")
        self.valt3 = 0
        for a in range(0, len(lista)):
            if self.valt3 < lista[a].ny13p1:
                self.valt3 = lista[a].ny13p1
            if self.valt3 == lista[a].ny13p1:
                print("Legnagyobb = ", lista[a].ev, lista[a].het)
        self.valt4 = 0
        for s in range(0, len(lista)):
            if self.valt4 > lista[s].ny13p1:
                self.valt4 = lista[s].ny13p1
            if self.valt4 == lista[s].ny13p1:
                print("Legkisebb = ", lista[s].ev, lista[s].het)

        #8. feladat
        print("8. feladat ☻")
        self.valt5 = 0
        for d in range(0, len(lista)):
            for d in str(lista[d].eredmenyek):
                if d == "X":
                    self.valt5 += 1
        print(f"{self.valt5} db döntetlen volt.")

        #9.feladat
        print("9. feladat ☻")
        self.valt6 = 0
        for f in range(0, len(lista)):
            for f in str(lista[f].eredmenyek):
                if str(f) == "X":
                    self.valt6 += 1
                    if self.valt6 == 1:
                        print("Tartalmaz döntetlen!")
                        break
                    else:
                        print("Nem tartalmaz döntetlent!")
                        break
            print("Hogy mennyit foglalkoztam vele?, A válaszom csak annyi, hogy a vizsgán kevesebb idő alatt kellene. ")
            break




Main()
