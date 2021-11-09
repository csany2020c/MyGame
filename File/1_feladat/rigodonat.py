import string
from typing import TextIO
from typing import List

class Data:

    def __init__(self, parseString: str) -> None:
        super().__init__()
        #print("Create Data from String")
        #print(parseString)
        fields: List['str'] = parseString.split(";")
        print(fields)
        # self.text: str = ""
        # for i in range(0, len(fields)):
        #     self.text += str(fields[i])
        #     if i < len(fields) - 1:
        #         self.text += " "


class Main:

    def __init__(self) -> None:
        super().__init__()
        f: TextIO = open("!_Spec/orvosi_nobeldijak.txt", "r")
        content: str = f.read()
        #print("Content:")
        #print(content)
        lines: List['str'] = content.split(sep="\n")
        #print("Split content")
        #print(lines)
        #print("Load to List")
        datalist: List['Data'] = list()
        i: int = 0
        for str in lines:
            if i > 0:
                d = Data(str)
                datalist.append(d)
            i+=1
        #print("Print list")
        #for d in datalist:
        #    print(d)
        f.close()


Main()
