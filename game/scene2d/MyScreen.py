from game.scene2d.MyTimers import *
from game.scene2d.MyElapsedTime import *

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from __type_checking__ import *


class MyScreen(MyTimers, MyElapsedTime):

    def __init__(self):
        MyElapsedTime.__init__(self)
        MyTimers.__init__(self)
        self.r: float = 0
        self.g: float = 0
        self.b: float = 0
        self._game: 'MyGame' = None
        self._stages = list()
        self._timers = list()
        self.create()

    def dispose(self):
        MyElapsedTime.dispose(self)
        MyTimers.dispose(self)
        for s in self._stages:
            s.dispose()

    def get_game(self):
        return self._game

    def set_game(self, game):
        if game == None:
            self.hide()
        else:
            self.show()
        self._game = game

    def set_BackGroundColor(self, r: int, g: int, b: int):
        self.r = r
        self.g = g
        self.b = b

    def act(self, delta_time: float):
        MyElapsedTime.act(self, delta_time)
        MyTimers.act(self, delta_time)
        for s in self._stages:
            if s._visible and not s._pause:
                s.act(delta_time)

    def draw(self):
        self._game.pgScreen.fill((self.r, self.g, self.b))
        for s in self._stages:
            # g = game.MyStage.MyStage(s)
            if s._visible and not s._pause:
                s.draw()

    def addStage(self, stage, zIndex: int = 0):
        self._stages.append(stage)
        stage.set_screen(self)
        pass

    def get_screen_width(self) -> int:
        return self.stage.game.screen_width

    def get_screen_height(self) -> int:
        return self.stage.game.screen_height

    game = property(get_game, set_game)
    screen_width: int = property(get_screen_width)
    screen_height: int = property(get_screen_height)

# @ Override
# public
# void
# change(boolean
# visible, MyStage
# sender) {
#     updateInputMultiplexer();
# }
# });
#
# stage.addPauseChangeListener(new
# MyStage.PauseChangeListener()
# {
# @ Override
# public
# void
# change(boolean
# pause, MyStage
# sender) {
#     updateInputMultiplexer();
# }
# });
#
#
# stage.addProcessInputChangeListener(new
# MyStage.ProcessInputChangeListener()
# {
# @ Override
# public
# void
# change(boolean
# pause, MyStage
# sender) {
#     updateInputMultiplexer();
# }
# });
#
# }
# }
#
# public
# void
# removeStage(MyStage
# stage){
#     stages.removeValue(stage, true);
# inputMultiplexer.removeProcessor(stage);
# }
#
#
# public
# void
# sortStagesByZindex()
# {
#
#     stages.sort(new
# Comparator < MyStage > ()
# {
# @ Override
# public
# int
# compare(MyStage
# actor, MyStage
# t1) {
# return actor.zIndex - t1.zIndex;
# }
# });
# updateInputMultiplexer();
# }
#
#
#
#
