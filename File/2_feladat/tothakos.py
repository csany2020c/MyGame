import string
from typing import TextIO
from typing import List

class Main:
    def __init__(self):
        super().__init__()
        f: TextIO = open("dalok.txt")
        content: str = f.read()
        print("Content:")
        print(content)
        lines:List['str'] = content.split()


Main()