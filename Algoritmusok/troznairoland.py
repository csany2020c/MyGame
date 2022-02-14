from typing import List

#1,feladat:
#szam = 1
#for i in range(42):
    #print(szam)
    #szam = szam + 1

#2,feladat:
#3,feladat:
#osszeg = 0
#while(True):
    #szam = input()
    #osszeg = osszeg + int(szam)
    #if szam == str(0):
        #print("Az összeg: {osszeg}".format(osszeg=osszeg))
        #break

#4,feladat:
#list: List['int'] = (4, 6, 5, 3, 2, 9, 1)
#osszeg: int = 0
#for i in range(0, len(list)):
    #print(i)
    #osszeg += list[i]
#print('Az összeg: {osszeg}'.format(osszeg=osszeg))

#5,feladat:
#def osszeg(list: List['int']) -> int:
    #osszeg = 0
    #for i in range(0, len(list)):
        #osszeg = osszeg + list[i]
    #return osszeg

#list: List['int'] = (1, 2, 3, 4, 5, 6)
#igen = osszeg(list=list)
#print(igen)

#6,feladat:
#szam = int(input())
#eredmeny = 1
#szor = 1

#for i in range(szam):
    #eredmeny = eredmeny * szor
    #szor = szor + 1
#print("Az eredmény: {eredmeny}".format(eredmeny=eredmeny))

#7,feladat:
#szam = int(input())
#osztas = 1
#while (osztas <= szam):
    #if szam % osztas == 0:
        #print(osztas)
    #osztas = osztas + 1

#8,feladat:
#def primszam(input):
    #osztas = 1
    #eredmeny = 0
    #while osztas <= input:
        #if input % osztas == 0:
            #eredmeny = eredmeny + 1
        #osztas = osztas + 1
    #if eredmeny == 2:
        #print("A(z) " + str(input) + " primszám!")
    #else:
        #print("A(z) " + str(input) + " nem primszám!")

#primszam(int(input()))

#9,feladat:
#def binary(be: int) -> str:
    #bemenet = abs(be)
    #kimenet: str = ""
    #while 0 < bemenet:
        #if bemenet % 2 == 0:
            #kimenet = "0" + kimenet
        #else:
            #kimenet = "1" + kimenet
        #bemenet = bemenet // 2
    #if kimenet == "":
        #return "0"
    # return string[::-1]
    #if be < 0:
        #return "-" + kimenet
    #return kimenet


#originalbemenet: int = int(input())
#print("A " + str(originalbemenet) + " binárisan: " + binary(originalbemenet))

#10,feladat:
def paros_lista(input: List['int']) -> List['int']:
    lisst: List['int'] = list()
    for i in lisst2:
        if i % 2 == 0:
            lisst.append(i)
    return lisst

lisst2 = [1, 4, 6, 8, 3, 5, 9, 2, 0, 10, 12, 34, 132, 353, 1, 31, 123, 89, 90]
lisst3 = paros_lista(lisst2)
#print(lisst3)

#11,feladat:
def egyesevel_lista(be: int) -> List['int']:
    ki: List['int'] = list()
    for i in range(abs(be) + 1):
        if be > 0:
            ki.append(i)
        else:
            ki.append(-i)
    #print(ki)

egyesevel_lista(be = -100)

#12,feladat:
def parosan_lista(be: int) -> List['int']:
    return paros_lista(egyesevel_lista(be))

print(parosan_lista(5))
