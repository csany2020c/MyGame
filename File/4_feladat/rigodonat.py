from typing import TextIO
from typing import  List
import string

class Data:

    def __init__(self, praseString: str) -> None:
        super(self).__init__()
        print(praseString)
        fields: List['str'] = parseString.split(" ")

        self.x: int = int(fields[0])