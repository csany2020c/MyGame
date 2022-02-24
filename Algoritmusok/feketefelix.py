from typing import List
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
def listaz():
    lista:List['int'] =(4, 2, 3)
    szorzat: int = 1
    for i in lista:
        #print(i)
        szorzat *= i
        print("Eredmény: {dsa}".format(dsa=szorzat))

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

def mersenne(o:int)-> int:
    z = 2
    for i in range(0, 10000):
        if o == z ^ i - 1:
            return True
        else:
            False

print(mersenne(int(input())))




