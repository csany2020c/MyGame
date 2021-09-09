from game.scene2d.MyElapsedTime import *
from game.scene2d.MyBaseListeners import *

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from __type_checking__ import *


class MyStage(MyBaseListeners, MyElapsedTime):

    def __init__(self):
        MyBaseListeners.__init__(self)
        MyElapsedTime.__init__(self)
        self._visible: bool = True
        self._pause: bool = False
        self._screen: 'MyScreen' = None
        self._actors = []
        self.create()

    def act(self):
        MyElapsedTime.act(self, self.get_delta_time())
        for obj in self._actors:
            obj.act()

    def draw(self):
        for obj in self._actors:
            obj.draw()

    def add_actor(self, actor: 'MyActor'):
        # https://stackoverflow.com/questions/2461907/python-circular-imports-needed-for-type-checking
        # The best solution is to not check types.
        # XD
        # XD
        #if isinstance(actor, 'MyBaseActor'):
        self._actors.append(actor)
        if actor._stage != None:
            print("A következő actor át lett helyezve a " + str(id(actor._stage)) + " stageből a " + str(id(self)) + " stagebe.")
            actor.remove_from_stage()
        actor.set_stage(self)
        #else:
        #    print("ERROR: Az objektum példány nem adható hozzá a staghez, mert nem a MyBaseActor leszármazottja.")

    def remove_actor(self, actor: 'MyBaseActor'):
        self._actors.remove(actor)
        actor.set_stage(0)

    def on_mouse_down(self, pos, button):
        if self._on_mouse_down_listener != 0:
            self._on_mouse_down_listener(pos, button)
        for obj in self._actors:
            if isinstance(obj, MyActor):
                obj.on_mouse_down(pos, button)

    def on_mouse_up(self, pos, button):
        if self._on_mouse_up_listener != 0:
            self._on_mouse_up_listener(pos, button)
        for obj in self._actors:
            if isinstance(obj, MyActor):
                obj.on_mouse_up(pos, button)

    def on_mouse_move(self, pos):
        if self._on_mouse_move_listener != 0:
            self._on_mouse_move_listener(pos)
        for obj in self._actors:
            if isinstance(obj, MyActor):
                obj.on_mouse_move(pos)

    def on_key_down(self, key, mod, unicode):
        if self._on_key_down_listener != 0:
            self._on_key_down_listener(key, mod, unicode)
        for obj in self._actors:
            if isinstance(obj, MyActor):
                obj.on_key_down(key, mod, unicode)

    def on_key_up(self, key, mod):
        if self._on_key_up_listener != 0:
            self._on_key_up_listener(key, mod)
        for obj in self._actors:
            if isinstance(obj, MyActor):
                obj.on_key_up(key, mod)

    def set_screen(self, screen):
        self._screen = screen
        if screen == None:
            self.hide()
        else:
            self.show()

    def get_delta_time(self) -> float:
        if self.screen is not None and self.screen.game is not None:
            return self._screen.game.get_delta_time()
        else:
            return 0

    def get_screen(self):
        return self._screen

    screen: 'MyScreen' = property(get_screen, set_screen)