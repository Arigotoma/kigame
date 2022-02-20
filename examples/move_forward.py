import kigame

alien = kigame.Sprite(source='alienBlue_walk1.png', pos=(20, 20))


def update():
    global speed

    if kigame.key.left:
        alien.angle += 1

    if kigame.key.right:
        alien.angle -= 1

    if kigame.key.up:
        alien.forward(1)

    if kigame.key.down:
        alien.forward(-1)


kigame.run()
