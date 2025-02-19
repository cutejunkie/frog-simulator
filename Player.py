import pygame
from config import window, window_width, window_height

class Player:
    def __init__(self):
        self.speed = 50
        self.x_cord = 0
        self.y_cord = 0
        
        self.images = {
            "down": pygame.image.load("./images/player_front.png"),
            "up": pygame.image.load("./images/player_back.png"),
            "left": pygame.image.load("./images/player_left.png"),
            "right": pygame.image.load("./images/player_right.png"),
        }
        
        # default look
        self.image = self.images["down"]
        self.p_width, self.p_height = self.image.get_size()
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.p_width, self.p_height)


    # once per every while loop
    def tick(self):
        keys = pygame.key.get_pressed()  # keys clicked
        moved = False  # flag to check if player moved
        

        # arrows clicked /// WSAD clicked
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if self.x_cord + self.speed < window_width - self.p_width:
                self.x_cord += self.speed
            else:
                self.x_cord = window_width - self.p_width
            self.image = self.images["right"]
            moved = True

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if self.x_cord - self.speed < 0:
                self.x_cord = 0
            else:
                self.x_cord -= self.speed
            self.image = self.images["left"]
            moved = True

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            if self.y_cord - self.speed < 0:
                self.y_cord = 0
            else:
                self.y_cord -= self.speed
            self.image = self.images["up"]
            moved = True

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            if self.y_cord + self.speed > window_height - self.p_height:
                self.y_cord = window_height - self.p_height
            else:
                self.y_cord += self.speed
            self.image = self.images["down"]
            moved = True

        # refreshing hitbox
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.p_width, self.p_height)


    # showing player in window
    def draw(self):
        window.blit(self.image, (self.x_cord, self.y_cord))
