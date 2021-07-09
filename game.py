from pgzero.actor import Actor
import pgzrun

WIDTH = 960
HEIGHT = 640

speed = 4

neko = Actor('front')
neko.pos = WIDTH / 2, HEIGHT / 2

crate = Actor('crate')
crate.pos = 200, HEIGHT / 2


def draw():
    screen.blit('map', (0, 0))
    neko.draw()
    crate.draw()


def update():
    collid = neko.colliderect(crate)
    # Keyboard input
    if keyboard.left:
        neko.x -= speed
        neko.image = 'left'
        if collid:
            crate.x -= speed
    if keyboard.right:
        neko.x += speed
        neko.image = 'right'
        if collid:
            crate.x += speed
    if keyboard.up:
        neko.y -= speed
        neko.image = 'back'
        if collid:
            crate.y -= speed
    if keyboard.down:
        neko.y += speed
        neko.image = 'front'
        if collid:
            crate.y += speed
    if keyboard.space:
        sounds.jump.play()


pgzrun.go()
