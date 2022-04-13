import pygame
import os

WIDTH = 900
HEIGHT = 700
BLACK = (0, 0, 0)
IMAGE_FOLDER = os.path.join(os.path.join(os.path.dirname(__file__),
                                         "Images Files"))
WIDTHDIFF = 20


class Dragon(pygame.sprite.Sprite):
    """Inherits from the inbuilt Sprite class
    """

    def __init__(self, center: tuple) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = \
            pygame.image.load(os.path.join(IMAGE_FOLDER,
                                           "individual_dragon.png"))
        self.rect = self.image.get_rect()
        self.rect.center = center

    def update(self) -> None:
        self.rect.x -= 1
        if self.rect.right < 0:
            self.rect.x = WIDTH


class Stone(pygame.sprite.Sprite):
    """class for stone sprite"""

    def __init__(self, center: tuple) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = \
            pygame.image.load(os.path.join(IMAGE_FOLDER,
                                           "rock.png")) # self.image in sprite class
        # needs a surface, and surface has a get_rect function
        self.rect = self.image.get_rect()  # a rect is not a surface, but get
        # _rect allows us to access the rectangular properties
        self.rect.center = center  # for that particular reason you can play
        # around with the center coordinates
        # center gives position of rect, which then is used to place the
        # rectangle by the draw method

        # self.image =
        # pygame.image.load(pygame.image.load(os.path.join(IMAGE_FOLDER,
        #                                                  "stone.png")))
        # self.rect = self.image.get_rect()
        # self.image.get_rect().center = center
        self.mask = pygame.mask.from_surface(self.image)


class GameDragon(pygame.sprite.Sprite):
    """Represents the player dragon class"""

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        # x and y values are assigned
        self.image = pygame.image.load(os.path.join(IMAGE_FOLDER,
                                                    "mini_individual_dragon.png"))
        self.x = WIDTH / 2
        self.y = HEIGHT / 2
        # self.image = \
        #     pygame.image.load(os.path.join(IMAGE_FOLDER,
        #                                    "individual_dragon.png"))
        self.rect = self.image.get_rect()

        # assign the center relative to the self.x and self.y
        self.rect.center = self.x, self.y
        self.mask = pygame.mask.from_surface(self.image)

        # changing the center reassigns all the attributes
        # Note changing the attributes in functions, below changes the initial
        # attributes because the reference of that variable is now at a
        # different pointer

    def update(self, dx: int, dy: int) -> None:
        """update the sprite's position"""

        if self.rect.right + dx >= WIDTH:
            self.x = WIDTH - self.rect.width / 2

        elif self.rect.left + dx <= 0:
            self.x = self.rect.width / 2

        else:
            self.x = self.x + dx

        if self.rect.bottom + dy >= HEIGHT:
            self.y = HEIGHT - self.rect.width / 2 + WIDTHDIFF
        elif self.rect.top + dy <= 0:
            self.y = self.rect.height / 2

        else:
            self.y = self.y + dy

        self.rect.center = self.x, self.y


class Fireball(pygame.sprite.Sprite):
    """A fireball sprite"""

    def __init__(self, x: int, y: int, dx: int, dy: int):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = self.x, self.y
        self.dx = dx
        self.dy = dy
        self.image = pygame.image.load(os.path.join(IMAGE_FOLDER,
                                                    "fireball.png"))

    def update(self):
        self.x += self.dx
        self.y += self.dy
        self.rect.center = self.x, self.y

class DragonKnight(pygame.sprite.Sprite):
    """Creates knight sprite objects"""

    def __init__(self, x: int, y: int):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(IMAGE_FOLDER,
                                                    "ship.png"))
        self.rect = self.image.get_rect()
        # positions x and y of the rect, thereby repositioning the rect
        self.x = x
        self.y = y
        self.rect.center = self.x, self.y
        self.change_x = 3
        self.change_y = 3
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        """updates the knight position"""

        if self.x + self.change_x <= self.rect.width / 2:
            self.x = self.rect.width / 2
            self.change_x = -self.change_x

        elif self.x + self.change_x >= WIDTH - self.rect.width / 2:
            self.x = WIDTH - self.rect.width / 2
            self.change_x = -self.change_x

        else:
            self.x += self.change_x

        if self.y + self.change_y < self.rect.height / 2:
            self.y = self.rect.height / 2
            self.change_y = -self.change_y

        elif self.y + self.change_y > HEIGHT - self.rect.height / 2:
            self.y = HEIGHT - self.rect.height / 2
            self.change_y = -self.change_y

        else:
            self.y += self.change_y

        self.rect.center = self.x, self.y


class Background(pygame.sprite.Sprite):
    """initialize the background"""

    def __init__(self, x: int, y: int):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(IMAGE_FOLDER,
                                                    "background_final.png"))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # center the rectangle, which then centers the image

    def update(self):
        """ scroll the screen forward """

        self.rect.x += 1


# dragon to rock collsion 
# dragon to knight collision
