"""valtozo = int(input())
eredmeny = 1
szorzas = 1
for i in range(valtozo):
    eredmeny = eredmeny * szorzas
    szorzas = szorzas + 1
print(eredmeny)"""

"""szam = int(input())
oszto = 1
while(oszto <= szam):
    if szam % oszto == 0:
        print(oszto)
    oszto = oszto + 1"""


def prime(input):
    osztas = 1
    osztva = 0
    while osztas <= input:
        if input % osztas == 0:
            osztva = osztva + 1
        osztas = osztas + 1
    if osztva == 2:
        print("A(z) " + str(input) + " egy prímszám")
    else:
        print("A(z) " + str(input) + " nem prímszám")

oszthatoe(int(input()))