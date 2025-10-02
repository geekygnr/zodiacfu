import pygame
import sys
from player import Player
from npc import Npc
from interactable import Interactable
from message import MessageDisplay

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D RPG")

# Player setup
player = Player(WIDTH // 2, HEIGHT // 2)

# NPC setup
npc = Npc(WIDTH // 2 + 150, HEIGHT // 2 - 150)

# Interactable object setup
interactable = Interactable(WIDTH // 2 - 100, HEIGHT // 2)

# Message display
font = pygame.font.SysFont(None, 32)
message = MessageDisplay(font, "You found a mysterious object!", WIDTH, HEIGHT)

clock = pygame.time.Clock()

# Main game loop
while True:
    npc.set_color((255, 128, 0))  # Reset color after hit

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if interactable.collides_with(player.get_rect()):
                    message.set("You found a mysterious object!")
                    message.show()
                else:
                    message.hide()
            if event.key == pygame.K_RETURN:
                if npc.collides_with(player.attack()):
                    message.set("Hit!")
                    npc.set_color((255, 255, 255))
                    message.show()
                else:
                    message.set("Miss!")
                    message.show()

    keys = pygame.key.get_pressed()
    player.move(keys)
    npc.move()
    if npc.collides_with(player.get_rect()):
        message.set("Hello, traveler!")
        message.show()

    screen.fill((30, 30, 30))
    interactable.draw(screen)
    npc.draw(screen)
    player.draw(screen)
    message.draw(screen)
    pygame.display.flip()
    clock.tick(60)
