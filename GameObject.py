__author__ = 'mosterann'

import pygame

class GameObject(pygame.sprite.Sprite):

    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.dead = False
        self.screen = pygame.display.get_surface()
        # Load image to sprite
        self.image = pygame.image.load(img).convert()
        self.rect = self.image.get_rect()

        # Move a step
        self.step = 20


    def kill(self):
        print("Dead")
        self.dead = True

    def handle_event(self, event):
        pass

    def update(self):
        pass

    def render(self):
        self.screen.blit(self.image, (self.rect))
