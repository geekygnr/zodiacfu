import pygame

class InteractableObject:
    def __init__(self, x, y, size=40, color=(255, 215, 0)):
        self.size = size
        self.color = color
        self.pos = [x, y]
        self.rect = pygame.Rect(*self.pos, self.size, self.size)
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
    def collides_with(self, other_rect):
        return self.rect.colliderect(other_rect)

