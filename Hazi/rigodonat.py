from typing import List
import random

#elsofeladat
#def legnagyobb(legnagyobbszam: list) -> int:
#    b: int = legnagyobbszam[0]
#  for i in legnagyobbszam:
#       if b < i:
#            b = i
#   return b

#lista: List['int'] = list()
#a: int = 0
#for i in range(3):
#   a = int(input())
#   lista.append(a)

#print(legnagyobb(lista))

#masodikfeladat

#list8num :List['int'] = [ 2,5,6,7,32,23,1,3]
#osszeg = 0
#db: int = 0
#for i in list8num:
#    osszeg += i
 #   db = i
  #  atlag = osszeg / db

   # print("A számok átlagánál kisebb számok({a})".format(a=atlag))
    #for a in list8num:
     #   if a < atlag:
      #      print (a)

#harmadikfeladat



#negyedikfeladata


#dolgozat-probavizsga
#1.
class Doga:
    def __init__(self) -> None:
        super().__init__()

    def elso(self):
        szam1: int = int(input("Kérem az elso szamot:"))
        szam2: int = int(input("Kérem a második szamot:"))
        for i in range(szam2 + 1):
            szorzatok = szam1 * i
            if i != 0:
                print(szorzatok)

