import pygame
from interactable import Interactable

class Player(Interactable):
    def __init__(self, x, y, size=40, color=(0, 128, 255), speed=5):
        super().__init__(x, y, size, color)
        self.speed = speed
        self.attacking = False
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
    def attack(self):
        self.attacking = not self.attacking
        return self.__attack_rect()
    def __attack_rect(self):
        pos = [self.pos[0] - self.size // 2, self.pos[1] - self.size // 2]
        return pygame.Rect(*pos, self.size * 2, self.size * 2)
    def draw(self, surface):
        if self.attacking:
            pygame.draw.rect(surface, (255, 0, 0), self.__attack_rect())
            self.attacking = False
        super().draw(surface)