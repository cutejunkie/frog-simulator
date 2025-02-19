import pygame
from config import window, window_width, window_height
from Player import Player
from Fly import Fly
from Bomb import Bomb

def main():
    run = True

    player = Player()
    allflies = []
    allbombs = []

    score = 0
    clock_fly = 0  # sth like stopper
    clock_dis_fly = -3  # for dissapearing of flies + delay
    clock_bomb = 0  # appearance of bomb
    clock_dis_bomb = -5  # disappearance of said bomb
    
    background = pygame.image.load("./images/background.png")
    font = pygame.font.SysFont("arial", 48)
    game_clock = pygame.time.Clock()

    while run:
        delta_time = game_clock.tick(60) / 1000  # max 60 fps /// %1000 to get seconds

        clock_fly += delta_time 
        clock_dis_fly += delta_time
        clock_bomb += delta_time 
        clock_dis_bomb += delta_time
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # closing by X
                run = False

        # every 3s
        if clock_fly >= 3:
            clock_fly = 0
            allflies.append(Fly())

        # every 3s
        if clock_dis_fly >= 3:
            if allflies:
                allflies.pop(0)  # deleting the longest existing fly
            clock_dis_fly = 0  # clock reset

        # every 5s
        if clock_bomb >= 5:
            clock_bomb = 0
            allbombs.append(Bomb())

        # every 5s
        if clock_dis_bomb >= 5:
            if allbombs:
                allbombs.pop(0)
            clock_dis_bomb = 0

        player.tick()
        for fly in allflies:
            fly.tick()
        for bomb in allbombs:
            bomb.tick()

        # player ate fly
        for fly in allflies[:]:  # iteration in list COPY so not to delete elements while in loop
            if player.hitbox.colliderect(fly.hitbox):
                allflies.remove(fly)
                score += 1

        # player ate the bomb
        for bomb in allbombs[:]:
            if player.hitbox.colliderect(bomb.hitbox):
                allbombs.remove(bomb)
                score = 0

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

        # drawing player and flies and bombs
        player.draw()
        for fly in allflies:
            fly.draw()
        for bomb in allbombs:
            bomb.draw()

        pygame.display.update()


    print(score)

if __name__ == "__main__":
    main()
