import pgzrun
from random import random
#player 

player = Actor("aliens")
player.x = 400 
player.y = 600 - player.height * 0.5 

speed = 10
lasers = [] 

#Spaceship
spaceships = []
def add_spaceship():
    spaceship = Actor("spaceship")  
    spaceship.x = 800 * random()
    spaceship.y = 300# spaceship.height * 0.5
    spaceships.append(spaceship)
clock.schedule_interval(add_spaceship, 5)
add_spaceship()
def fire_laser():
    laser = Rect((player.x - 2, player.y),(5,10))
    lasers.append(laser)

def update():

    if keyboard.left and player.x > player.width * 0.5:
        player.x -= speed

    if keyboard.right and player.x < 800 - player.width * 0.5:
        player.x += speed 

    if keyboard.up: 
        pass 

    if keyboard.down:
        pass      

    if keyboard.space:
        fire_laser()

    for spaceship in spaceships:
        spaceship.y += 3
    for laser in lasers:
        laser.y -= 10 
        for spaceship in spaceships:
            if laser.x > spaceship.x - spaceship.width * 0.5:
                if laser.y > spaceship.y - spaceship.height * 0.5:
                    if laser.x < spaceship.x + spaceship.width * 0.5:
                        if laser.y < spaceship.y + spaceship.height * 0.5:
                            spaceships.remove(spaceship)

def draw():
    screen.clear()
    player.draw()
    for spaceship in spaceships:   
       spaceship.draw()
    for laser in lasers:
       screen.draw.filled_rect(laser,(118,244,165)) 


pgzrun.go()

