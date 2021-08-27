import pygame
from game.MyLifeCycles import *
from game.MyTimer import *
from game.MyBaseListeners import *


class MyBaseActor(MyLifeCycles):

    def __init__(self) -> None:
        self.elapsed_time: float = 0
        self._stage: 'MyStage' = 0
        self.timers = list()
        self.create()

    def add_timer(self, timer: 'MyBaseTimer'):
        if isinstance(timer, MyBaseTimer):
            self.timers.append(timer)
            if timer.base_actor != 0:
                timer.remove()
            timer.base_actor = self
        else:
            print("ERROR: Az objektum példány nem adható hozzá a staghez, mert nem a MyBaseTimer leszármazottja.")

    def remove_timer(self, timer: 'MyBaseTimer'):
        try:
            self.timers.remove(timer)
            timer.base_actor = 0
        except ValueError:
            print("A következő objektum már el lett távolítva korábban: " + str(id(self)))

    def get_delta_time(self) -> float:
        return self._stage.screen.game.get_delta_time()

    def act(self):
        self.elapsed_time += self.get_delta_time()
        for obj in self.timers:
            obj.act()

    def remove_from_stage(self):
        try:
            self._stage.remove_actor(actor=self)
        except ValueError:
            print("A következő objektum már el lett távolítva korábban: " + str(id(self)))

    def set_stage(self, stage: 'MyStage'):
        self._stage = stage
        if stage == None:
            self.hide()
        else:
            self.show()

    def is_on_stage(self) -> bool:
        return self._stage != 0


class MyActor(MyBaseActor, MyBaseListeners):

    def __init__(self, image_url: str = ""):
        MyBaseActor.__init__(self)
        MyBaseListeners.__init__(self)
        self.x = 0
        self.y = 0
        self._r = 0
        self._w = 0
        self._h = 0
        self._box = [[0, 0], [0, 0], [0, 0], [0, 0]]
        self.original_image: pygame.Surface = None
        self.image: pygame.Surface = None
        if image_url != "":
            self.set_image(image_url)

    #
    # def overlaps_with(self, otheractor: 'MyActor') -> bool:
    #     return self.colliderect(otheractor)
    #
    # def overlaps_point(self, pos) -> bool:
    #     return self.collidepoint(pos)
    #
    # def on_mouse_down(self, pos, button):
    #     if self.overlaps_point(pos):
    #         if self._on_mouse_down_listener != 0:
    #             self._on_mouse_down_listener(pos, button)
    #
    # def on_mouse_up(self, pos, button):
    #     if self.overlaps_point(pos):
    #         if self._on_mouse_up_listener != 0:
    #             self._on_mouse_up_listener(pos, button)
    #
    # def on_mouse_move(self, pos):
    #     if self.overlaps_point(pos):
    #         if self._on_mouse_move_listener != 0:
    #             self._on_mouse_move_listener(pos)
    #
    # def on_key_down(self, key, mod, unicode):
    #     if self._on_key_down_listener != 0:
    #         self._on_key_down_listener(key, mod, unicode)
    #
    # def on_key_up(self, key, mod):
    #     if self._on_key_up_listener != 0:
    #         self._on_key_up_listener(key, mod)

    def set_image(self, image_url: str):
        self.original_image = pygame.image.load(image_url)
        self.image = self.original_image
        self._w = self.image.get_width()
        self._h = self.image.get_height()
        self.calc_box()
        print(str(self) + " Set image: " + image_url + " " + str(self.image.get_width()) + " x " + str(self.image.get_height()))

    def calc_box(self):
        self._box = [list(self.image.get_rect().bottomleft), list(self.image.get_rect().bottomright),
                     list(self.image.get_rect().topright), list(self.image.get_rect().topleft)]
        for i in range(4):
            self._box[i][0] += self.x
            self._box[i][1] += self.y
        print(self._box)

    def transform(self):
        if self._r != 0:
            self.image = pygame.transform.smoothscale(self.original_image, (self._w, self._h))
            self.calc_box()
            self.image = pygame.transform.rotate(self.image, self._r)
        else:
            self.image = pygame.transform.smoothscale(self.original_image, (self._w, self._h))
            self.calc_box()

    def set_size(self, width: int, height: int):
        self._w = width
        self._h = height
        self.transform()
        # if width == -1 and height == -1:
        #     if self._w == -1 and self._h == -1:
        #         self._surf = pygame.transform.scale(self._surf, (self.width, self.height))
        #     else:
        #         self._surf = pygame.transform.scale(self._surf, (self._w, self._h))
        # else:
        #     self._surf = pygame.transform.scale(self._surf, (width, height))
        #     self._w = width
        #     self._h = height
        # self._update_pos()

    def set_rotation(self, degree: int):
        self.angle = degree
        self.set_size(-1, -1)

    def rotate_with(self, degree: int):
        self.set_rotation(self.angle + degree)

    def set_x(self, x: int):
        self.x = x

    def set_y(self, y: int):
        self.y = y

    def get_x(self) -> int:
        return self.x

    def get_y(self) -> int:
        return self.y

    def set_width(self, width: int, aspect_ratio: bool = True):
        if aspect_ratio:
            self.set_size(width, int(float(self.h) * (float(width) / float(self.w))))
        else:
            self.set_size(width, self.h)

    def set_height(self, height: int, aspect_ratio: bool = True):
        if aspect_ratio:
            self.set_size(int(float(self.w) * (float(height) / float(self.h))), height)
        else:
            self.set_size(self.w, height)

    def get_width(self)->int:
        return self._w

    def get_height(self)->int:
        return self._h

    def draw(self):
        super().draw()
        self._stage.screen.game.pgScreen.blit(self.image, (
            self.x - self.image.get_width() / 2 + self._w / 2, self.y - self.image.get_height() / 2 + self._h / 2))

        for i in range(3):
            pygame.draw.line(self._stage.screen.game.pgScreen, color=(0, 200, 27), start_pos=self._box[i],
                             end_pos=self._box[i + 1])
        pygame.draw.line(self._stage.screen.game.pgScreen, color=(0, 200, 27), start_pos=self._box[0],
                         end_pos=self._box[3])

    def set_rotation(self, angle: int):
        self._r = angle
        self.transform()

    def get_rotation(self) -> int:
        return self._r

    w: int = property(get_width, set_width)
    h: int = property(get_height, set_height)
    r: int = property(get_rotation, set_rotation)


