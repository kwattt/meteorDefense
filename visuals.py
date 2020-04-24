import weakref
import numpy as np
import pygame as p

class Mountain():
    def __init__(self, xsize, ysize):
        self.xsize = xsize
        self.ysize = ysize
        self.bg = p.image.load('vfx/sprites/mountain.png')
        self.cann = p.transform.scale(self.bg, (xsize, 150))
        self.hitbox = (0, ysize-115 ,xsize, 20)

    def Draw(self, win):
        win.blit(self.cann, (0, self.ysize-150))
        #p.draw.rect(win,(255,0,0), self.hitbox)

class bg():
    def __init__(self):
        self.bgg = p.image.load('vfx/background/space.jpg').convert()
    def Draw(self, win):
        win.blit(self.bgg, (0,0))

class Cannon:
    def __init__(self, screenSize_y):
        self.xpos = 20
        self.ypos = screenSize_y-50

        self.size = (10, 70)

        self.sprite = p.image.load('vfx/sprites/cannon.png')
        self.cann = p.transform.scale(self.sprite, self.size)
        self.sprite_rect = None
        self.last_angle = None

    def AngleToMouse(self, screenSize_y):
        mpos = np.array(p.mouse.get_pos())
        cpos = np.array((self.xpos, self.ypos))
        bpos = np.array((self.xpos, screenSize_y))

        A = np.linalg.norm(np.abs(mpos-cpos))
        B = np.linalg.norm(np.abs(cpos-bpos))
        C = np.linalg.norm(np.abs(mpos-bpos))

        return np.degrees(np.arccos((A * A + B * B - C * C)/(2.0 * A * B)))

    def Draw(self, win, angle):
        self.sprite = p.transform.rotate(self.cann, angle%360)
        self.last_angle = angle%360
        self.sprite_rect = self.sprite.get_rect()

        self.sprite_rect.center = (self.xpos, self.ypos)
        win.blit(self.sprite, self.sprite_rect)


class Proyectile:
    ptiles = weakref.WeakSet()
    def __init__(self, oxpos, oypos, txpos, typos, angle):
        self.xpos = oxpos
        self.ypos = oypos
        self.angle = angle

        self.size = (15, 25)
        self.tposx = txpos
        self.tposy = typos

        self.sprite = p.image.load('vfx/sprites/proyectile.png')
        self.cann = p.transform.scale(self.sprite, self.size)
        self.sprite_rect = None
        self.last_angle = None

        self.kme = False

        self.__class__.ptiles.add(self)

    def UpdatePos(self):
        vel = 69.0

        self.xpos, self.ypos = (self.xpos-(vel*np.cos(np.radians(-1.0*self.last_angle-90))), \
                self.ypos-(vel*np.sin(np.radians(-1.0*self.last_angle-90))))

        if self.xpos < self.tposx+70/2 and self.xpos > self.tposx-70/2:
            if self.ypos < self.tposy+70/2 and self.ypos > self.tposy-70/2:
                self.kme = True

    def Draw(self, win, angle):
        self.sprite = p.transform.rotate(self.cann, angle+180%360)
        self.last_angle = angle%360
        self.sprite_rect = self.sprite.get_rect()

        self.sprite_rect.center = (self.xpos, self.ypos)
        win.blit(self.sprite, self.sprite_rect)

    @classmethod
    def getProjectiles(cls):
        return cls.ptiles

def showFps(win, clock):
    fps_overlay = \
        p.font.SysFont("Verdana", 15).render(str(clock.get_fps()), True, p.Color("goldenrod"))
    win.blit(fps_overlay, (0, 0))
