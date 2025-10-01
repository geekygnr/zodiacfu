import pygame
from interactable import Interactable

class Player(Interactable):
    def __init__(self, x, y, size=40, color=(0, 128, 255), speed=5):
        super().__init__(x, y, size, color)
        self.speed = speed
    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.pos[0] -= self.speed
        if keys[pygame.K_RIGHT]:
            self.pos[0] += self.speed
        if keys[pygame.K_UP]:
            self.pos[1] -= self.speed
        if keys[pygame.K_DOWN]:
            self.pos[1] += self.speed
        self.update_rect()
