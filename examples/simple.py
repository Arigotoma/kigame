import kigame

ACCELERATION_OF_GRAVITY = -0.2

image = kigame.Sprite(pos=(20, 20))

speed = 10


def loop():
    global speed

    if kigame.key.spacebar:
        speed += 1

    image.y += speed
    speed += ACCELERATION_OF_GRAVITY


kigame.GameApp().run()
