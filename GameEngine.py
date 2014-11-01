__author__ = 'mosterann'

import pygame

from Snake import Snake
from Apple import Apple
from GameObject import GameObject

# Stupid Pycharm wont recognize .py file
class GameEngine:

    def __init__(self):
        print("Game engine")
        pygame.init()
        self.screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("Snake challenge")

        # Fill background with black
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((0, 0, 0))

        self.running = True
        self.apple = Apple()
        self.snake = Snake()


    # Starting point of the game
    def start(self):

        clock = pygame.time.Clock()
        # Simplefied Game loop
        while self.running:
            clock.tick(50)
            self.handle_events()
            self.update()
            self.render()


    # Call rendering for all game objects
    def render(self):
        # Clear the screen
        self.screen.blit(self.background, (0, 0))
        # Render objects
        self.apple.render()
        self.snake.render()

        # Update screen
        pygame.display.flip()

    # Call updates on all game objects
    def update(self):
        self.apple.update()
        self.snake.update(self.apple)


    # Handle events such as key presses or exits
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            else:
                self.snake.handle_event(event)


