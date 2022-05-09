from typing import TextIO, List


class Hazi:
    def __init__(self, ) -> None:
        super().__init__()
        f:TextIO = open("toto.txt", "r")
        file:str = f.read()
        self.lines:List['str'] = file.split('\n')
        for i in range(len(self.lines-1)):
            self.loto(self.lines[i])



    def loto(self, str):
        sor = lines.split(' ')
        self.ev = str(sor[0])
        self.het = str(sor[1])
        self.fordulo = str(sor[2])
        self.T13p1 = str(sor[3])
        self.Ny13p1 = int(sor[4])
        self.eredmenyek = int(sor[5])




Hazi()