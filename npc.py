import pygame
from interactable import Interactable

class Npc(Interactable):
    def __init__(self, x, y, size=40, color=(255, 128, 0), speed=5):
        super().__init__(x, y, size, color)
        self.speed = speed
        self.bound = [20,50]
        self.relative = [0,0]
        self.direction = [0,1]
        self.timer = 0
        self.step = 2
    def move(self):
        if self.timer < self.step:
            self.timer += 1
            return
        self.timer = 0
        self.pos[0] += self.direction[0] * self.speed
        self.pos[1] += self.direction[1] * self.speed
        self.relative[0] += 1 * self.direction[0]
        self.relative[1] += 1 * self.direction[1]
        self.__adjust_direction()
        self.update_rect()
    def __adjust_direction(self):
        if self.relative[0] <= 0 and self.relative[1] <= 0:
            self.direction[0] = 0
            self.direction[1] = 1
            return
        if self.relative[0] <= 0 and self.relative[1] >= self.bound[1]:
            self.direction[0] = 1
            self.direction[1] = 0
            return
        if self.relative[0] >= self.bound[0] and self.relative[1] >= self.bound[1]:
            self.direction[0] = 0
            self.direction[1] = -1
            return
        if self.relative[0] >= self.bound[0] and self.relative[1] <= 0:
            self.direction[0] = -1
            self.direction[1] = 0
            return


