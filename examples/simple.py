import os

# print(os.environ['PYTHONPATH'].split(os.pathsep))


import kigame

ACCELERATION_OF_GRAVITY = -0.1

image = kigame.Sprite(source='fly.png', pos=(20, 20))

speed = 10


def loop():
    global speed

    if kigame.key.spacebar:
        speed += 0.5

    image.y += speed
    speed += ACCELERATION_OF_GRAVITY


kigame.GameApp().run()
