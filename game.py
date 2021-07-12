from pgzero.actor import Actor
import pgzrun

WIDTH = 960
HEIGHT = 640

speed = 6
enemySpeed = 2
enemySpeed2 = 3
enemySpeed3 = 1

neko = Actor('front')
neko.pos = WIDTH / 2, HEIGHT / 2

enemy = Actor('enemy')
enemy.pos = 64, HEIGHT / 2

enemy2 = Actor('enemy6')
enemy2.pos = WIDTH / 2, 64

boss = Actor('boss')
boss.pos = WIDTH / 2, HEIGHT / 2

enemy3 = Actor('enemy8')
enemy3.pos = 896, HEIGHT / 2

retour = False
retour2 = False
retour3 = False
def draw():
    screen.blit('map', (0, 0))
    neko.draw()
    enemy.draw()
    enemy2.draw()
    boss.opacity = 0
    enemy3.draw()
def update():
    joueur()
    enemi()
    enemi2()
    boss1()
    enemi3()
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

def boss1():
    if neko.colliderect(enemy2):
       boss.opacity = 1
       
 
def enemi3():
    global retour3
    if neko.colliderect(enemy3):
       enemy3.image = 'enemy9'
    else:
       enemy3.image = 'enemy8'
    if enemy3.x<64:
       retour3 = True
    if enemy3.x>896:
       retour3 = False 
    
    if retour3:
       enemy3.x += enemySpeed3
    else:
       enemy3.x -= enemySpeed3 


pgzrun.go()
