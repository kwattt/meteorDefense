import pygame as p
import meteors
import visuals as v
import math

def mainSetup():
    
    global screenSize_x,screenSize_y
    
    screenSize_x = 400
    screenSize_y = 600
    
    global win, clock
    win = p.display.set_mode((screenSize_x,screenSize_y))
    clock = p.time.Clock()



def main():
    gameExit = False

    Cannon = v.Cannon()
    deg = 0

    while not gameExit:

        
        #Manejo de eventos de pygame.
        for e in p.event.get():
            if e.type == p.QUIT:
                gameExit = True 

            elif e.type == p.MOUSEBUTTONUP:
                x,y = p.mouse.get_pos()
                deg = math.degrees(math.atan2(-1*y-Cannon.ypos, x-Cannon.xpos))
                print(deg+90)

        v.backgrounDraw()

        Cannon.Draw(deg+90)

        clock.tick(60) # 30fps
        p.display.flip() # update-screen

mainSetup()
main()