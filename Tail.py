__author__ = 'mosterann'

import pygame
from GameObject import GameObject


class Tail(GameObject):

    def __init__(self, tail, hasTail, rect):
        super(self.__class__, self).__init__("tail.png")
        self.hasTail = hasTail
        self.tail = tail
        self.rect = rect

    def update(self, rect):
        # Update tails behind you recursivly
        if(self.hasTail):
            self.tail.update(self.rect)
        # Update yourself
        self.rect = rect


    def collide(self, rect):

        collision = rect.colliderect(self.rect)

        if(collision):
            return collision

        if(self.hasTail):
            collision = self.tail.collide(rect)

        return collision



    def render(self):
        if(self.hasTail):
            self.tail.render()
        self.screen.blit(self.image, (self.rect))