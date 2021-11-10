import string
from typing import TextIO
from typing import List

class Data:

    def __init__(self, parseString: str) -> None:
        super().__init__()
        print("Create Data")
        print(parseString)

        fields: List['str'] = parseString.split(" ")

        self.x: