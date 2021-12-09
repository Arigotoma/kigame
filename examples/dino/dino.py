import kigame

ACCELERATION_OF_GRAVITY = -0.2

terrain = kigame.Sprite('terrain.png')
terrain.bottom = 55

dino = kigame.Sprite('dino1.png')
dino.add_texture('dino2.png')
dino.add_texture('dino3.png')
dino.bottom = 70
dino.left = 40

dino_texture_index = 0


cacti = []
for i in range(3):
    cactus = kigame.Sprite('cacti1.png')
    cactus.bottom = 70
    cactus.left = kigame.Window.width + i*400
    cacti.append(cactus)


cloud = kigame.Sprite('cloud_small.png')
cloud.top = kigame.Window.height - 55


terrain_speed = 2
fall_speed = 0


def update():
    global fall_speed
    global terrain_speed
    global dino_texture_index

    for cactus in cacti:
        if dino.collide(cactus):
            return

    terrain_speed += 0.001

    for cactus in cacti:
        cactus.x -= terrain_speed

        if cactus.right <= 0:
            cactus.left = kigame.Window.width

    terrain.x -= terrain_speed
    if terrain.right <= kigame.Window.width:
        terrain.left = 0

    cloud.x -= terrain_speed - 0.5
    if terrain.right <= 0:
        terrain.left = kigame.Window.width

    if dino.bottom > 70:  # в прыжке
        fall_speed += ACCELERATION_OF_GRAVITY
    else:  # не в прыжке
        fall_speed = 0
        # прыгать можно только если персонаж стоит ан земле
        if kigame.key.spacebar:
            fall_speed = 10

    dino.y += fall_speed

    dino_texture_index += 1
    if dino_texture_index % 10 == 0:
        dino.next_texture()


kigame.run()
