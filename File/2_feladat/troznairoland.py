import string
from typing import TextIO
from typing import List

class Data:

    def __init__(self, parseString: str) -> None:
        super().__init__()
        print("Create Data")
        print(parseString)

        fields: List['str'] = parseString.split(" ")

        self.eloado: str = (fields[0])
        self.nev: str = (fields[1])
        self.zenekar: str = (fields[2])
        self.dalid: str = (fields[3])
        self.eloadoid: str = (fields[4])
        self.cim: str = (fields[5])
        self.megjelenes: str = (fields[6])
        self.ev: str (fields[7])
        self.helyezes: str (fields[8])
        self.hdalid: str = (fields[9])
        self.text: str = ""

    def __str__(self) -> str:
        return "{eloado};   {nev};   {zenekar};   {dalid};   {eloadoid};   {cim};   {megjelenes};   {ev};   {helyezes};   {hdalid};   {text}".format(eloado=self.eloado, nev=self.nev, zenekar=self.zenekar, dalid=self.dalid, eloadoid=self.eloadoid, cim=self.cim, megjelenes=self.megjelenes, ev=self.ev, helyezes=self.helyezes, hdalid=self.hdalid)

class Main:

    def __init__(self) -> None:
        super().__init__()
        f: