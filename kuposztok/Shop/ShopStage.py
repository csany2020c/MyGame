import game
import pygame

from kuposztok.Shop.ShopActors import ShopActor


class ShopStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        bg = ShopActor()
        self.add_actor(bg)
        from kuposztok.Menu.MenuStage import MenuStage
        self.money = MenuStage.getMoneyMenu()
        self.moneyLabel = game.scene2d.MyLabel("Your money: " + self.money)
        self.add_actor(self.moneyLabel)