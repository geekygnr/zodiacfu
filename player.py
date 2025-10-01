import pygame

class Player:
    def __init__(self, x, y, size=40, color=(0, 128, 255), speed=5):
        self.size = size
        self.color = color
        self.speed = speed
        self.pos = [x, y]
    def get_rect(self):
        return pygame.Rect(*self.pos, self.size, self.size)
    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.pos[0] -= self.speed
        if keys[pygame.K_RIGHT]:
            self.pos[0] += self.speed
        if keys[pygame.K_UP]:
            self.pos[1] -= self.speed
        if keys[pygame.K_DOWN]:
            self.pos[1] += self.speed
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (*self.pos, self.size, self.size))

