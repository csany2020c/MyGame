from typing import List
from time import time

class Algoritmusok():
    def __init__(self) -> None:
        super().__init__()
        self.listam: List['int'] = list()
        t1 = time()
        #print(self.boldogszam(230))
        print(self.boldokketkozott(1, 10000))
        print(self.boldoggyorsites(23))
        t2 = time()
        print(t2 - t1)

    def helyiertek(self, be:int) -> List['int']:
        ki: List['int'] = list()
        for i in str(abs(be)):
            ki.append(int(i))
        return ki

    def negyzetosszeg(self, be:List['int']) -> bool:
        szam :int = 0
        for i in be:
            szam += i*i
        return szam

    def boldogszam(self, beszam: int) -> bool:
        aktszam :int = beszam
        lista :List['int'] = list()
        while aktszam != 1 and aktszam not in lista:
            lista.append(aktszam)
            aktszam = self.negyzetosszeg(self.helyiertek(aktszam))
        return aktszam == 1

    #2.

    def boldokketkozott(self, egy:int, ketto:int) -> List['int']:
        for i in range(egy, ketto):
            if self.boldogszam(i):
                self.listam.append(i)
            self.listam.append(i)
        return self.listam


    #4
    def boldoggyorsites(self, beszam:int)-> bool:
        for i in self.listam:
            return beszam == i


Algoritmusok()