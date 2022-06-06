from typing import List
def feladat1():
    print("1.Feladat")
    print("Vigyen be 3db számot:")
    szam1 = int(input())
    szam2 = int(input())
    szam3 = int(input())

    print("A bevitt számok közül a legnagyobb: {a}".format(a=max(szam1, szam2, szam3)))

feladat1()

def feladat2():
    print("----------")
    print("2.Feladat")
    lista: list = [1,2,3,4,5,6,7,8]
    osszeadva: int = 0
    db: int = 0
    for i in lista:
        osszeadva += i
        db = i
    atlag = osszeadva / db

    print("Átlagnál kisebb számok({a}):".format(a=atlag))
    for a in lista:
        if a < atlag:
            print(a)

feladat2()

#def feladat3():
#    print("----------")
#    print("3.Feladat")
#    lista = list()
#    for i in range(1, 90):
#        lista.append(i)
#
#    print(lista)
#
#feladat3()
def feladat4():
    while True:
        szam: int = int(input())
        if szam % 21:
            pass
        else:
            break

feladat4()


