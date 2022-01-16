import kigame
import random


images = []
for i in range(500):
    image = kigame.Sprite(
        source='alienBlue_walk1.png',
        pos=(random.randint(-100, kigame.Window.width), random.randint(0, kigame.Window.height - 200)))
    images.append(image)

speed = 10


def update():
    global speed

    for image in images:
        if image.left > kigame.Window.width:
            image.right = 0
        else:
            image.x += speed

kigame.run()
