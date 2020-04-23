import pygame as p
import weakref
import numpy as np

class Meteor:
    meteors = weakref.WeakSet()

    def __init__(self, type, vel, sprite, xsize):

        self.type = type
        self.vel = vel
        self.sprite = sprite

        self.pos = (np.random.randint(20,xsize-20),0)

        self.sprite = p.image.load("vfx//sprites//meteor1.png")
        self.cann = p.transform.scale(self.sprite, (20,70))

        self.__class__.meteors.add(self)
        print(Meteor.meteors)

    def UpdatePos(self):
        self.pos = (self.pos[0], self.pos[1]+self.vel)

    def Draw(self,win,angle):
        self.sprite = p.transform.rotate(self.cann, angle%360)
        self.sprite_rect = self.sprite.get_rect()

        self.sprite_rect.center = self.pos
        win.blit(self.sprite, self.sprite_rect)

    @classmethod
    def getMeteors(cls):
        return cls.meteors
    