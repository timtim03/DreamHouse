
import pygame

#let's have a clock in our project so the player can move
clock = pygame.time.Clock()

pygame.init()
#initial dimentions of the window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("DreamHouse")

#let's have a background for our program and seize it to our screen dimentions
back = pygame.image.load('images.house/back.png')
back = pygame.transform.scale(back, (800, 600))
back_x = 0

#let's have a background sound
back_sound = pygame.mixer.Sound('images.house/silent-wood.mp3')
back_sound.play()

#let's have a player in our project using png's from the folders
walk_left = [
    pygame.image.load('images.house/player_left/player_left1.png'),
    pygame.image.load('images.house/player_left/player_left2.png'),
    pygame.image.load('images.house/player_left/player_left3.png'),
    pygame.image.load('images.house/player_left/player_left4.png'),
]
walk_right = [
    pygame.image.load('images.house/player_right/player_right1.png'),
    pygame.image.load('images.house/player_right/player_right2.png'),
    pygame.image.load('images.house/player_right/player_right3.png'),
    pygame.image.load('images.house/player_right/player_right4.png'),
]
walk_up = [
    pygame.image.load('images.house/player_back/player_back1.png'),
    pygame.image.load('images.house/player_back/player_back2.png'),
    pygame.image.load('images.house/player_back/player_back3.png'),
    pygame.image.load('images.house/player_back/player_back4.png'),
]
walk_down = [
    pygame.image.load('images.house/player_front/player_front1.png'),
    pygame.image.load('images.house/player_front/player_front2.png'),
    pygame.image.load('images.house/player_front/player_front3.png'),
    pygame.image.load('images.house/player_front/player_front4.png'),
]
standing_still = [
    pygame.image.load('images.house/player_still/player_still.png'),
    pygame.image.load('images.house/player_still/player_still.png'),
    pygame.image.load('images.house/player_still/player_still.png'),
    pygame.image.load('images.house/player_still/player_still.png'),
]

player_anim_count = 0  #we need it for player animation
player_x = 470  #player's x position
player_y = 470 #player's y position
player_speed = 10 #player's velocity

#let's have dimensions of a house
house = pygame.Surface((220, 280))
house.fill((166, 97, 73))


#let's have a condition here so when the window appears it does not close and we can quit it properly
running = True
while running:

    #print the background
    screen.blit(back, (back_x, 0))
    screen.blit(back, (back_x + 800, 0))

    #infinitely moving background
    back_x-=1
    if back_x == -800:
        back_x = 0


    #let's draw a house with a roof
    screen.blit(house, (120, 270))
    pygame.draw.rect(screen, (74, 40, 28), (270, 150, 40, 90))
    pygame.draw.polygon(screen, (223, 230, 224), ((275, 150), (300, 100), (320, 70),(385, 50), (450, 60), (380, 120), (305, 150)))
    pygame.draw.polygon(screen, (74, 40, 28), ((120,270), (230, 130), (340, 270)))
    pygame.draw.line(house, (10, 10, 10), [0, 140], [220, 140], 2)
    #door
    pygame.draw.rect(house, (189, 162, 104), (146.6, 175, 36.6, 105))
    #door window
    pygame.draw.rect(house, (170, 235, 240), (155.75, 185, 18.3, 35))
    pygame.draw.rect(house, (10, 10, 10), (155.75, 185, 18.3, 35), 2)
    pygame.draw.line(house, (10, 10, 10), [155.75, 201.5], [172.5, 201.5], 2)
    pygame.draw.line(house, (10, 10, 10), [163, 185], [163, 220], 2)
    #window 1st floor
    pygame.draw.rect(house, (170, 235, 240), (20, 165, 90, 80))
    pygame.draw.rect(house, (10, 10, 10), (20, 165, 90, 80), 2)
    pygame.draw.line(house, (10, 10, 10,), [20, 205], [110, 205], 2)
    pygame.draw.line(house, (10, 10, 10,), [65, 165], [65, 245], 2)
    #window left 2nd floor
    pygame.draw.rect(house, (158, 163, 230), (20, 25, 90, 80))
    pygame.draw.rect(house, (10, 10, 10), (20, 25, 90, 80), 2)
    pygame.draw.line(house, (10, 10, 10,), [20, 65], [110, 65], 2)
    pygame.draw.line(house, (10, 10, 10,), [65, 25], [65, 105], 2)
    #window right 2nd floor
    pygame.draw.circle(house, (158, 163, 230), (165, 65), 40)
    pygame.draw.circle(house, (10, 10, 10), (165, 65), 40, 2)
    pygame.draw.line(house, (10, 10, 10,), [165, 25], [165, 105], 2)
    pygame.draw.line(house, (10, 10, 10,), [125, 65], [205, 65], 2)

    #butterfly
    #draw the wings of butterfly
    pygame.draw.polygon(screen, (173, 66, 129), ((600, 250), (650, 300), (700, 250), (700, 300), (650, 310), (700, 320), (700, 370), (650, 320), (600, 370), (600, 320), (650, 310), (600, 300), (600, 250)))
    pygame.draw.polygon(screen, (10, 10, 10), ((600, 250), (650, 300), (700, 250), (700, 300), (650, 310), (700, 320), (700, 370), (650, 320), (600, 370), (600, 320), (650, 310), (600, 300), (600, 250)), 2)
    #draw the body of butterfly
    pygame.draw.ellipse(screen, (53, 59, 143), (638, 280, 25, 70))
    pygame.draw.ellipse(screen, (10, 10, 10), (638, 280, 25, 70), 2)
    #draw antennae
    pygame.draw.line(screen, (10, 10, 10), (638, 265), (650, 280), 2)
    pygame.draw.line(screen, (10, 10, 10), (663, 265), (650, 280), 2)


    #condition when keys are pressed so the animation moves right, left, up or down
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        screen.blit(walk_left[player_anim_count], (player_x,player_y))
    elif keys[pygame.K_RIGHT]:
        screen.blit(walk_right[player_anim_count], (player_x, player_y))
    elif keys[pygame.K_UP]:
        screen.blit(walk_up[player_anim_count], (player_x, player_y))
    elif keys[pygame.K_DOWN]:
        screen.blit(walk_down[player_anim_count], (player_x, player_y))
    else:
        screen.blit(standing_still[player_anim_count], (player_x, player_y))


    #boundaries of the animation movement for x and y axis
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 20:
        player_x -= player_speed
    elif keys[pygame.K_RIGHT] and player_x < 730:
        player_x += player_speed
    elif keys[pygame.K_UP] and player_y > 400:
        player_y -= player_speed
    elif keys[pygame.K_DOWN] and player_y < 520:
        player_y += player_speed

    #we need it in order to change the player's animation
    if player_anim_count == 3:
        player_anim_count = 0
    else:
        player_anim_count += 1


    # update the screen and pause
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    clock.tick(10)