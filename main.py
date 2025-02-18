import pygame
from config import window
from Player import Player

def main():
    run = True
    player = Player()
    while run:
        pygame.time.Clock().tick(60)  # max 60 fps
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # closing by X
                run = False

        player.tick()

        # background
        window.fill((247, 198, 223))
        # player
        player.draw()

        pygame.display.update()

if __name__ == "__main__":
    main()
