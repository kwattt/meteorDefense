import pygame as p
import sys

def mainSetup():
    global screen, clock
    
    screen = p.display.set_mode((600,600))
    clock = p.time.Clock()

def main():
    gameExit = False
    while not gameExit:
        screen.fill((0,0,0))

        #Manejo de eventos de pygame.
        for e in p.event.get():
            if e.type == p.QUIT:
                gameExit = True
        rect1 = p.Rect(300,300, 20,20)
        
        p.draw.rect(screen, (255,255,255), rect1)

        p.display.flip() # update-screen
        clock.tick(30) # 30fps

mainSetup()
main()