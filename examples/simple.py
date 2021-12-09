import os

# print(os.environ['PYTHONPATH'].split(os.pathsep))


import kigame

ACCELERATION_OF_GRAVITY = -0.1

image = kigame.Sprite(source='alienBlue_walk1.png', pos=(20, 20))
image.add_texture('alienBlue_walk2.png')

speed = 10


def update():
    global speed

    if kigame.key.spacebar:
        speed += 0.5

    image.y += speed
    speed += ACCELERATION_OF_GRAVITY

    if speed > 0:
        image.next_texture()


kigame.GameApp().run()
