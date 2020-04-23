import pygame as p
import numpy as np
import meteors as m
import visuals as v

def main_Setup():
    '''Initial Settings'''
    global screenSize_x, screenSize_y

    screenSize_x = 400
    screenSize_y = 600

    global win, clock, gameStatus, frameCount, maxFrames, minVel

    p.init()


    gameStatus = 0
    maxFrames = 60
    frameCount = 0

    minVel = 1/(maxFrames*2.0/120)
    print(minVel)

    win = p.display.set_mode((screenSize_x, screenSize_y))
    clock = p.time.Clock()

# GameStatus #spawnMet
# 0 -> menu
# 1 -> ingame mode 0

def Generate():
    '''Generador de meteoros'''

    if gameStatus == 200:
        return

    global frameCount, spawnMet

    if frameCount == spawnResult:
        spawnMet = spawnResult + int(np.random.uniform(0.0, spawnDif)*maxFrames)

    if spawnMet == frameCount:
        frameCount = 0
        sel = 0
        bspeed = 0
        if gameStatus == 1:
            if np.random.randint(0, 3) == 0:
                sel = 1
                bspeed = np.random.uniform(-0.2, 0.8)
            else:
                sel = 0

        allMeteors.append(m.Meteor(sel, minVel*(np.random.uniform(2.0, 4.4-bspeed)), screenSize_x))

    frameCount += 1

def checkHealth():
    global gameStatus
    if healthPoints <= 0:
        gameStatus = 200

def main():
    '''Game Loop'''
    global allMeteors, gameStatus

    allMeteors = []

    global spawnRate, spawnDif, spawnResult, spawnMet

    spawnMet = 0
    # sobre segundo.
    spawnRate = 0.45
    spawnDif = 0.15

    spawnResult = int(spawnRate*maxFrames)
    gameExit = False
    dg = 0

    Cannon = v.Cannon(screenSize_y)
    bg = v.bg()
    mt = v.Mountain(screenSize_x, screenSize_y)

    gameStatus = 1

    global healthPoints
    healthPoints = 100

    while not gameExit:
        mPos = (0, 0)

        #Manejo de eventos de pygame.
        for e in p.event.get():
            if e.type == p.QUIT:
                gameStatus = 0
                gameExit = True

            elif e.type == p.MOUSEBUTTONDOWN:
                mPos = p.mouse.get_pos()

        ## Mostrar assets generales

        bg.Draw(win)
        mt.Draw(win)
        Cannon.Draw(win, dg)

        # Generar meteoros
        Generate()

        # Loop meteoros.
        for met in m.Meteor.getMeteors():
            met.UpdatePos()
            met.Draw(win, hitbox=True)

            if mPos[0] > 0:
                mx, my = mPos
                x, y = met.pos
                if mx < x+met.hitbox[2]/2 and mx > x-met.hitbox[2]/2:
                    if my < y+met.hitbox[3]/2 and my > y-met.hitbox[3]/2:
                        allMeteors.remove(met)
                        del met
                        mPos = (0, 0)

                        #rotat&shoot
                        dg = Cannon.AngleToMouse(screenSize_y)
                        continue

            #coll mountain
            if met.pos[1]+met.hitbox[3]/2 > mt.hitbox[1]:
#                healthPoints -= met.damage

                allMeteors.remove(met)
                del met

                checkHealth()

        v.showFps(win, clock)

        clock.tick(maxFrames) # setFrameRate
        p.display.flip() # update-screen

        if gameStatus == 200:
            print("Perdiste!")



main_Setup()
main()
