from typing import List
from typing import TextIO
import string

class Data:
    def __init__(self, parseString: str) -> None:
        super().__init__()
        print("Create Data from String")
        print(parseString)

        fields: List['str'] = parseString.split(" ")

        self.x: int = int(fields[0])
        self.x: int = int(fields[1])
        self.color: int = int(fields[2], int(fields[3], fields[4]))
        self.text: str = ""

        for i in range(5, len(fields)):
            self.text += str(fields[i])
            if i < len(fields) - 1:
                self.text += " "


#class Olvas:
#    def __init__(self) -> None:
 #       super().__init__()
  #      f: TextIO = open("readme.txt", "r")
#
 #       content: str = f.read()

  #      print("Content:")
   #     print(content)

        #lines: List'Data' = list()


#Olvas()