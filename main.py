import pygame
from config import window, window_width, window_height
from Player import Player
from Fly import Fly

def main():
    run = True
    score = 0
    player = Player()
    clock = 0  # sth like stopper
    allflies = []
    background = pygame.image.load("./images/background.png")
    font = pygame.font.SysFont("arial", 48)

    while run:
        clock += pygame.time.Clock().tick(60) / 1000 # max 60 fps /// %1000 to get seconds
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # closing by X
                run = False

        # every 3 seconds
        if clock >= 3:
            clock = 0
            allflies.append(Fly())

        player.tick()
        for fly in allflies:
            fly.tick()

        # player ate fly
        for fly in allflies[:]:  # iteration in list COPY so not to delete elements while in loop
            if player.hitbox.colliderect(fly.hitbox):
                allflies.remove(fly)
                score += 1

        # SCORE
        score_text = font.render(f"score: {score}", True, (0, 0, 0))
        
        # drawing background
        window.blit(background, (0, 0))
        
        # drawing score
        score_width, score_height = score_text.get_size()  # size of the text
        border = 8
        bottom_margin = 10
        start_x = window_width/2 - score_width/2
        start_y = window_height - score_height - bottom_margin
        pygame.draw.rect(window, (154, 204, 214), (start_x - border/2, start_y, score_width+border, score_height))  # drawing background for text
        window.blit(score_text, (start_x, start_y))

        # drawing player and flies
        player.draw()
        for fly in allflies:
            fly.draw()

        pygame.display.update()


    print(score)

if __name__ == "__main__":
    main()
