import pygame
import random
import config

class Obstacle:
    def __init__(self):
        self.position = [random.randrange(1, config.SCREEN_WIDTH//10) * 10,
                         random.randrange(1, config.SCREEN_HEIGHT//10) * 10]

    def spawn_obstacle(self):
        self.position = [random.randrange(1, config.SCREEN_WIDTH//10) * 10,
                         random.randrange(1, config.SCREEN_HEIGHT//10) * 10]
        return self.position

    def draw(self, surface):
        pygame.draw.rect(surface, config.BLACK, pygame.Rect(self.position[0], self.position[1], 10, 10))
