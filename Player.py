import pygame
from config import window, window_width, window_height

class Player:
    def __init__(self):
        self.x_cord = 0
        self.y_cord = 0
        self.p_width = 0
        self.p_height = 0
        self.image = pygame.image.load("./images/player.png")

    # once per every while loop
    def tick(self):
        self.p_width, self.p_height = self.image.get_size()

        # keys clicked
        keys = pygame.key.get_pressed()

        speed = 3

        # arrows clicked /// WSAD clicked
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if self.x_cord + speed < window_width - self.p_width:
                self.x_cord += speed
            else:
                self.x_cord = window_width - self.p_width

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if self.x_cord - speed < 0:
                self.x_cord = 0
            else:
                self.x_cord -= speed

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            if self.y_cord - speed < 0:
                self.y_cord = 0
            else:
                self.y_cord -= speed

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            if self.y_cord + speed > window_height - self.p_height:
                self.y_cord = window_height - self.p_height
            else:
                self.y_cord += speed

    # showing player in window
    def draw(self):
        window.blit(self.image, (self.x_cord, self.y_cord))
