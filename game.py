from pgzero.actor import Actor
import pgzrun

WIDTH = 960
HEIGHT = 640

speed = 6
enemySpeed = 2
enemySpeed2 = 2

neko = Actor('front')
neko.pos = WIDTH / 2, HEIGHT / 2

enemy = Actor('enemy')
enemy.pos = 64, HEIGHT / 2

enemy2 = Actor('enemy6')
enemy2.pos = WIDTH / 2, 64

retour = False
retour2 = False
def draw():
    screen.blit('map', (0, 0))
    neko.draw()
    enemy.draw()
    enemy2.draw()
    
def update():
    joueur()
    enemi()
    enemi2()
def joueur():
    # Keyboard input
    if keyboard.left:
        neko.x -= speed
        neko.image = 'left'
    if keyboard.right:
        neko.x += speed
        neko.image = 'right'
    if keyboard.up:
        neko.y -= speed
        neko.image = 'back'
    if keyboard.down:
        neko.y += speed
        neko.image = 'front'
    if keyboard.space:
        sounds.jump.play()


def enemi():
    global retour
    if neko.colliderect(enemy):
       enemy.image = 'enemy3' 
    else:
       enemy.image = 'enemy'
    if enemy.x>896:
        retour = True
    if enemy.x<64:
        retour = False
    
    if retour:
       enemy.x -= enemySpeed
    else:
       enemy.x += enemySpeed


def enemi2():
    global retour2
    if neko.colliderect(enemy2):
       enemy2.image = 'enemy5'
    else:
       enemy2.image = 'enemy6' 
    if enemy2.y>576:
        retour2 = True
    if enemy2.y<64:
        retour2 = False
       
    if retour2:
       enemy2.y -= enemySpeed2
    else:
       enemy2.y += enemySpeed2














pgzrun.go()
