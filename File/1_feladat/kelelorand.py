from typing import TextIO
from typing import List


class Data:


    def __init__(self, parseString: str) -> None:
        super().__init__()
        print("Create Data from String")
        print(parseString)

        fields: List['str'] = parseString.split(" ")

        self.datum: int = int(fields[0])
        self.nev1: int = int(fields[1]), int(fields[2]), int(fields[3])
        self.datum2: int = int(fields[4])
        self.text: str = ""

        for i in range(5, len(fields)):
            self.text += str(fields[i])
            if i < len(fields) - 1:
                self.text += " "
    def __str__(self) -> str:
        return "datum = {datum}; nev1 = {nev1}; datum2 = {datum2}; text = {text}".format(datum=self.datum, nev1=self.nev1, datum2=self.datum2, text = self.text)
class Main:

    def __init__(self) -> None:
        super().__init__()
        f: TextIO = open("!_Spec/orvosi_nobeldijak.txt", "r")
        content: str = f.read()
        f.close()
        print("Content:")
        print(content)
        lines: List['str'] = content.split(sep="\n")
        print("Split content")
        print(lines)
        print("Load to List")
        datalist: List['Data'] = list()
        for s in lines:
            d = Data(s)
            datalist.append(d)
        print("Print list")
        for d in datalist:
            print(d)


Main()