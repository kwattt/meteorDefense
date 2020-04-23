import pygame as p
import meteors
import visuals as v
import math
import numpy as np

def mainSetup():
    
    global screenSize_x,screenSize_y
    
    screenSize_x = 400
    screenSize_y = 600
    
    p.init()

    global win, clock, gameStatus, frameCount, maxFrames
    gameStatus = 0
    maxFrames = 60

    win = p.display.set_mode((screenSize_x,screenSize_y))
    clock = p.time.Clock()

    p.event.set_allowed([p.QUIT, p.MOUSEBUTTONUP, p.KEYUP])

# GameStatus #
# 0 -> menu
# 1 -> ingame 0

def main():
    gameStatus = 1
    gameExit = False

    Cannon = v.Cannon()
    bg = v.bg()
    dg = 0

    while not gameExit:

        #Manejo de eventos de pygame.
        for e in p.event.get():
            if e.type == p.QUIT:
                gameStatus = 0
                gameExit = True 

            elif e.type == p.MOUSEBUTTONDOWN: # 
                # if meteorClicked -> Rotate & shoot
                dg = Cannon.AngleToMouse()

        ## key control
        #pkey = p.key.get_pressed()
        #if pkey[p.K_UP]:
        #    Cannon.ypos-=1.0

        ## Mostrar assets.
            
        bg.Draw()
        Cannon.Draw(dg)
        v.showFps()

        clock.tick(maxFrames) # setFrameRate
        p.display.flip() # update-screen

mainSetup()
main()