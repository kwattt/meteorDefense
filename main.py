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

    global win, clock, aevents
    
    win = p.display.set_mode((screenSize_x,screenSize_y))
    clock = p.time.Clock()

    p.event.set_allowed([p.QUIT, p.MOUSEBUTTONUP, p.KEYUP])

def main():
    gameExit = False

    Cannon = v.Cannon()
    bg = v.bg()
    dg = 0

    while not gameExit:

        #Manejo de eventos de pygame.
        for e in p.event.get():
            if e.type == p.QUIT:
                gameExit = True 

            elif e.type == p.MOUSEBUTTONUP:
                mpos = np.array(p.mouse.get_pos())
                cpos = np.array((Cannon.xpos, Cannon.ypos))
                bpos = np.array((Cannon.xpos, screenSize_y))

                A = np.linalg.norm(np.abs(mpos-cpos))
                B = np.linalg.norm(np.abs(cpos-bpos))
                C = np.linalg.norm(np.abs(mpos-bpos))

                dg = np.degrees(np.arccos((A * A + B * B - C * C)/(2.0 * A * B)))

        ## key control
        pkey = p.key.get_pressed()
        if pkey[p.K_UP]:
            Cannon.ypos-=1.0

        bg.Draw()
        Cannon.Draw(dg)
        v.showFps()

        clock.tick(60) # 30fps
        p.display.flip() # update-screen

mainSetup()
main()