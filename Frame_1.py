import pygame
import os
import sprites

# GLOBAL VARIABLES
BLACK = (0, 0, 0)
FPS = 30
WIDTH = 700
HEIGHT = 600
COUNT = 0

# initializing PyGame module and mixer module
pygame.init()
pygame.mixer.init()

# allowing access to the various files
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "Images Files")
music_folder = os.path.join(game_folder, "Music Files")

# creating the screen, which is also a surface
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# entering the while loop
run = True
clock = pygame.time.Clock()

# run the music
music = pygame.mixer.music.load(os.path.join(music_folder,
                                             "bensound-newdawn.wav"))
pygame.mixer.music.play(-1)

# create dragon sprite and a sprite group
dragon1 = sprites.Dragon((WIDTH - 600, HEIGHT - 200))
dragon2 = sprites.Dragon((WIDTH - 100, HEIGHT - 200))
dragon3 = sprites.Dragon((WIDTH - 300, HEIGHT - 150))
dragon_group = pygame.sprite.Group()
dragon_group.add(dragon1, dragon2, dragon3)

# load background image
background = pygame.image.load(os.path.join(img_folder, "resized.png"))

# set font and then create text
font = pygame.font.SysFont("Algerian", 60, False)
text = pygame.font.Font.render(font, "Dragon Knight", True, (255, 0, 0))
font = pygame.font.SysFont("Algerian", 25, False)
text_2 = pygame.font.Font.render(font, "Press enter to start game", True, (255, 255, 255))

while run:
    # screen is the  surface on which to blit the image

    clock.tick(FPS)
    screen.blit(background, (0, 0))
    dragon_group.draw(screen)
    screen.blit(text, (WIDTH/2 - text.get_rect().width/2, text.get_rect().height - 20))
    screen.blit(text_2, (WIDTH/2 - text_2.get_rect().width/2,
                         text.get_rect().height + text_2.get_rect().height + 20))
    pygame.display.update()
    dragon_group.update()
    pygame.display.update()

    # key functionality
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

        if pygame.key.get_pressed()[pygame.K_RETURN]:
            # call frame 2
            count = 1
            music = pygame.mixer.music.load(os.path.join(music_folder,
                                             "bensound-birthofahero.mp3"))
            pygame.mixer.music.play(-1)
            os.system('Frame_2.py')
            count = 0