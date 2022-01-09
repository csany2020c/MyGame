from typing import TextIO
from typing import List


class Data:
    def __init__(self, parsestring: str) -> None:
        super().__init__()
        fields: List['str'] = parsestring.split(";")
        self.versenyzo: str = fields[0]
        self.rajtsz: str = fields[1]
        self.kateg: str = fields[2]
        self.versido: str = fields[3]
        self.tavsz: str = fields[4]


    def __str__(self) -> str:
        return "versenyzo = {v}; rajtsz = {r}; kateg = {k}; versido = {vi}; tavsz = {t}".format(v=self.versenyzo, r=self.rajtsz, k=self.kateg, vi=self.versido, t=self.tavsz)