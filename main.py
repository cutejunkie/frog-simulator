import pygame
from config import window
from Player import Player
from Fly import Fly

def main():
    run = True
    score = 0
    player = Player()
    clock = 0  # sth like stopper
    allflies = []
    background = pygame.image.load("./images/background.png")

    while run:
        clock += pygame.time.Clock().tick(60) / 1000 # max 60 fps /// %1000 to get seconds
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # closing by X
                run = False

        if clock >= 3:
            clock = 0
            allflies.append(Fly())

        player.tick()
        for fly in allflies:
            fly.tick()

        # player ate fly
        for fly in allflies:
            if player.hitbox.colliderect(fly.hitbox):
                allflies.remove(fly)
                score += 1

        # background
        window.blit(background, (0, 0))
        player.draw()
        for fly in allflies:
            fly.draw()

        pygame.display.update()


    print(score)

if __name__ == "__main__":
    main()
