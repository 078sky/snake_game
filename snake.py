import pygame
import config

class Snake:
    def __init__(self):
        self.position = [100, 50]
        self.body = [[100, 50], [90, 50], [80, 50]]
        self.direction = 'RIGHT'
        self.change_to = self.direction

    def change_dir_to(self, dir):
        if dir == 'RIGHT' and not self.direction == 'LEFT':
            self.direction = 'RIGHT'
        if dir == 'LEFT' and not self.direction == 'RIGHT':
            self.direction = 'LEFT'
        if dir == 'UP' and not self.direction == 'DOWN':
            self.direction = 'UP'
        if dir == 'DOWN' and not self.direction == 'UP':
            self.direction = 'DOWN'

    def move(self):
        if self.direction == 'RIGHT':
            self.position[0] += 10
        if self.direction == 'LEFT':
            self.position[0] -= 10
        if self.direction == 'UP':
            self.position[1] -= 10
        if self.direction == 'DOWN':
            self.position[1] += 10
        self.body.insert(0, list(self.position))
        self.body.pop()

    def grow(self):
        self.body.append(self.body[-1])

    def check_collision(self):
        if self.position[0] > config.SCREEN_WIDTH or self.position[0] < 0:
            return True
        if self.position[1] > config.SCREEN_HEIGHT or self.position[1] < 0:
            return True
        for block in self.body[1:]:
            if self.position == block:
                return True
        return False

    def draw(self, surface):
        for pos in self.body:
            pygame.draw.rect(surface, config.GREEN, pygame.Rect(pos[0], pos[1], 10, 10))
