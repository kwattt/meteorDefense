import weakref
import numpy as np
import pygame as p

class Object:
    objects = weakref.WeakSet()
    def __init__(self, typeX, vel, xsize, ysize):

        self.type = typeX
        self.damage = 10

        if self.type == 0:
            self.damage = 10
            self.sprite = p.image.load("vfx/sprites/misil1.png")

        self.vel = vel
        self.size = (40, 70)
        self.pos = (np.random.randint(20, xsize-20), ysize-40)

        self.cann = p.transform.scale(self.sprite, self.size)
        self.hitbox = (self.pos[0]-self.size[0]/2, self.pos[1]-self.size[1]/2, \
            self.size[0]-15, self.size[1]-2)
        self.sprite_rect = None

        self.__class__.objects.add(self)

    def UpdatePos(self):
        self.hitbox = (self.pos[0]-self.size[0]/2, self.pos[1]-self.size[1]/2, \
            self.size[0]-10, self.size[1]-10)

        self.pos = (self.pos[0], self.pos[1]-self.vel)

    def Draw(self, win, hitbox=False):
        self.sprite = p.transform.rotate(self.cann, 0)
        self.sprite_rect = self.sprite.get_rect()

        self.sprite_rect.center = self.pos
        win.blit(self.sprite, self.sprite_rect)
        if hitbox:
            p.draw.rect(win, (255, 0, 0), (self.pos[0]+self.hitbox[2]/2, \
                self.pos[1]-self.hitbox[3]/2, 3, self.hitbox[3]))

            p.draw.rect(win, (255, 255, 0), (self.pos[0]-self.hitbox[2]/2, \
                self.pos[1]-self.hitbox[3]/2, 3, self.hitbox[3]))

            p.draw.rect(win, (255, 255, 255), (self.pos[0]-self.hitbox[2]/2, \
                self.pos[1]+self.hitbox[3]/2, self.hitbox[2], 3))

            p.draw.rect(win, (255, 0, 255), (self.pos[0]-self.hitbox[2]/2, \
                self.pos[1]-self.hitbox[3]/2, self.hitbox[2], 3))

    @classmethod
    def getObjects(cls):
        return cls.objects
    