__author__ = 'mosterann'


from GameObject import GameObject
from random import randint


class Apple(GameObject):

    def __init__(self):
        super(self.__class__, self).__init__("apple.png")

        # Init position
        self.rect.top = 80;
        self.rect.left = 80;

    def spawn(self, snake):
        print("SPAWNING")
        x = randint(40, 440)
        y = randint(40, 600)
        self.rect.top = y
        self.rect.left = x

