import pgzrun
import sys
import os
import random

TITLE = "Bug Fix"

WIDTH = 700
HEIGHT = 600
score = 0

plr1 = Actor("plr1")
plr1.pos=(100,100)

plr2 = Actor("plr2")
plr2.pos=(200,200)

def draw():
    screen.blit("bg",(0,0))
    screen.draw.text("Score: "+str(score),color="blue",topleft=(10,10))
    plr1.draw()
    plr2.draw()
    
pgzrun.go()