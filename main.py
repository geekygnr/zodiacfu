import pygame
import sys
from player import Player
from interactable import InteractableObject

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
show_message = False
message_text = "You found a mysterious object!"

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
                    show_message = not show_message
                else:
                    show_message = False

    keys = pygame.key.get_pressed()
    player.move(keys)

    screen.fill((30, 30, 30))
    # Draw interactable object
    interactable.draw(screen)
    # Draw player
    player.draw(screen)
    # Show message if interacted
    if show_message:
        msg_surface = font.render(message_text, True, (255, 255, 255))
        screen.blit(msg_surface, (WIDTH // 2 - msg_surface.get_width() // 2, HEIGHT - 60))
    pygame.display.flip()
    clock.tick(60)
