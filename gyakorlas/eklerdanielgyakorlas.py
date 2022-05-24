from dataclasses import fields
from operator import contains
from tkinter import N
from typing import TextIO
from re import I, X
from typing import List
class Adat:
    def __init__(self, Parsestring: str) -> None:
        super().__init__()
        fields: List['str'] = Parsestring.split("")
        self.ev: int = int(fields[0])
        self.het: int = int(fields[1])
        self.ford: int = int(fields[2])
        self.t: int = int(fields[3])
        self.n: int = int(fields[4])
        self.ered: str = str(fields[5])

    
    def __str__(self):
        return " ev ={e}, het= {h}, ford= {f}, t= {t}, n= {n}, ered= {e}".format(e =self.ev, h=self.het, f=self.ford, t=self.t, n=self.n, ered=self.ered)

class ZAMN:
    

    def __init__(self):
        super().__init__()

        f = open("gyakorlas/toto.txt", "r")
        cucc = f.read()
        print(cucc)
        
        f.close()

        print("3. feladat")
        harmas = len(cucc.split("\n")) - 1

        print("Eredmények száma:")
        print(harmas)
        print("4.feladat")
        
        b = 0
        for i in cucc:
            if  i == "X":
                b += 1
        print(b)
        
                
ZAMN()