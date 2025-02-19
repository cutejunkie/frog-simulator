import pygame
from config import window, window_width, window_height
from random import randint

class Bomb():
    def __init__(self):
        self.image = pygame.image.load("./images/bomb.png")
        self.p_width, self.p_height = self.image.get_size()
        self.x_cord = randint(0, window_width - self.p_width)
        self.y_cord = randint(0, window_height - self.p_height)
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.p_width, self.p_height)

    def tick(self):
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.p_width, self.p_height)

    def draw(self):
        window.blit(self.image, (self.x_cord, self.y_cord))

    