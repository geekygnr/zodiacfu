import pygame
import sys
from player import Player
from interactable import InteractableObject
from message import MessageDisplay

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D RPG")

# Player setup
player = Player(WIDTH // 2, HEIGHT // 2)

# Interactable object setup
interactable = InteractableObject(WIDTH // 2 - 100, HEIGHT // 2)

# Message display
font = pygame.font.SysFont(None, 32)
message = MessageDisplay(font, "You found a mysterious object!", WIDTH, HEIGHT)

clock = pygame.time.Clock()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if interactable.collides_with(player.get_rect()):
                    message.toggle()
                else:
                    message.hide()

    keys = pygame.key.get_pressed()
    player.move(keys)

    screen.fill((30, 30, 30))
    interactable.draw(screen)
    player.draw(screen)
    message.draw(screen)
    pygame.display.flip()
    clock.tick(60)
