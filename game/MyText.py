
class MyText(MyBaseActor):
    text: str = "The quick brown fox jumps over the lazy dog."
    color = (255, 255, 255)
    alpha: float = 1
    background = None
    fontname = None
    fontsize = 32

    def set_color(self, r: int, g: int, b: int, a: float = 1):
        self.color = (r, g, b)
        self.alpha = a

    def set_background(self, r: int, g: int, b: int):
        self.color = (r, g, b)

    def set_text(self, text: str):
        self.text = text

    def set_alpha(self, a: float):
        self.alpha = a

    def set_fontname(self, fontname: str):
        self.fontname = fontname

    def set_fontsize(self, size: float):
        self.fontsize = size
