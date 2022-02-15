import math
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
        #print(self.elso([10,12,13],2))
        #print(str(self.masodik([1,2])))
        #print(str(self.min(1,5)))
        #print(str(self.minList([6,2,1])))
        #print(str(self.mertanisorozat(1,2,3)))
        #print(str(self.negyedik([5,6,9])))
        #print(self.otodik(1,2,3))
        print(self.masodfoku(2,2,1))
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
        megoldas1:float = (-b+(math.sqrt(b**2 - 4 * a * c)))/2 * a
        megoldas2: float = (-b - (math.sqrt(b ** 2 - 4 * a * c))) / 2 * a
        outLista.append(megoldas1)
        outLista.append(megoldas2)
        return outLista








Algorythm()