import pygame as p
import meteors as m
import visuals as v
import numpy as np

def mainSetup():
    
    global screenSize_x,screenSize_y
    
    screenSize_x = 400
    screenSize_y = 600
    
    p.init()

    global win, clock, gameStatus, frameCount, maxFrames
    gameStatus = 0
    maxFrames = 60
    frameCount = 0

    win = p.display.set_mode((screenSize_x,screenSize_y))
    clock = p.time.Clock()

    p.event.set_allowed([p.QUIT, p.MOUSEBUTTONUP, p.KEYUP])

# GameStatus #
# 0 -> menu
# 1 -> ingame 0

def Generate():
    global frameCount

    frameCount += 1
    if frameCount == spawnResult:
        frameCount = 0

def main():
    global spawnRate, spawnDif, spawnResult

    gameStatus = 1
    gameExit = False

    Cannon = v.Cannon(screenSize_x, screenSize_y)
    bg = v.bg()
    dg = 0

    # segundos.
    spawnRate = 0.2 
    # spawnRate dif en ms

    # spawnResult 4 Generate()
    spawnResult = int(spawnRate*maxFrames)

    while not gameExit:

        #Manejo de eventos de pygame.
        for e in p.event.get():
            if e.type == p.QUIT:
                gameStatus = 0
                gameExit = True 

            elif e.type == p.MOUSEBUTTONDOWN: # 
                # if meteorClicked -> Rotate & shoot
                dg = Cannon.AngleToMouse(screenSize_y)

        ## key control
        #pkey = p.key.get_pressed()
        #if pkey[p.K_UP]:
        #    Cannon.ypos-=1.0

        ## Mostrar assets.
            
        bg.Draw(win)
        Cannon.Draw(win,dg)
        v.showFps(win,clock)

        # Generar meteoros. 
        Generate()

        clock.tick(maxFrames) # setFrameRate
        p.display.flip() # update-screen

mainSetup()
main()