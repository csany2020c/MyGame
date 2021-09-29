import game

print(__name__)

r1 = game.simpleworld.MyRectangle()
for i in range(0, 8):
    r1.rotateBy(45)
    print(r1.getCorners())


c1 = game.simpleworld.MyCircle()
for i in range(0, 8):
    c1.rotateBy(45)
    print(c1.getCorners())

r2 = game.simpleworld.MyRectangle(x = 0, y = 0)
r3 = game.simpleworld.MyRectangle(x = 10, y = 0)
for i in range(0, 20):
    print(game.simpleworld.Overlaps.rect_vs_rect(r2, r3))
    r2.setX(r2.getX()+0.5)


c2 = game.simpleworld.MyCircle(x = 0, y = 0)
c3 = game.simpleworld.MyCircle(x = 10, y = 0)
for i in range(0, 20):
    print(game.simpleworld.Overlaps.circle_vs_circle(c2, c3))
    c2.setX(c2.getX()+0.5)

r4 = game.simpleworld.MyRectangle(x = 0, y = 0)
r5 = game.simpleworld.MyRectangle(x = 1.1, y = 0)
for i in range(0, 36):
    print(game.simpleworld.Overlaps.rect_vs_rect(r4, r5))
    r4.rotateBy(10)

