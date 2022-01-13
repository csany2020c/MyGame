from Impostorsus.Game.AnimatedWario import spritesheet

ss = spritesheet.spriteshee('actorsusus.png')
# Sprite is 16x16 pixels at location 0,0 in the file...
image = ss.image_at((0, 0, 16, 16))
images = []
# Load two images into an array, their transparent bit is (255, 255, 255)
images = ss.images_at((0, 0, 16, 16),(17, 0, 16,16), colorkey=(255, 255, 255))

#https://www.pygame.org/wiki/Spritesheet