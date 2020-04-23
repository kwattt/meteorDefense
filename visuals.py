import pygame as p 
import numpy as np

class bg():
    def __init__(self):
        self.bgg = p.image.load('vfx/background/space.jpg').convert()
    def Draw(self, win):
        win.blit(self.bgg, (0,0))

class Cannon:
    def __init__(self,screenSize_x, screenSize_y):
        self.xsize = 20
        self.ysize = 70

        self.xpos = 20
        self.ypos = screenSize_y-self.ysize-20

        self.sprite = p.image.load('vfx/sprites/cannon.png')
        self.cann = p.transform.scale(self.sprite, (self.xsize,self.ysize))

    def AngleToMouse(self,screenSize_y):
        mpos = np.array(p.mouse.get_pos())
        cpos = np.array((self.xpos, self.ypos))
        bpos = np.array((self.xpos, screenSize_y))

        A = np.linalg.norm(np.abs(mpos-cpos))
        B = np.linalg.norm(np.abs(cpos-bpos))
        C = np.linalg.norm(np.abs(mpos-bpos))
        
        return np.degrees(np.arccos((A * A + B * B - C * C)/(2.0 * A * B)))

    def Draw(self,win,angle):
        self.sprite = p.transform.rotate(self.cann, angle%360)
        self.sprite_rect = self.sprite.get_rect()

        self.sprite_rect.center = (self.xpos, self.ypos)
        win.blit(self.sprite, self.sprite_rect)

def showFps(win,clock):
    fps_overlay = p.font.SysFont("Verdana", 15).render(str(clock.get_fps()), True, p.Color("goldenrod"))
    win.blit(fps_overlay, (0, 0))