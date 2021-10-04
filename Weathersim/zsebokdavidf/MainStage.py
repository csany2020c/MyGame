import game
from Weathersim.zsebokdavidf.MainActor import MainActor


class MainStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        Ma = MainActor()
        self.add_actor(actor=Ma)