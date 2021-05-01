# SEV Beginner - Introduction to Game Development

# start your game code here!

import pgzrun
import random

WIDTH = 800 #width of the window
HEIGHT = 600 #height of the window

BACKGROUND_IMG = "my_final_background"

player = Actor("spaceship_beg_up")
player.midbottom = (WIDTH/2, HEIGHT)

alien = Actor("alien_beg_sprite") #create alien actor
alien.pos = (random.randint(40,WIDTH-40), random.randint(100,HEIGHT-40)) #set inital position

score = 0
sounds.music_upbeat.play(-1)

def update():
    global score #since were changing the variable score within a function, we need to add the  
    
    if(keyboard.up == 1 and player.top > 0):
        player.y += -5 #moving up, so moving in NEGATIVE y direction
        player.image = "spaceship_beg_up"

    elif(keyboard.down == 1 and player.bottom < HEIGHT):
        player.y += 5 #moving down, so moving in the POSITIVE y difection
        player.image = "spaceship_beg_down"

    elif(keyboard.left ==1 and player.left > 0):
        player.x += -5 #moving left, so moving in the NEGATIVE x direction
        player.image = "spaceship_beg_left"

    elif(keyboard.right == 1 and player.right < WIDTH):
        player.x += 5 #moving right, so moving in the POSITIVE difrction
        player.image = "spaceship_beg_right"

    if(player.colliderect(alien) == 1):
        alien.pos = (random.randint(40,WIDTH-40), random.randint(100,HEIGHT-40))
        sounds.alien_device.play()
        score +=1
        
def draw():
    screen.clear()
    screen.blit(BACKGROUND_IMG, (0,0))
    player.draw()
    alien.draw()

    show_score = str(score)
    screen.draw.text(show_score,fontsize=45, topright=(750,30), color="white")




                     
pgzrun.go()                  
