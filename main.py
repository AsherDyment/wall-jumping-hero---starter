def on_a_pressed():
    if wall_jumping_master.is_hitting_tile(CollisionDirection.BOTTOM):
        wall_jumping_master.vy = -350
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_left_pressed():
    wall_jumping_master.set_image(leftFacingImg)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_right_pressed():
    wall_jumping_master.set_image(rightFacingImg)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

wall_jumping_master: Sprite = None
leftFacingImg: Image = None
rightFacingImg: Image = None
rightSwordOutImg = img("""
    . . . . . . . f f . . . . . . . 
        . . . . f f f f 2 f f . . . . . 
        . . f f e e e e f 2 f f . . . . 
        . f f e e e e e f 2 2 f f . . . 
        . f e e e e f f e e e e f . . . 
        . f f f f f e e 2 2 2 2 e f . . 
        f f f e 2 2 2 f f f f e 2 f . . 
        f f f f f f f f e e e f f f . . 
        f e f e 4 4 e b f 4 4 e e f . . 
        . f e e 4 d 4 b f d d e f . . . 
        . . f e e e 4 d d d e e . c . . 
        . . . f 2 2 2 2 e e d d e c c c 
        . . . f 4 4 4 e 4 4 d d e c d d 
        . . . f f f f f e e e e . c c c 
        . . f f f f f f f f . . . c . . 
        . . f f f . . f f . . . . . . .
""")
leftSwordOutImg = img("""
    . . . . . . . f f . . . . . . . 
        . . . . . f f 2 f f f f . . . . 
        . . . . f f 2 f e e e e f f . . 
        . . . f f 2 2 f e e e e e f f . 
        . . . f e e e e f f e e e e f . 
        . . f e 2 2 2 2 e e f f f f f . 
        . . f 2 e f f f f 2 2 2 e f f f 
        . . f f f e e e f f f f f f f f 
        . . f e e 4 4 f b e 4 4 e f e f 
        . . . f e d d f b 4 d 4 e e f . 
        . . c . e e d d d 4 e e e f . . 
        c c c e d d e e 2 2 2 2 f . . . 
        d d c e d d 4 4 e 4 4 4 f . . . 
        c c c . e e e e f f f f f . . . 
        . . c . . . f f f f f f f f . . 
        . . . . . . . f f . . f f f . .
""")
rightFacingImg = img("""
    . . . . . . . . . . . . . . . . 
        . . . . . f f f f f f . . . . . 
        . . . f f e e e e f 2 f . . . . 
        . . f f e e e e f 2 2 2 f . . . 
        . . f e e e f f e e e e f . . . 
        . . f f f f e e 2 2 2 2 e f . . 
        . . f e 2 2 2 f f f f e 2 f . . 
        . f f f f f f f e e e f f f . . 
        . f f e 4 4 e b f 4 4 e e f . . 
        . f e e 4 d 4 1 f d d e f . . . 
        . . f e e e e e d d d f . . . . 
        . . . . f 4 d d e 4 e f . . . . 
        . . . . f e d d e 2 2 f . . . . 
        . . . f f f e e f 5 5 f f . . . 
        . . . f f f f f f f f f f . . . 
        . . . . f f . . . f f f . . . .
""")
leftFacingImg = img("""
    . . . . . . . . . . . . . . . . 
        . . . . . f f f f f f . . . . . 
        . . . . f 2 f e e e e f f . . . 
        . . . f 2 2 2 f e e e e f f . . 
        . . . f e e e e f f e e e f . . 
        . . f e 2 2 2 2 e e f f f f . . 
        . . f 2 e f f f f 2 2 2 e f . . 
        . . f f f e e e f f f f f f f . 
        . . f e e 4 4 f b e 4 4 e f f . 
        . . . f e d d f 1 4 d 4 e e f . 
        . . . . f d d d e e e e e f . . 
        . . . . f e 4 e d d 4 f . . . . 
        . . . . f 2 2 e d d e f . . . . 
        . . . f f 5 5 f e e f f f . . . 
        . . . f f f f f f f f f f . . . 
        . . . . f f f . . . f f . . . .
""")
wall_jumping_master = sprites.create(rightFacingImg, SpriteKind.player)
controller.move_sprite(wall_jumping_master, 100, 0)
tiles.set_tilemap(tilemap("""
    level1
"""))
scene.camera_follow_sprite(wall_jumping_master)
tiles.place_on_tile(wall_jumping_master, tiles.get_tile_location(9, 31))
wall_jumping_master.ay = 1

def on_update_interval():
    if wall_jumping_master.is_hitting_tile(CollisionDirection.RIGHT):
        wall_jumping_master.set_image(rightSwordOutImg)
        wall_jumping_master.ay = 0
        wall_jumping_master.vy = 20
game.on_update_interval(500, on_update_interval)
