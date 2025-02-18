import pygame

pygame.init()
window_width, window_height = 800, 600
window = pygame.display.set_mode((window_width, window_height))

x, y = 0, 0  # starting cords
p_width, p_height = 100, 100  # player size
player = pygame.rect.Rect(x, y, p_width, p_height)
# pygame.rect is about making rectangles, to show them on the screen
# pygame.draw.rect is needed

run = True
while run:
    pygame.time.Clock().tick(60)  # max 60 fps
    for event in pygame .event.get():
        if event.type == pygame.QUIT:  # closing by X
            run = False

    keys = pygame.key.get_pressed()

    # arrows clicked
    speed = 3
    if keys[pygame.K_RIGHT]:
        if x + speed < window_width - p_width:
            x += speed
        else:
            x = window_width - p_width

    if keys[pygame.K_LEFT]:
        if x - speed < 0:
            x = 0
        else:
            x -= speed

    if keys[pygame.K_UP]:
        if y - speed < 0:
            y = 0
        else:
            y -= speed

    if keys[pygame.K_DOWN]:
        if y + speed > window_height - p_height:
            y = window_height - p_height
        else:
            y += speed
    
    # refreshing
    player = pygame.rect.Rect(x, y, p_width, p_height)

    # order in drawing is important!
    window.fill((247, 198, 223))
    pygame.draw.rect(window, (94, 32, 64), player)

    pygame.display.update()
