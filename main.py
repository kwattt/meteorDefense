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
    maxFrames = 120
    frameCount = 0

    win = p.display.set_mode((screenSize_x,screenSize_y))
    clock = p.time.Clock()

    p.event.set_allowed([p.QUIT, p.MOUSEBUTTONUP, p.KEYUP])

# GameStatus #spawnMet
# 0 -> menu
# 1 -> ingame 0

spawnMet = 0
def Generate():
    global frameCount,spawnMet

    if frameCount == spawnResult:
        spawnMet = spawnResult + int (np.random.uniform(0.0, spawnDif)*maxFrames) 

    if spawnMet == frameCount:
        frameCount = 0
        sel = 0
        bspeed = 0
        if gameStatus == 1:
            if np.random.randint(0,3) == 0:
                sel = 1
                bspeed = np.random.uniform(-0.2, 0.8)
            else:
                sel = 0 

        allMeteors.append(m.Meteor(sel, np.random.uniform(1.0, 2.4-bspeed), screenSize_x))

    frameCount += 1

def main():
    global allMeteors, gameStatus

    allMeteors = []

    global spawnRate, spawnDif, spawnResult

    # sobre segundo.
    spawnRate = 0.01
    spawnDif = 0.00

    spawnResult = int(spawnRate*maxFrames)
    gameExit = False
    dg = 0

    Cannon = v.Cannon(screenSize_x, screenSize_y)
    bg = v.bg()
    mt = v.Mountain(screenSize_x, screenSize_y)


    gameStatus = 1
    while not gameExit:
        lMouse = (0,0)

        #Manejo de eventos de pygame.
        for e in p.event.get():
            if e.type == p.QUIT:
                gameStatus = 0
                gameExit = True 

            elif e.type == p.MOUSEBUTTONDOWN: # 
                lMouse = p.mouse.get_pos()
        
        ## Mostrar assets generales.        

        bg.Draw(win)
        mt.Draw(win)
        Cannon.Draw(win,dg)

        # Generar meteoros. 
        Generate()

        # Loop meteoros.
        for met in m.Meteor.getMeteors():
            met.UpdatePos()
            met.Draw(win, hitbox=True)
            
            if lMouse[0] > 0:
                mx,my = lMouse
                x,y = met.pos
                if mx < x+met.hitbox[2]/2 and mx > x-met.hitbox[2]/2:
                    if my < y+met.hitbox[3]/2 and my > y-met.hitbox[3]/2:
                        allMeteors.remove(met)
                        del met
                        lMouse = (0,0)

                        #rotat&shoot
                        dg = Cannon.AngleToMouse(screenSize_y)
                        continue                        

            #coll mountain 
            if met.pos[1]+met.hitbox[3]/2 > mt.hitbox[1]:
                allMeteors.remove(met)
                del met

        v.showFps(win,clock)

        clock.tick(maxFrames) # setFrameRate
        p.display.flip() # update-screen

mainSetup()
main()