import random
import pygame
import os
import sprites
import digital_display

# GLOBAL VARIABLES
WIDTH = 900
HEIGHT = 700
IMAGE_FOLDER = os.path.join(os.path.dirname(__file__), "Images Files")
FPS = 30
change_x = 0
change_y = 0
FONT = pygame.font.SysFont("Algerian", 40, False)
GAME_OVER_TEXT = pygame.font.Font.render(FONT, "GAME OVER | PRESS Enter FOR MAIN", True, (0, 0, 0))
EX_KNIGHT_SPACE = 10
EX_ROCK_SPACE = 200



run = True

# Setting up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# adding dragon player to sprite group
dragon_player = sprites.GameDragon()
player_group = pygame.sprite.Group()
player_group.add(dragon_player)

# establishing coordinates for the knights to occur in
seq1 = 0, dragon_player.rect.left - EX_KNIGHT_SPACE
seq2 = dragon_player.rect.right + EX_KNIGHT_SPACE, WIDTH 

seq3 = 0, dragon_player.rect.top - EX_KNIGHT_SPACE
seq4 = dragon_player.rect.bottom + EX_KNIGHT_SPACE, HEIGHT 

# establishing coordinates for the stones to occur in
# prevents dragon from being surrounded by rocks 
seq1 = 0, dragon_player.rect.left - EX_ROCK_SPACE
seq2 = dragon_player.rect.right + EX_ROCK_SPACE, WIDTH 

seq3 = 0, dragon_player.rect.top - EX_ROCK_SPACE
seq4 = dragon_player.rect.bottom + EX_ROCK_SPACE, HEIGHT 


# creating stone sprites
# stone_rect = []
stone_group = pygame.sprite.Group()
for stone in range(7):
    choice = random.choice([seq1, seq2])
    choice1 = random.choice([seq3, seq4])

    s = sprites.Stone((random.randint(choice[0] + 20, choice[1] - 20), 
                       random.randint(choice1[0] + 20, choice1[1] - 20)))
    stone_group.add(s)
    # stone_rect.append(s.rect)
# note that stones can stack on each other or be in the same quadrant 

# setting up background images for scrolling background
background_forth = sprites.Background(0, 0)
background_back = sprites.Background(-WIDTH, 0)

# setting up the knights
knight_group = pygame.sprite.Group()
for knight in range(10):
    
    choice = random.choice([seq1, seq2])
    choice1 = random.choice([seq3, seq4])

    k = sprites.DragonKnight(random.randint(choice[0], choice[1]),
                             random.randint(choice1[0], choice1[1]))
    knight_group.add(k)

# creating a background sprite
background = pygame.sprite.Group()
background.add(background_forth, background_back)

# establishing the bullet group
fireball_group = pygame.sprite.Group()


# setting the clock
clock = pygame.time.Clock()

# creating score board
score_number = 0
score = digital_display.Score(0, WIDTH)
score_group = pygame.sprite.GroupSingle()
score_group.add(score)
while run:

    clock.tick(FPS)
    background.draw(screen)
    stone_group.draw(screen)
    knight_group.draw(screen)
    player_group.draw(screen)
    fireball_group.draw(screen)
    score_group.draw(screen)
    pygame.display.flip()
    background.update()
    pygame.display.flip()



    if background_back.rect.x == 0:
        background_back.rect.x = -WIDTH

    if background_forth.rect.x == WIDTH:
        background_forth.rect.x = 0

    fireball_group.update()

    for ball in fireball_group.sprites():
        if ball.x > WIDTH or ball.x < 0 or ball.y > HEIGHT or ball.y < 0:
            fireball_group.remove(sprites)

        for knight in knight_group.sprites():

            if knight.rect.colliderect(ball):
                choice = random.choice([seq1, seq2])
                choice1 = random.choice([seq3, seq4])
                knight_group.remove(knight)
                new_knight = \
                    (sprites.DragonKnight
                     (random.randint(choice[0] - 20, choice[1] - 20),
                      random.randint(choice1[0] - 20, choice1[1] - 20)))
                knight_group.add(new_knight)
                score_group.update(1)
    for knight in knight_group:

        if pygame.sprite.collide_mask(dragon_player, knight):
        # if dragon_player.rect.colliderect(knight.rect): #ollided=pygame.sprite.collide_rect_ratio(.75)
            player_group.remove(dragon_player)
           
            while True:
                screen.blit(GAME_OVER_TEXT, (WIDTH/2 - GAME_OVER_TEXT.get_rect().width/2, HEIGHT/2))
                pygame.display.update()


                for event in pygame.event.get():
                    if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_RETURN]:
                        quit()


    knight_group.update()

    # iterate through each possible event in the queue
    for event in pygame.event.get():

        # set up quit window command
        if event.type == pygame.QUIT:
            quit()

        # if the event type, is a key_down event, only then goes through all
        # the if statements
        if event.type == pygame.KEYDOWN:

            # if a particular key gets pressed, then move in that direction via
            # the update changing the rect attributes
            # now we want to keep moving in that direction

            if event.key == pygame.K_a:
                change_y = 0
                change_x = -20

            if event.key == pygame.K_d:
                change_y = 0
                change_x = 20

            if event.key == pygame.K_w:
                change_x = 0
                change_y = -20

            if event.key == pygame.K_s:
                change_x = 0
                change_y = 20

        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            vec = pygame.math.Vector2(mx-dragon_player.x, my-dragon_player.y)
            unit_vec = pygame.math.Vector2.normalize(vec)
            fireball = sprites.Fireball(dragon_player.x, dragon_player.y,
                                        unit_vec.x*20, unit_vec.y*20)
            fireball_group.add(fireball)

    for stone in stone_group:
        if pygame.sprite.collide_mask(dragon_player, stone):
            while True:
                screen.blit(GAME_OVER_TEXT, (WIDTH/2 - GAME_OVER_TEXT.get_rect().width/2, HEIGHT/2))
                pygame.display.update()
            
                for event in pygame.event.get():
                    if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_RETURN]:
                        quit()
        
    dragon_player.update(change_x, change_y)


    # knights on the corners - left and right 