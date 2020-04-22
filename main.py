import pygame as p


def mainSetup():
    global screen, clock
    
    screen = p.display.set_mode((600,600))
    clock = p.time.Clock()

def main():
    done = False
    while not done:
        screen.fill((0,0,0))
        p.display.flip() #update-screen

mainSetup()
main()