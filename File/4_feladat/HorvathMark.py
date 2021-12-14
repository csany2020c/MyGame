from typing import List
from typing import TextIO

class Data:
    def __init__(self, parseString: str) -> None:
        super().__init__()
        fields: List['str'] = parseString.split(" ")
        self.helyezes: int = int(fields[0])
        self.versenyzok: int = int(fields[1])
        self.sportag: str = fields[2]
        self.versenyszam: str = fields[3]

    def __str__(self) -> float:

