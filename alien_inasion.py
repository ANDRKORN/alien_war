import sys

import pygame
from GifImage import GIFImage
from setting import Setting 
from ship import Ship

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings=Setting()
        self.bg_color=self.settings.bg_color
        self.bg_image= GIFImage('image/out.gif')
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Alien Invasion')

        self.ship = Ship(self)

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()               
            self._update_screen()

    def _update_screen(self):
        
        self.screen.fill(self.bg_color)
        self.bg_image.render(self.screen,(0,0))    
        self.ship.bltime()
        pygame.display.flip()

    def _check_keydown_events(self, event):
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
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)            
                    
if __name__ == "__main__":

    ai=AlienInvasion()
    ai.run_game()