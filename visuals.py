import pygame as p 

class bg():
    def __init__(self):
        self.bgg = p.image.load('vfx/background/space.jpg').convert()
   
    def Draw(self):
        from main import win
        win.blit(self.bgg, (0,0))

class Cannon:
    def __init__(self):
        from main import screenSize_x, screenSize_y
        
        self.xsize = 20
        self.ysize = 70

        self.xpos = 20
        self.ypos = screenSize_y-self.ysize-20

        self.sprite = p.image.load('vfx/sprites/cannon.png')
        self.cann = p.transform.scale(self.sprite, (self.xsize,self.ysize))

    def Draw(self,angle):
        self.sprite = p.transform.rotate(self.cann, angle%360)
        self.sprite_rect = self.sprite.get_rect()

        self.sprite_rect.center = (self.xpos, self.ypos)
        from main import win
        win.blit(self.sprite, self.sprite_rect)

def showFps():
    from main import win, clock
    fps_overlay = p.font.SysFont("Verdana", 20).render(str(clock.get_fps()), True, p.Color("goldenrod"))
    win.blit(fps_overlay, (0, 0))