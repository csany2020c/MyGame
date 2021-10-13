from Weathersim.ZsuppanFlorian.mainstage import *
from Weathersim.ZsuppanFlorian import *

#class MainScreen(game.scene2d.MyScreen):

 #   def __init__(self):
  #      super().__init__()
   #     self.add_stage(MainStage())
    #    self.add_stage(snowStage())
     #   self.add_stage(rainStage())

class Esikaeso(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(EsoStage())


class Napsutes(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(NapStage())


class Esikaho(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(HoStage())


class Esikmindketo(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(Havaseso())
