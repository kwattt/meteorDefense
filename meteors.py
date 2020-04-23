import weakref
import numpy as np
import pygame as p

class Meteor:
    meteors = weakref.WeakSet()
    def __init__(self, typeX, vel, xsize):

        self.type = typeX
        self.mSize = 0

        if self.type == 0:
            self.mSize = 70
            self.sprite = p.image.load("vfx/sprites/meteor1.png")
        elif self.type == 1:
            self.mSize = 45
            self.sprite = p.image.load("vfx/sprites/meteor2.png")

        self.vel = vel
        self.size = (self.mSize, self.mSize)
        self.pos = (np.random.randint(20,xsize-20),0)

        self.cann = p.transform.scale(self.sprite, self.size)
        self.angle = 0
        self.hitbox = (self.pos[0]-self.size[0]/2, self.pos[1]-self.size[1]/2, \
            self.mSize-10, self.mSize-10)
        self.sprite_rect = None

        self.__class__.meteors.add(self)

    def UpdatePos(self):
        self.hitbox = (self.pos[0]-self.size[0]/2, self.pos[1]-self.size[1]/2, \
            self.mSize-10, self.mSize-10)

        self.pos = (self.pos[0], self.pos[1]+self.vel)
        self.angle = (self.angle+1*np.sqrt(self.vel*3))%360

    def Draw(self, win, hitbox = False):
        self.sprite = p.transform.rotate(self.cann, self.angle)
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
    def getMeteors(cls):
        return cls.meteors
    