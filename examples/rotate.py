import kigame

alien = kigame.Sprite(source='alienBlue_walk1.png', pos=(20, 20))
alien2 = kigame.Sprite(source='alienBlue_walk1.png', pos=(500, 500))

speed = 10


def update():
    global speed

    if kigame.key.spacebar:
        alien.forward(5)

    if kigame.key.left:
        alien.angle += 1

    if kigame.key.right:
        alien.angle -= 1

    if kigame.key.up:
        alien.y += speed

    if kigame.key.down:
        alien.y -= speed


kigame.run()
