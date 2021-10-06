import game


class Background(game.scene2d.MyActor):
    def __init__(self, image_url: str = '../fujpacal/images/geryhatter.jpg'):
        super().__init__(image_url)
        pygame.init()
        self.info = pygame.display.Info()
        self.width = self.info.current_w
        self.height = self.info.current_h
        self.set_size(1280, 720)

Background().run()