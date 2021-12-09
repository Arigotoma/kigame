import kigame

alien = kigame.Sprite(source='alienBlue_walk1.png', pos=(20, 20))

speed = 10


def update():
    global speed

    if kigame.key.left:
        alien.angle += 1

    if kigame.key.right:
        alien.angle -= 1

    if kigame.key.up:
        alien.x += speed

    if kigame.key.down:
        alien.x -= speed


kigame.run()
