import pygame

class Ship():
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        
        self.movie_right = False
        self.movie_left = False
        
        self.image = pygame.transform.scale( pygame.image.load('image\space-ship.svg'), (50, 60))
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom
    def update(self):
        
        if self.movie_left and self.rect.x > 0:
            self.rect.x -= 1
        if self.movie_right and self.rect.x <= self.screen_rect.width - 50:
            print(self.screen_rect.width, self.rect.x)
            self.rect.x += 1

    def bltime(self):
        self.screen.blit(self.image , self.rect)