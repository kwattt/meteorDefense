import pygame as p
import weakref
import numpy as np

mSize = 70

class Meteor:
    meteors = weakref.WeakSet()

    def __init__(self, type, vel, sprite, xsize):

        self.type = type
        self.vel = vel
        self.sprite = sprite

        self.size = (mSize,mSize)
        
        self.pos = (np.random.randint(20,xsize-20),0)
        
        self.sprite = p.image.load("vfx//sprites//meteor1.png")
        self.cann = p.transform.scale(self.sprite, self.size)

        self.__class__.meteors.add(self)

    def UpdatePos(self):
        self.hitbox = (self.pos[0]-self.size[0]/2, self.pos[1]-self.size[1]/2  ,mSize-10, mSize-10) 
        self.pos = (self.pos[0], self.pos[1]+self.vel)

    def Draw(self,win,angle):
        self.sprite = p.transform.rotate(self.cann, angle%360)
        self.sprite_rect = self.sprite.get_rect()

        self.sprite_rect.center = self.pos
        win.blit(self.sprite, self.sprite_rect)
        #p.draw.rect(win,(255,0,0), self.hitbox)

    @classmethod
    def getMeteors(cls):
        return cls.meteors
    