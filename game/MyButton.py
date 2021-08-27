class MyButton(MyActor, MyText):

    def __init__(self, image="blank.png", pos=(0, 0), anchor=(0, 0), width:int=256, height:int=64, **kwargs):
        super().__init__(image, pos, anchor, **kwargs)
        MyText.__init__(self)
        self.set_size(width, height)
        self.set_x(20)
        self.set_y(80)

    def draw(self):
        super().draw()
        Screen(pygame.display.get_surface()).draw.text(self.text, (self.x, self.y), angle=self.angle, color=self.color, background=self.background, fontname=self.fontname, fontsize=self.fontsize, alpha=self.alpha)
