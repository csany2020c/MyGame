import abc

#Minden időzítőt a staehez vagy actorhoz lehet hozzáadni. A lényeg, hogy oda lehet beilleszteni, ahol megjelent az .add_timer(...) metódus.
# pl.: text2.add_timer(MyTickTimer(self.tikk))
#  ahol a text2 egy Button típus.
#
#   Vagy referenciát csinálva:
#   self.timer: MyIntervalTimer = MyIntervalTimer(csinaldeztfuggveny, 3, 7)
#   stage.add_timer(self.timer)
#   ...
#   Máshol meghívható, akár egy kattintáskor:
#   self.timer.stop()
#
#   Minden időzítő megállítható, elindítható a start() és a stop() metódusokkal.
#   Az időzítő eltávolítható a remove() függvénnyel.
#
#   Az időzítő eseményéhez illesztett függvénynek egy paraméterének kell lenni, ami az időzítőt adja eredményül. Innen lehet lekérdezni például, hogy hányszor futott le, vagy mióta megy éppen.
#   pl:
#   text2.add_timer(MyTickTimer(self.tikk))

#     def tikk(self, timer: MyMultiTickTimer):
#         print("TIKK " + str(timer.count))
# TIKK 1
# TIKK 2
# TIKK 3
#
# Ez az osztály minden időzítő őse. Ezeket a funkciókat, amik benne vannak, minden időzítő tudja.


class MyBaseTimer(metaclass=abc.ABCMeta):

    _listener = 0
    _enabled: bool = True
    correction: float = 0
    # base_actor: game.MyActor.MyBaseActor = 0
    base_actor = 0
    elapsed_time:float = 0

    def __init__(self, func = 0):
        self._listener = func

    def set_timer_listener(self, func):
        self._listener = func

    def remove_timer_listener(self, func):
        self._listener = 0

    def start(self):
        self._enabled = True

    def stop(self):
        self._enabled = False

    def update(self, deltaTime: float = 0.0166666666666666666666):
        if self._enabled:
            self.elapsed_time += deltaTime
            self._do_timer()

    def _do_timer(self):
        pass

    def remove(self):
        if self.base_actor == 0:
            return
        self.base_actor.remove_timer(self)
        self.base_actor = 0


#Folyamatosan fut, ki és be lehet kapcsolni.
class MyPermanentTimer(MyBaseTimer):

    def _do_timer(self):
        if self._listener != 0:
            self._listener(self)


# Folyamatosan fut, de csak meghatározott időközönként futtatja le a kódot.
class MyTickTimer(MyBaseTimer):

    # interval: ennyi időközönként
    # start_delay: A hozzáadás után ennyivel később fut le először
    # repeat: ismétli, többször fut
    def __init__(self, func=0, interval: float = 1, start_delay: float = 0, repeat: bool = True):
        super().__init__(func)
        self.interval: float = interval
        self.elapsed_time = -start_delay
        self.repeat: bool = repeat

    def _do_timer(self):
        if not self._enabled:
            return
        if self.elapsed_time >= self.interval:
            self.correction = self.elapsed_time-self.interval
            if self._listener != 0:
                self._listener(self)
            if not self.repeat:
                self.stop()
            else:
                self.elapsed_time = self.correction


# folyamatosan, minden száításkor lefut egy intervallumon belül.
class MyIntervalTimer(MyBaseTimer):

    #start_time: futás kezdete
    #stop_time: futás vége
    def __init__(self, func=0, start_time: float = 1, stop_time: float = 4):
        super().__init__(func)
        self.start_time = start_time
        self.stop_time = stop_time

    def _do_timer(self):
        if not self._enabled:
            return
        if (self.elapsed_time >= self.start_time) and (self.elapsed_time <= self.stop_time):
            if self._listener != 0:
                self._listener(self)


# Egyszer fut le a hozzáadást követően. Ezután eltávolítja megát a birtokló objektum példányból.
class MyOneTickTimer(MyBaseTimer):

    def __init__(self, func=0, interval: float = 1):
        self.interval = interval
        super().__init__(func)

    def _do_timer(self):
        if not self._enabled:
            return
        if self.elapsed_time >= self.interval:
            self.correction = self.elapsed_time - self.interval
            if self._listener != 0:
                self._listener(self)
            self.remove()


# Meg lehet adni, hogy hányszor fusson le, és ez milyen időközönként legyen. Ezután eltávolítja megát a birtokló objektum példányból.
class MyMultiTickTimer(MyBaseTimer):

    def __init__(self, func=0, interval: float = 1, startdelay: float = 0, count = 5):
        super().__init__(func)
        self.interval: float = interval
        self.elapsed_time = -startdelay
        self.count: int = 0
        self.target_count: int = count

    def _do_timer(self):
        if not self._enabled:
            return
        if self.elapsed_time >= self.interval:
            self.correction = self.elapsed_time-self.interval
            self.count += 1
            if self._listener != 0:
                self._listener(self)
            if self.count >= self.target_count:
                self.remove()
            self.elapsed_time = self.correction

