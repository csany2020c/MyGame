from typing import List, TextIO
from os.path import exists


class Gyakorlatok:
    def __init__(self,gyakorlat:str,suly,ismetles,set) -> None:
        super().__init__()
        self.gyakorlat = gyakorlat
        self.suly = suly
        self.ismetles = ismetles
        self.set = set

    def __str__(self) -> str:
        return f"Gyakorlat neve: {self.gyakorlat} Súly: {self.suly}kg Ismétlésszám: {self.ismetles} Elvégzett szettek: {self.set}"

class Program:

    def __init__(self) -> None:
        super().__init__()
        print("Üdvözöllek, kérlek írd be a válaszaidat majd a feltett kérdésekre!")
        gyakorlatok:List['Gyakorlatok'] = list()

        print("Gyakorlat amit rögzíteni szeretnél:")
        exercise:str = input()
        weight:int = self.intbeolvas("Súly amivel elvégezted:")
        ismetles:int = self.intbeolvas("Ismétlés:")
        set:int = self.intbeolvas("Szettek:")
        obj:Gyakorlatok = Gyakorlatok(exercise,weight,ismetles,set)
        gyakorlatok.append(obj)
        save:bool = self.boolbeolvas("Mented?")
        if save:
            clean:bool = self.boolbeolvas("Szeretnéd formázni?")
            if clean:
                sure:bool = self.boolbeolvas("Biztos?")
                if sure:
                    FileHandle(True,gyakorlatok)
                else:
                    quit("RENDBEN!")
            else:
                FileHandle(False,gyakorlatok)


        if save == "N":
            print("Nincs siker")
        for i in gyakorlatok:
            print(i)

    def boolbeolvas(self,prompt: str) -> bool:
        while True:
            be: str = input(prompt + " (I/N): ")
            if be.upper() == "I" or be.upper() == "Y":
                return True
            if be.upper() == "N":
                return False

    def intbeolvas(self,prompt: str) -> int:
        while True:
            be: str = input(prompt)
            try:
                return int(be)
            except:
                pass

class FileHandle:

    def __init__(self, clean:bool,content:List['Gyakorlatok']) -> None:
        super().__init__()
        if clean:
            writeable: str = ""
            f:TextIO = open("FMFile.txt","w", encoding="UTF-8")
            f.write(writeable)
            f.close()
        else:
            if exists("FMFile.txt"):
                fr:TextIO = open("FMFile.txt", "r", encoding="UTF-8")
                contents:str = fr.read()
                writeable: str = contents
                fr.close()
            else:
                print("Nem létezik még a fájl")
                quit()
        for i in content:
            writeable+=str(str(i) + "\n")
        self.writeIt(writeable)
    def writeIt(self,szoveg:str):
        f: TextIO = open("FMFile.txt", "w", encoding="UTF-8")
        f.write(szoveg)






Program()
