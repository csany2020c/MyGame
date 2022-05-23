from dataclasses import field
from tkinter import N

from typing import TextIO
from typing import List

class Data:

    def __init__(self, parseString: str):
        super().__init__()

        lista: List['str'] = parseString.split("\n")

        self.evv: int = int (lista[0])
        self.het: int = int (lista[1])
        self.fordulo: int = int (lista[2])
        self.t13p1: int = int (lista[3])
        self.ny13p1: int = int (lista[4])
        self.eredmenyek: str = (lista[5])
        
        
    def __str__(self) -> str:
        return "{x};   {y};   {txt};   {col};  {tavi}, {zamn}".format(x=self.evv, y=self.het, txt=self.fordulo, col=self.t13p1, tavi=self.ny13p1, zamn=self.eredmenyek)


class Main:

    def __init__(self) -> None:
        super().__init__()
        print("2. feladat")
        f: TextIO = open("toto.txt", "r", encoding="utf-8")
        content: str = f.read()
        print(content)
        print("4.feladat")












        

        
        # kb 2 és fél óra
        
       
    
Main()

# class NAIN:
#     print("4.feladat")
#     content = open("toto.txt", "r", encoding="utf-8")
#     lines = content.splitlines()[4:]
#     part_data = {}
#     for line in lines:
#         columns = line.split()
#         if len(columns) != 3:
#             continue
#         part_data[columns[0]] = (columns[1], columns[2])
#
#
#
#
# NAIN()


