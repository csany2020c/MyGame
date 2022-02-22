from typing import List
import math

#def fakt(n: int) -> int:
    #szorzat = 1
    #for i in range(2, n + 1):
        #szorzat *= i

    #return szorzat


#for i in range(1, 5000):
        #print(fakt(i))

#def oszt():
    #inp = int(input())
    #lista = []
    #oszto = 1
    #for i in range(inp):
        #if inp % oszto == 0:
            #lista.append(oszto)
        #oszto = oszto + 1

    #print(lista)

#def oszt2(n: int) -> int:
    #l: list['int'] = list()
    #for i in range(1, n + 1):
        #if n % i == 0:
            #l.append(i)

    #return l


# def prim():
#     inp = int(input())
#     lista =[]
#     mb = 1
#     mb2 = False
#     for i in range(inp):
#         if inp % mb == 0:
#             lista.append(mb)
#         mb = mb + 1
#
#     if len(lista) == 2:
#         mb2 = True
#     print(lista)




# class Algorythm:
#     def __init__(self) -> None:
#         super().__init__()
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
        # print(self.masodfoku(2,2,1))
    # def masikBinaris(self,szam:int) -> str:
    #     outP:str = ""
    #     for i in range(8):
    #         outP += str(int(szam%2))
    #         szam=int(szam/2)
    #         print(szam)
    #     return outP
    # def elso(self,lista:List['int'],szam:int) -> List['int']:
    #     outLista:List['int'] = list()
    #     for i in lista:
    #         if(i%szam == 0):
    #             outLista.append(i)
    #     return outLista
    #
    # def masodik(self,lista:List['int']) -> bool:
    #     count:int = 0
    #     for i in lista:
    #         if (i == 0):
    #             count+=1
    #     if (count>0):
    #         return True
    #     else:
    #         return False
    #
    # def min(self,szam1:int,szam2:int) -> int:
    #     return min(szam1,szam2)
    #
    # def minList(self,lista:List['int']):
    #     min:int = 999999
    #     for i in lista:
    #         if (i < min):
    #             min = i
    #     return min
    #
    # def mertanisorozat(self,a1:int,q:int,n:int) -> List['int']:
    #     outList:List['int'] = list()
    #     outList.append(a1)
    #     for i in range(n):
    #         if (i-1 >= 0):
    #             outList.append(outList[i-1] * q)
    #     return outList
    #
    # def negyedik(self,lista:List['int']) -> int:
    #     count:int = 0
    #     for i in lista:
    #         count+=i
    #     return count
    #
    # def otodik(self,a1:int,q:int,n:int) -> int:
    #     return self.negyedik(self.mertanisorozat(a1,q,n))
    #
    # def masodfoku(self,a:float,b:float,c:float) -> List['float']:
    #     outLista:List['float'] = list()
    #     megoldas1:float = (-b+(math.sqrt(b**2 - 4 * a * c)))/2 * a
    #     megoldas2: float = (-b - (math.sqrt(b ** 2 - 4 * a * c))) / 2 * a
    #     outLista.append(megoldas1)
    #     outLista.append(megoldas2)
    #     return outLista


def are_coprime(a, b):
    asd = 1

    for i in range(1, a + 1):
        if a % i == 0 and b % i == 0:
            asd = i

    return asd == 1

elso = int(input('Első szám: '))
masodik = int(input('Második szám: '))

if are_coprime(elso, masodik):
    print('%d és %d relativ prim' % (elso, masodik))
else:
    print('%d és %d nem relativ prim' % (elso, masodik))