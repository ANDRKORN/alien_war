import pygame

class Ship():
    def __init__(self, ai_game):

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        

        self.movie_right = False
        self.movie_left = False
        self.movie_up = False
        self.movie_down = False
        self.speed_ship = ai_game.settings.speed_ship
        
        self.image = pygame.transform.scale( pygame.image.load('image\space-ship.svg'), (50, 60))
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        
        self.x = float(self.rect.x)
        
    def update(self):        
        if self.movie_left and self.x > 0:
            self.x -= self.speed_ship
        if self.movie_right and self.x <= self.screen_rect.width - 50:
            self.x += self.speed_ship
        self.rect.x = self.x
        if self.movie_up:
            self.rect.top -= 1
        if self.movie_down:
            self.rect.bottom +=1
    def bltime(self):
        self.screen.blit(self.image , self.rect)