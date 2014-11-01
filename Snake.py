__author__ = 'mosterann'

import pygame
from GameObject import GameObject
from Tail import Tail

class Snake(GameObject):

    def __init__(self):
        super(self.__class__, self).__init__("snake.png")
        self.direction = 1
        self.rect.top = 200
        self.rect.left = 200
        self.moveCounter = 0
        self.moveThreshold = 50
        r = pygame.Rect(240, 200, 40, 40)
        self.tail = Tail(None, False, r)
        self.screenRect = pygame.Rect(0, 0, 640, 480)


    def render(self):
        self.tail.render()
        self.screen.blit(self.image, (self.rect))

    def collision(self, apple):

        rect = self.move()

        #Outside of screen
        if(not rect.colliderect(self.screenRect)):
            self.kill()
        # Collision with tail
        elif(self.tail.collide(rect)):
            self.kill()
        # Collision with apple
        elif(rect.colliderect(apple)):
            apple.spawn(self)
            return True

        return False



    def update(self, apple):
        self.moveCounter += 1
        if(self.moveCounter > self.moveThreshold):

            grow = self.collision(apple)

            oldRect = self.rect.copy()

            if(grow):
                # Create a new tail segment
                tmp = Tail(self.tail, True, oldRect)
                self.tail = tmp
            else:
                self.tail.update(oldRect)

            self.rect = self.move()
            self.moveCounter = 0

    def move(self):
        rect = self.rect
        if(self.direction == 0):
            rect.top -= self.step
        elif(self.direction == 1):
            rect.top += self.step
        elif(self.direction == 2):
            rect.left += self.step
        elif(self.direction == 3):
            rect.left -= self.step

        return rect

    def handle_event(self, event):
        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_DOWN):
                print("Key down")
                self.direction = 1
            if(event.key == pygame.K_UP):
                print("Key up")
                self.direction = 0
            if(event.key == pygame.K_RIGHT):
                print("Key right")
                self.direction = 2
            if(event.key == pygame.K_LEFT):
                print("Key left")
                self.direction = 3

