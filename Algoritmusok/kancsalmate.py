from typing import List
import math
class igen:
    def __init__(self) -> None:
        super().__init__()
        print(self.masodfoku(5,20,2))
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
    #0.0
    def maradek(self, szam: List['int'], oszto):
        kimenet: List['int'] = list()
        for i in range(len(szam)):
            if szam[i] % oszto == 0:
                kimenet.append(szam[i])
    #0.1
    def vanenulla(self,szam: List['int']):
        kimenet = False
        for i in range(len(szam)):
            if szam[i] == 0:
              kimenet = True
        return kimenet
    #1
    def min(self, egyik, masik):
        kisebb = 0
        if egyik > masik:
            kisebb =kisebb + masik
        if egyik < masik:
            kisebb =kisebb + egyik
        return kisebb
    #2
    def minlist(self, szam: List['int']):
        legkisebb = szam[1]
        for i in range(len(szam)):
            if szam[i] < legkisebb:
                legkisebb = szam[i]
        return legkisebb

    #3
    def mertan(self, a1, q, n):
        szam = 0
        self.sorozat: List['int'] = list()
        for i in range(n):
            a1 = a1 * q
            self.sorozat.append(a1)
        return self.sorozat

    #4
    def add(self, szam: List['int']):
        start = 0
        for i in range(len(szam)):
            start = start + szam[i]
        return start

    #5
    def mix(self):
        print(self.add(self.mertan(1, 2, 2)))

    #6
    def masodfoku(self,a,b,c):
        gyokok: List['int'] = list()
        b2 = math.pow(b, 2)
        ac = 4 * (a*c)
        aa = 2 * a
        gyokalatt = math.sqrt(b2 - ac)
        lepes1 = -b + gyokalatt
        gyok1 = lepes1 / 2 * a
        lepes2 = -b - gyokalatt
        gyok2 = lepes2 / 2 * a
        gyokok.append(gyok1)
        gyokok.append(gyok2)
        return gyokok










igen()