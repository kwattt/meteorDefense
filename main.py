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
    maxFrames = 100
    frameCount = 0

    win = p.display.set_mode((screenSize_x,screenSize_y))
    clock = p.time.Clock()

    p.event.set_allowed([p.QUIT, p.MOUSEBUTTONUP, p.KEYUP])

# GameStatus #
# 0 -> menu
# 1 -> ingame 0

def Generate():
    global frameCount,spawnMet

    if frameCount == spawnResult:
        tres = int (np.random.uniform(0.0, spawnDif)*maxFrames) 
        #print(tres+spawnResult)
        spawnMet = spawnResult 
         
    if spawnMet == frameCount:
        frameCount = 0

    allMeteors.append(m.Meteor(0, np.random.uniform(1.0, 2.0), 0, screenSize_x))

    frameCount += 1

def main():
    global allMeteors

    allMeteors = []

    global spawnRate, spawnDif, spawnResult, spawnMet

    spawnMet = 0
    
    # por segundo.
    spawnRate = 0.4
    spawnDif = 0.1

    spawnResult = int(spawnRate*maxFrames)

    gameStatus = 1
    gameExit = False

    dg = 0

    Cannon = v.Cannon(screenSize_x, screenSize_y)
    bg = v.bg()

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

        ## 

        ## Mostrar assets generales.        

        bg.Draw(win)
        Cannon.Draw(win,dg)
        v.showFps(win,clock)

        # Generar meteoros. 
        Generate()

        # Loop meteoros.
        for met in m.Meteor.getMeteors():

            met.UpdatePos()
            met.Draw(win, 0)

        clock.tick(maxFrames) # setFrameRate
        p.display.flip() # update-screen

mainSetup()
main()