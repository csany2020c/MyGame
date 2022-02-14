import plistlib
from typing import List

class igen:
    def __init__(self) -> None:
        super().__init__()

    def faktorialis(self):
        x = 1
        a = int(input())
        for i in range(1, a+1):
            x = x * i
        print(x)

    def osztok(self):
        self.lista = list()
        szam = int(input())
        for i in range(1, szam + 1):
            if szam % i == 0:
                self.lista.append(i)
        print(self.lista)

    def prim(self):
        prim = False
        if len(self.lista) == 2:
            prim = True
            return prim

    def paroslista(self, szamok: list) -> List['int']:
        parosok :List['int'] = list()
        for i in range(len(szamok)):
            if szamok[i] % 2 == 0:
                parosok.append(szamok[i])
        return parosok

    def szamolo(self, szam) -> List['int']:
        lista: List['int'] = list()
        if szam < 0:
            szam = -szam
            for i in range(szam):
                lista.append(-i-1)
        else:
            for i in range(szam):
                lista.append(i+1)
        return lista

    def parosszamolo(self, szam) -> List['int']:
        lista : List['int'] = list()
        for i in range(szam):
            if i % 2 == 0:
                lista.append(i)
        return lista






''
igen()