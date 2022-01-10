from typing import List

# def faktoralis(asd: int) -> int:
#     szorzat = 1
#     for i in range(2, asd + 1):
#         szorzat *= i
#     return szorzat


#print(faktoralis(6))

#2. feladat
#print(8 % 3)

def fuggveny(n: int) -> List['str']:
     lista: List['int'] = list()
     #bemenet: int = int(input())
     for i in range(1, n + 1):
         if n % i == 0:
             lista.append(i)
     return lista

     for i in fuggveny(26):
         print(i)

#print(fuggveny(26))

#3.feladat
def fuggveny1(n: int) -> bool:
    return len(fuggveny(n)) == 2

# for i in range(0, 126):
#     print("{szam} {primszam}".format(szam=i, primszam=fuggveny1(i)))


