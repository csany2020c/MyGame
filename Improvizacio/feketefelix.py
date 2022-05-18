from typing import List

class huto:
    def __init__(self):
        self.szin: "szine"
        self.tipus: "fajtaja"
        self.szeleseg: int + 0
        self.magassag: int + 0
        self.marka: "markaneve"
        self.teljesitmeny: "Wolt szam"

adat = huto()
adat.marka = "Gorenje"
adat.szin = "Piros"
adat.szeleseg = 600
adat.magassag = 1940
#ezek mm-be megadott értékek
adat.tipus = "Standard"
adat.teljesitmeny = "70 W"
print(adat.marka)
print(adat.szin)
print(adat.szeleseg)
print(adat.magassag)
print(adat.teljesitmeny)

class map:
    def __init__(self):
        self.circles: "amount of circles in the map"
        self.sliders: "amount of sliders in the map"
        self.bpm: "the songs beats per minute"
        self.time: "the time of the map"


data = map
data.circles = 360
data.sliders = 602
data.bpm = 250
data.time = "4:24"
print(data.time)
print(data.bpm)
print(data.circles)
print(data.sliders)

class video:
    def __init__(self):
        self.megtekintes:"megtekintesek szama"
        self.ido:"video ideje"
        self.feltoltesidatum:"feltoltes datuma"
        self.likeszam:"likeok szama"
        self.hozzaszolasok:"hozzaszolasok szama"

info = video
info.ido = "1:30" #perc
info.megtekintes = 10
info.feltoltesdatuma = "2022.május.4"
info.likeszam = 0
info.hozzaszolasok = 0

print(info.ido)
print(info.megtekintes)
print(info.feltoltesdatuma)
print(info.likeszam)
print(info.hozzaszolasok)
















