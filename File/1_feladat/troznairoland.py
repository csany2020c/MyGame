import string
from typing import TextIO
from typing import List

class Adat:

    def __init__(self, parseString: str) -> None:
        super().__init__().
        print("Create data from string")
        print(parseString)

        fields: List['str'] = parseString.split('')

        self.Év: int = int(fields[0])
        self.Név: int = int(fields[1])
        self.Születés-Halálozás: int = int(fields[2])
        self.Országkód: int = int(fields[3])
        self.text: str = ""

        for i in range(5, len(fields)):
            self.text += str(fields[1])
            if i < len(fields) - 1:
                self.text += " "

        def __str__(self) -> str:

            return "Év = {ev}; Név = {nev}; Születés-Halálozás = {szulhal}; color = {orsz}".format(ev=self.Év, nev=self.Név, szulhal=self.Születés-Halálozás, orsz=self.Országkód)