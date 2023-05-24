import pygame

pygame.init()

size = [400,600]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("TestGame")
clock = pygame.time.Clock()

background = pygame.image.load("background.png")
character = pygame.image.load("Character.png")

character_x = 150
character_y = 300

character_speed = 4
is_jumping = False
jump_count = 10

sb = True

while sb:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sb = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        character_x -= character_speed
    elif keys[pygame.K_RIGHT]:
        character_x += character_speed
    if keys[pygame.K_UP]:
        character_y -= character_speed
    elif keys[pygame.K_DOWN]:
        character_y += character_speed
    if keys[pygame.K_SPACE] and not is_jumping:
        is_jumping = True
        jump_count = 10

    if is_jumping:
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            character_y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else:
            is_jumping = False

    if character_x + 65 < 0 or character_x > size[0] - 65 or character_y + 70 < 0 or character_y > size[1] - 70:
        sb = False
    
    screen.blit(background,(0,0))
    screen.blit(character,(character_x,character_y))

    pygame.display.update()

pygame.display.quit()
pygame.quit()
    
