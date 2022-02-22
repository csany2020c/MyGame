import math
from time import time
from typing import List


class Algorythm:
    def __init__(self) -> None:
        super().__init__()
        # szam:str = input()
        # intszam:int = int(szam)
        # logszam: int = int(math.log2(intszam) + 1)
        # max: int = int(math.pow(2, logszam))
        # print(max)
        # vege: str = str()
        # for i in range(logszam):
        #     max = int(max/2)
        #     if (max <= intszam):
        #         vege += "1"
        #         intszam -= max
        #     else:
        #         vege += "0"
        # print(vege)
        #print(self.masikBinaris(63))
        #print(self.paros([2]))
        # t1 = time()
        # print(self.szamoljelodaig(999999))
        # t2 = time()
        # print(t2-t1)
        #print(self.szamolasparos(-12))
        #print(self.masikBinaris(63))
        #print(self.elso([10,12,13],2))
        #print(str(self.masodik([1,2])))
        #print(str(self.min(1,5)))
        #print(str(self.minList([6,2,1])))
        #print(str(self.mertanisorozat(1,2,3)))
        #print(str(self.negyedik([5,6,9])))
        #print(self.otodik(1,2,3))
        #print(self.masodfoku(2,20,2))
        #print(self.relativprim(12000000,2))
        #print(self.helyiertek(125))
        #print(self.tokeletes(6))
        #print(self.helyiertekosszeg(123))
        #print(self.szamjegyeinekszorzata(10))
        #print(self.szamjegyekosszeesoszthato())

    def masikBinaris(self,szam:int) -> str:
        outP:str = ""
        for i in range(8):
            outP += str(int(szam%2))
            szam=int(szam/2)
            print(szam)
        return outP
    def elso(self,lista:List['int'],szam:int) -> List['int']:
        outLista:List['int'] = list()
        for i in lista:
            if(i%szam == 0):
                outLista.append(i)
        return outLista

    def masodik(self,lista:List['int']) -> bool:
        count:int = 0
        for i in lista:
            if (i == 0):
                count+=1
        if (count>0):
            return True
        else:
            return False

    def min(self,szam1:int,szam2:int) -> int:
        return min(szam1,szam2)

    def minList(self,lista:List['int']):
        min:int = 999999
        for i in lista:
            if (i < min):
                min = i
        return min

    def mertanisorozat(self,a1:int,q:int,n:int) -> List['int']:
        outList:List['int'] = list()
        outList.append(a1)
        for i in range(n):
            if (i-1 >= 0):
                outList.append(outList[i-1] * q)
        return outList

    def negyedik(self,lista:List['int']) -> int:
        count:int = 0
        for i in lista:
            count+=i
        return count

    def otodik(self,a1:int,q:int,n:int) -> int:
        return self.negyedik(self.mertanisorozat(a1,q,n))

    def masodfoku(self,a:float,b:float,c:float) -> List['float']:
        outLista:List['float'] = list()
        delta:float = b ** 2 -4 * a * c
        if (delta >= 0):
            outLista.append((-b + math.sqrt(delta)) / (2 * a))
            outLista.append((-b - math.sqrt(delta)) / (2 * a))
        else:
            print("Nem valós gyök")
        return outLista




    def paros(self,szamok:List['int']) -> List['int']:

        parosok:List['int'] = list()
        for i in szamok:
            if (i%2 == 0):
                parosok.append(i)
        return parosok

    def szamoljelodaig(self,szam:int) -> List['int']:
        outLista:List['int'] = list()
        if (szam > 0):
            for i in range(0,szam+1):
                outLista.append(i)
        else:
            szam = -szam
            for i in range(0,szam+1):
                outLista.append(-i)
        return outLista


    def szamolasparos(self,szam:int) -> List['int']:
        return self.paros(self.szamoljelodaig(szam))

    def relativprim(self,szam1:int,szam2:int) -> bool:
        szam1oszthatok:List['int'] = list()
        szam2oszthatok:List['int'] = list()
        for i in range(2,szam1+1):
            if (szam1%i == 0):
                szam1oszthatok.append(i)
        for i in range(2, szam2+1):
            if (szam2%i == 0):
                szam2oszthatok.append(i)
        for i in szam1oszthatok:
            for a in szam2oszthatok:
                if a == i:
                    return False
        return True

    def tokeletes(self,szam:int) -> bool:
        osztok:List['int'] = list()
        szorzat:int = 1
        for i in range(1,szam):
            if (szam%i == 0):
                osztok.append(i)

        for i in osztok:
            szorzat*=i
        return szorzat==szam

    def tokeletesLista(self,eleje:int,vege:int) -> List['int']:
        lista:List['int'] = list()
        for i in range(eleje,vege):
            if (self.tokeletes(i)):
                lista.append(i)
        return lista




    def helyiertek(self,szam:int) -> List['int']:
        outLista:List['int'] = list()
        for i in str(szam):
            outLista.append(int(i))
        return outLista

    def helyiertekosszeg(self,szam:int) -> int:
        lista:List['int'] = self.helyiertek(int(szam))
        count:int=0
        for i in lista:
            count+=i
        return count

    def szamjegyeinekszorzata(self,szam:int) -> List['int']:
        outLista:List['int'] = list()

        for i in range(szam):
            count = 1
            lista:List['int'] = self.helyiertek(i)
            for a in lista:
                count*=a
                print(count)

            if (i == count):
                outLista.append(i)

        return outLista

    def szamjegyekosszeesoszthato(self) -> List['int']:
        outLista:List['int'] = list()
        vege = 999
        for i in range(vege):
            if (i % 15 == 0 and self.helyiertekosszeg(i) == 15):
                outLista.append(i)
        return outLista






Algorythm()