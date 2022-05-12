from dataclasses import field
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
        f: TextIO = open("gyakorlas//toto.txt", "r", encoding="utf-8")
        content: str = f.read()
        print(content)
        print("3.feladat")
        with open(r"gyakorlas//toto.txt", 'r') as fp:
            for count, line in enumerate(fp):
                pass
        print('Eredmények száma', count + 1)
        # sacc per kábé 1 és fél óra
        
       
    
Main()