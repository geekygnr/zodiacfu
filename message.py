import pygame

class MessageDisplay:
    def __init__(self, font, width, height):
        self.font = font
        self.text = "--EMPTY--"
        self.width = width
        self.height = height
        self.visible = False
    def show(self):
        self.visible = True
    def hide(self):
        self.visible = False
    def toggle(self):
        self.visible = not self.visible
    def set(self, text):
        self.text = text
    def draw(self, surface):
        if self.visible:
            msg_surface = self.font.render(self.text, True, (255, 255, 255))
            surface.blit(msg_surface, (self.width // 2 - msg_surface.get_width() // 2, self.height - 60))

