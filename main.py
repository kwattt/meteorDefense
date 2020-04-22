import pygame as p
import meteors


def mainSetup():
    global win, clock
    
    win = p.display.set_mode((600,600))
    clock = p.time.Clock()

    
bg = p.image.load('vfx/background/space.jpg')

def drawBackground():
    win.blit(bg, (0,0))

def main():
    gameExit = False

    while not gameExit:

        
        #Manejo de eventos de pygame.
        for e in p.event.get():
            if e.type == p.QUIT:
                gameExit = True

        drawBackground()
        p.display.flip() # update-screen
        clock.tick(30) # 30fps

mainSetup()
main()