from dataclasses import field
from tkinter import N

from typing import TextIO
from typing import List

class Data:

    def __init__(self, parseString: str) -> None:
        super().__init__()
        fields: List['str'] = parseString.split(";")
        self.év: str = str(fields[0])
        self.hét: str = fields[1]
        self.fordulo: str = fields[2]
        self.t13p1: str = fields[3]
        self.ny13p1: int = fields[4]
        self.eredmények: int = fields[5]
        
        
    def __str__(self) -> str:
        return "{x};   {y};   {txt};   {col};  {tavi}, {zamn}".format(x=self.év, y=self.hét, txt=self.fordulo, col=self.t13p1, tavi=self.ny13p1, zamn=self.eredmények)

class Main:

    def __init__(self) -> None:
        super().__init__()
        print("2. feladat")
        f: TextIO = open("toto.txt", "r", encoding="utf-8")
        content: str = f.read()
        print(content)
        print("3.feladat")


        fil = open("toto.txt","r")
        Counter = 0
        Content = fil.read()
        Colist = Content.split("\n")

        for i in Colist:
            if i:
                Counter += 1

        print("Eredmények Száma:")
        print(Counter)

        

        
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


