from typing import List

class huto:
    def __init__(self):
        self.szin:  "Piros"
        self.tipus: "fajtaja"
        self.szeleseg: int + 0
        self.magassag: int + 0
        self.marka: "markaneve"
        self.teljesitmeny: "Wolt szam"

    def __str__(self) -> str:
        return "Szín = {a} Típus = {b} Szélesség = {c} Magasság = {d} Márka = {f} Teljesítmény = {g}".format(a= self.szin, b=self.tipus, c=self.szeleseg, d=self.magassag, f=self.marka, g=self.teljesitmeny)



adat = huto()
adat.marka = "Gorenje"
adat.szin = "Piros"
adat.szeleseg = 600
adat.magassag = 1940
#ezek mm-be megadott értékek
adat.tipus = "Standard"
adat.teljesitmeny = "70 W"
print(adat)

dsa = (input("Hütő színe:"))




class map:
    def __init__(self):
        self.circles: "amount of circles in the map"
        self.sliders: "amount of sliders in the map"
        self.bpm: "the songs beats per minute"
        self.time: "the time of the map"

    def __str__(self) -> str:
        return "Circles = {y} Sliders = {x} BPM = {c} Beatmap time = {v}".format(y=self.circles, x= self.sliders, c=self.bpm, v=self.time)

data = map()
data.circles = 360
data.sliders = 602
data.bpm = 250
data.time = "4:24"
print(data)

class video:
    def __init__(self):
        self.megtekintes:"megtekintesek szama"
        self.ido:"video ideje"
        self.feltoltesdatum:"feltoltes datuma"
        self.likeszam:"likeok szama"
        self.hozzaszolasok:"hozzaszolasok szama"

    def __str__(self) -> str:
        return "Megtekintések = {q} Videó időtartama = {w} Feltöltés dátuma = {e} Likeok száma = {r} Hozzászólások = {t}".format(q=self.megtekintes, w=self.ido, e=self.feltoltesdatum, r=self.likeszam, t=self.hozzaszolasok)


info = video()
info.ido = "1:30" #perc
info.megtekintes = 10
info.feltoltesdatum = "2022.május.4"
info.likeszam = 0
info.hozzaszolasok = 0

print(info)
















