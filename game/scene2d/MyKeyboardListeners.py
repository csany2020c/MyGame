import pygame

from game.scene2d.MyLifeCycles import *

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from __type_checking__ import *


class MyKeyboardListeners:

    def __init__(self) -> None:
        MyLifeCycles.__init__(self)
        self._on_key_up_listener = None
        self._on_key_down_listener = None
        self._on_key_press_listener = None
        self._pressed_keys: List['pygame.event.Event'] = list()

    def remove_on_key_down_listener(self):
        self._on_key_down_listener = None

    def remove_on_key_up_listener(self):
        self._on_key_up_listener = None

    def remove_on_key_press_listener(self):
        self._on_key_press_listener = None

    def set_on_key_down_listener(self, func):
        self._on_key_down_listener = func

    def set_on_key_up_listener(self, func):
        self._on_key_up_listener = func

    def set_on_key_press_listener(self, func):
        self._on_key_press_listener = func

    def is_keyboard_event_present(self) -> bool:
        return self._on_key_up_listener is not None or self._on_key_down_listener is not None or self._on_key_press_listener is not None

    def on_key_up(self, sender: object, event: pygame.event.Event) -> bool:
        if self._on_key_up_listener is not None:
            self._on_key_up_listener(sender, event)

    def on_key_down(self, sender: object, event: pygame.event.Event) -> bool:
        if self._on_key_down_listener is not None:
            self._on_key_down_listener(sender, event)

    def on_key_press(self, sender: object, event: pygame.event.Event) -> bool:
        if self._on_key_press_listener is not None:
            self._on_key_press_listener(sender, event)

    def do_key_event(self, sender: object, event: pygame.event.Event) -> bool:
        # ret: bool = False
        #print(len(self._pressed_keys))
        if event.type == pygame.KEYUP:
            for e in self._pressed_keys:
                if e.key == event.key:
                    self._pressed_keys.remove(e)
            if self.on_key_up(sender, event):
                pass
                # ret = True
        if event.type == pygame.KEYDOWN:
            self._pressed_keys.append(event)
            if self.on_key_down(sender, event):
                pass
                # ret = True
        return False

    def do_keypress_event(self):
        for e in self._pressed_keys:
            self.on_key_press(self, e)
