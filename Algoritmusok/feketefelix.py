from typing import List
from math import sqrt
#def asd():
    #for i in range(1, 15):
        #print(i)
#def jkl():
        #while(True):
            #asd: int= int(input())
            #if asd == 0:
             #break
#def zui():
        #ok: int = 0
        #asd: int = 1
        #while (asd != 0):
            #asd = int(input())
            #if asd != 0:
                #ok += asd
                #print("Eddigi összeg: {idk}".format(idk=ok))
        #print("Vég összeg: {idk}".format(idk=ok))
#def listaz():
    #lista:List['int'] =(4, 2, 3)
    #szorzat: int = 1
    #for i in lista:
        #print(i)
        #szorzat *= i
        #print("Eredmény: {dsa}".format(dsa=szorzat))

#def rtz():
    #while(True):
        #io: int= 11
        #ku: int= 8
        #if io%ku == 3:
            #break

#def osztoosszeg(szam: int) -> int:
    #szamfele: int = szam // 2 + 1
    #osszeg: int = 0
    #for x in range(1, szamfele):
        #if szam % x == 0:
            #osszeg = osszeg + x
    #return osszeg

#print(osztoosszeg(int(input())))

#def baratiszamok(a:int, b:int)-> bool:
    #return a != b and osztoosszeg(a) == b and osztoosszeg(b) == 0

#print(baratiszamok(10,20))
#print(baratiszamok(33,66))
#print(baratiszamok(77,99))

#def idk(c:int)-> int:
    #d: int = osztoosszeg(c)
    #if c == osztoosszeg(d) and c != d:
        #return d
    #else:
        #print("Nem baratok")

#print(idk(int(input())))

#def sracokvanegyinhalatoromjolvagyok(f:int, g:int)-> List['int']:
    #dani = list
    #szorzat: int = 1


#def pls(k:int)-> int:
    #l: int=osztoosszeg(k)
    #if k + osztoosszeg(l):
        #return l




#print(pls(10))

#def mersenne(o:int)-> bool:
    #z = 2
    #for i in range(0, 1000000):
        #if o == z * i - 1:
            #return True
    #return False

#print(mersenne(int(input())))

def boldog(n:int)-> bool:
    lista: List['int'] = list()
    szam= n

    if szam > 10:
        while n > 0:
            lista.append(n % 10)
            n = n // 10
        szam = pow(lista[0], 2) + pow(lista[1], 2)
        print(szam)
        print(n)
    return lista


print(boldog(94))

#def bemen(ki:int)-> List:
    #be: List['int'] = list()
    #for g in str(abs(ki)):
        #be.append(int (g))
        #return be

#def szamolas(ki: List['int'])-> int:
    #szam: int = 0
    #for i in ki:
        #szam += i*i
    #return szam

#def vege(szam:int)-> bool:
    #mostani = szam
    #megegylista: List['int'] = list()
    #while mostani != 1 and mostani not in megegylista:
        #megegylista.append(mostani)
        #mostani = szamolas(bemen(mostani))
        #print(mostani)
        #print(megegylista)
    #return mostani == 1
#print(vege(2903))




