import pygame as p
import weakref

meteorI = p.image.load("vfx//sprites//meteor1.png")


class Meteor:
    meteors = weakref.WeakSet()

    def __init__(self, type, vel, sprite):
        self.type = type
        self.vel = vel
        self.sprite = sprite
        self.pos = (0,0)
        self.__class__.meteors.add(self)

    @classmethod
    def getMeteors(cls):
        return cls.meteors
    