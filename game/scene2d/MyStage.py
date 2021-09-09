from game.scene2d.MyLifeCycles import *
from game.scene2d.MyBaseListeners import *

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from __type_checking__ import *


class MyStage(MyBaseListeners, MyLifeCycles):

    def __init__(self):
        self.visible: bool = True
        self.pause: bool = False
        self.actors = list()
        self.screen: 'MyScreen' = None
        MyBaseListeners.__init__(self)
        self.actors = []
        self.create()
        self.elapsed_time = 0

    def act(self):
        self.elapsed_time += self.get_delta_time()
        for obj in self.actors:
            obj.act()

    def draw(self):
        for obj in self.actors:
            obj.draw()

    def add_actor(self, actor: 'MyActor'):
        # https://stackoverflow.com/questions/2461907/python-circular-imports-needed-for-type-checking
        # The best solution is to not check types.
        # XD
        # XD
        #if isinstance(actor, 'MyBaseActor'):
        self.actors.append(actor)
        if actor._stage != 0:
            print("A következő actor át lett helyezve a " + str(id(actor._stage)) + " stageből a " + str(id(self)) + " stagebe.")
            actor.remove_from_stage()
        actor.set_stage(self)
        #else:
        #    print("ERROR: Az objektum példány nem adható hozzá a staghez, mert nem a MyBaseActor leszármazottja.")

    def remove_actor(self, actor: 'MyBaseActor'):
        self.actors.remove(actor)
        actor.set_stage(0)

    def on_mouse_down(self, pos, button):
        if self._on_mouse_down_listener != 0:
            self._on_mouse_down_listener(pos, button)
        for obj in self.actors:
            if isinstance(obj, MyActor):
                obj.on_mouse_down(pos, button)

    def on_mouse_up(self, pos, button):
        if self._on_mouse_up_listener != 0:
            self._on_mouse_up_listener(pos, button)
        for obj in self.actors:
            if isinstance(obj, MyActor):
                obj.on_mouse_up(pos, button)

    def on_mouse_move(self, pos):
        if self._on_mouse_move_listener != 0:
            self._on_mouse_move_listener(pos)
        for obj in self.actors:
            if isinstance(obj, MyActor):
                obj.on_mouse_move(pos)

    def on_key_down(self, key, mod, unicode):
        if self._on_key_down_listener != 0:
            self._on_key_down_listener(key, mod, unicode)
        for obj in self.actors:
            if isinstance(obj, MyActor):
                obj.on_key_down(key, mod, unicode)

    def on_key_up(self, key, mod):
        if self._on_key_up_listener != 0:
            self._on_key_up_listener(key, mod)
        for obj in self.actors:
            if isinstance(obj, MyActor):
                obj.on_key_up(key, mod)

    def set_screen(self, screen):
        self.screen = screen
        if screen == None:
            self.hide()
        else:
            self.show()

    def get_delta_time(self) -> float:
        return self.screen.game.get_delta_time()

