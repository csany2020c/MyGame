from typing import List, TextIO


class Data:
    def __init__(self, parseString:str) -> None:
        super().__init__()
        fields:List['str'] = parseString.split(" ")
        self.helyezes:int = int(fields[0])
        self.csapattagok:int = int(fields[1])
        self.sportag:str = str(fields[2])
        self.versenyszam:str = str(fields[3])

    def __str__(self) -> str:
        return "Helyezés:{helyezes} csapattagok:{csapattagok} sportag:{sportag} versenyszam:{versenyszam}".format(helyezes=self.helyezes,csapattagok=self.csapattagok,sportag=self.sportag,versenyszam=self.versenyszam)


class Main:
    def __init__(self) -> None:
        super().__init__()
        f:TextIO = open("!_Specs/helsinki.txt",encoding="utf8")
        content:str = f.read()
        lines:List['str'] = content.split(sep="\n")
        dataList:List['Data'] = list()
        for i in range(0,len(lines)):
                dataList.append(Data(lines[i]))
        f.close()
        print("3.Feladat: Pontszerző helyezések száma : " + str(len(lines)))

        arany:int = 0
        ezust:int = 0
        bronz:int = 0
        for index in range(0,len(dataList)):
            if dataList[index].helyezes == 1:
                arany += 1
            elif dataList[index].helyezes == 2:
                ezust += 1
            elif dataList[index].helyezes == 3:
                bronz += 1
        ossz = int(arany + ezust + bronz)
        print("4.Feladat: \n Aranyérmek : {arany} \n Ezüstérmek : {ezust} \n Bronzérmek : {bronz} \n összesen: {ossz}".format(arany = arany,ezust = ezust, bronz = bronz,ossz=ossz))

        points:int = 0
        for index in range(0,len(dataList)):
            if dataList[index].helyezes == 1:
                points += 7
            elif dataList[index].helyezes == 2:
                points += 5
            elif dataList[index].helyezes == 3:
                points += 4
            elif dataList[index].helyezes == 4:
                points += 3
            elif dataList[index].helyezes == 5:
                points += 2
            elif dataList[index].helyezes == 6:
                points += 1
        print(f"5.feladat: \n Olimpikai pontok: {points}".format(points = points))

        swimming:int = 0
        torna:int = 0
        for index in range(0,len(dataList)):
            if dataList[index].sportag == "uszas" and dataList[index].helyezes <= 3:
                swimming += 1
            elif dataList[index].sportag == "torna" and dataList[index].helyezes <= 3:
                torna += 1
        if swimming > torna:
            print("6.Feladat : \n Úszás sportágban szereztek több érmet")
        elif swimming < torna:
            print("6.Feladat : \n Torna sportágban szereztek több érmet")
        else:
            print("6.Feladat : \n Egyenlő volt az érmek száma")

Main()

