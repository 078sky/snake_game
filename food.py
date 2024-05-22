import pygame
import random
import config

class Food:
    def __init__(self):
        self.position = [random.randrange(1, config.SCREEN_WIDTH//10) * 10,
                         random.randrange(1, config.SCREEN_HEIGHT//10) * 10]
        self.is_food_on_screen = True

    def spawn_food(self):
        if not self.is_food_on_screen:
            self.position = [random.randrange(1, config.SCREEN_WIDTH//10) * 10,
                             random.randrange(1, config.SCREEN_HEIGHT//10) * 10]
            self.is_food_on_screen = True
        return self.position

    def set_food_on_screen(self, b):
        self.is_food_on_screen = b

    def draw(self, surface):
        pygame.draw.rect(surface, config.RED, pygame.Rect(self.position[0], self.position[1], 10, 10))
