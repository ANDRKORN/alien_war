import pygame

class Ship():
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.transform.scale( pygame.image.load('image\space-ship.svg'), (50, 60))
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

    def bltime(self):

        self.screen.blit(self.image , self.rect)