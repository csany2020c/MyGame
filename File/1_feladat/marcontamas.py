import string
from typing import TextIO
from typing import List

class Data:

    def __init__(self, parseString: str) -> None:
        super().__init__()
        print("Create Data from String")
        print(parseString)
        fields: List['str'] = parseString.split(" ")
        self.x: int = int(fields[0])
        self.y: int = int(fields[1])
        self.color: int = (int(fields[2]), int(fields[3]), int(fields[4]))
        self.text: str = ""
