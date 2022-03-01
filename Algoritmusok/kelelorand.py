from typing import List


def helyiertek2(be:int) -> List['int']:
    ki: List['int'] = list()
    for c in str(abs(be)):
        ki.append(int(c))
    return ki


def negyzetosszeg(be: List['int']) -> int:
    szam: int = 0
    for i in be:
        szam+=i*i
    return szam

def boldoge(szam: int) -> bool:

    f1 = open('kelelorandfile', 'r+')
    f1open = f1.read().strip().split(';')

    f2 = open('kelelorandfile2', 'r+')
    f2open = f2.read().strip().split(';')
    print(f2open)

    aktualisnegyzetosszeg: int = szam
    szekvencia: List['int'] = list()
    if str(szam) in f1open:
        return False
    if str(szam) in f2open:
        return True

    if str(szam) not in f1open and str(szam) not in f2open:
        while aktualisnegyzetosszeg != 1 and aktualisnegyzetosszeg not in szekvencia:
            szekvencia.append(aktualisnegyzetosszeg)
            aktualisnegyzetosszeg = negyzetosszeg(helyiertek2(aktualisnegyzetosszeg))

    if aktualisnegyzetosszeg == 1:
        f2.write(str(szam) + ";")

    else:
        f1.write(str(szam) + ";")









print(boldoge(7))



