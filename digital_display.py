import pygame
pygame.init()

class Score(pygame.sprite.Sprite):

    def __init__(self, score: int, width: int):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.SysFont("Arial", 30, True, False)
        self.image = pygame.font.Font.render(self.font, str(score), True, (255, 255, 255),
                                      (0, 0, 0))
        self.rect = self.image.get_rect()
        self.x = width/2
        self.y = 0
        self.rect.topright = self.x, self.y
        self.score = score

    def update(self, new_score):
        """change the score of the game"""
        self.score += 1
    
        self.image = pygame.font.Font.render(self.font, str(self.score), True, (255, 255, 255),
                                      (0, 0, 0))


