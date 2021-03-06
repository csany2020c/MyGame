import game
from Impostorsus.Game.WarioActor import *
from Impostorsus.Game.WarioMinden import *

class WarioScr(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.r = 92
        self.g = 148
        self.b = 252
        self.add_stage(ASD())

class WarioScr2(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.r = 92
        self.g = 148
        self.b = 252
        self.add_stage(ASD3())

class WarioKartScr(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.r = 92
        self.g = 148
        self.b = 252
        self.add_stage(WarioKartStage())


class MenuScreen(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.r = 200
        self.g = 100
        self.b = 0
        self.add_stage(ASD2())

class BindingsScreen(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.r = 92
        self.g = 148
        self.b = 252
        self.add_stage(BindingsStage())

class CreditScreen(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.r = 92
        self.g = 148
        self.b = 252
        self.add_stage(CreditStage())

class HalalScreen(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.r = 92
        self.g = 148
        self.b = 252
        self.add_stage(HalalStage())

    def act(self, delta_time: float):
        super().act(delta_time)
        if self.elapsed_time > 2.5:
            self.game.screen = WarioScr()

class WinScreen(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.r = 92
        self.g = 148
        self.b = 252
        self.add_stage(WinStage())

    def act(self, delta_time: float):
        super().act(delta_time)
        if self.elapsed_time > 5:
            self.game.screen = MenuScreen()

class KartWinScr(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.r = 92
        self.g = 148
        self.b = 252
        self.add_stage(KartWinStage())

    def act(self, delta_time: float):
        super().act(delta_time)
        if self.elapsed_time > 5:
            self.game.screen = MenuScreen()

class HalalScreen2(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.r = 92
        self.g = 148
        self.b = 252
        self.add_stage(HalalStage2())

    def act(self, delta_time: float):
        super().act(delta_time)
        if self.elapsed_time > 2.5:
            self.game.screen = WarioScr2()

class KartHalalScr(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.r = 92
        self.g = 148
        self.b = 252
        self.add_stage(KartHalalStage())

    def act(self, delta_time: float):
        super().act(delta_time)
        if self.elapsed_time > 2.5:
            self.game.screen = WarioKartScr()


class PalyaScr(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.r = 92
        self.g = 148
        self.b = 252
        self.add_stage(PalyaStage())

