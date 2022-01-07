from typing import List

#for i in range(1,43):
    #print(i)




def beolvasas():
    szam1 = int(input())
    gf: int = 0
    gf =szam1
    while(szam1 !=0):
        szam1 = int(input())
        gf = gf + szam1
    print(gf)


def lista():
    lista: List['int'] = (6, 5, 9, 3, 1, 2, 3)
    osszeg: int = 0
    for i in lista:
        print(i)
        osszeg += i
        print("Az összeg: {sum}".format(sum=osszeg))


def osszegzes(lista: list['int']) -> int:
    lista: List['int'] = (6, 4, 2, 3)
    for i in range(0, len(list)):


osszegzes()




