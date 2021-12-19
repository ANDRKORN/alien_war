import sys

import pygame
from GifImage import GIFImage
from setting import Setting 
from ship import Ship
from bullet import Bullet
class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings=Setting()
        self.bg_color=self.settings.bg_color
        self.bg_image= GIFImage('image/out.gif')
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Alien Invasion')

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()                         
            self._update_screen()
            
    def _update_screen(self):
        
        self.screen.fill(self.bg_color)
        self.bg_image.render(self.screen,(0,0))    
        self.ship.bltime()
        self._update_bullets()
        pygame.display.flip()


    def _check_keydown_events(self, event):
        if event.key == pygame.K_q:
                    sys.exit()
        if event.key == pygame.K_SPACE:
            self._fire_bullets()
        if event.key == pygame.K_RIGHT:
            self.ship.movie_right = True
        if event.key == pygame.K_LEFT:
            self.ship.movie_left = True
    
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.movie_right = False
        if event.key == pygame.K_LEFT:
            self.ship.movie_left = False
    
    def _check_events(self):
        for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)            
    
    def _update_bullets(self):
        for bullet in self.bullets:
            bullet.draw_bullet()
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)   
        
    def _fire_bullets(self):
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

if __name__ == "__main__":

    ai=AlienInvasion()
    ai.run_game()