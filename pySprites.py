"""
    Author: Simon Zhang, Alex

    Date: Aug 20, 2021
    
    Description: Sprites for 8-Ball Battle Game!
"""

import pygame

class Ball(pygame.sprite.Sprite):
  '''This class defines the sprite for the Ball.'''
  
  def __init__(self, screen):
    pygame.sprite.Sprite.__init__(self)

    # Image and rect attributes
    self.image = pygame.image.load("hockey-disc.png")
    self.image.fill((0, 0, 0))
    self.image.set_colorkey((0,0,0))
    pygame.draw.circle(self.image, (255, 0, 0), (10, 10), 10, 0)
    self.rect = self.image.get_rect()
    self.rect.center = (screen.get_width()/2,screen.get_height()/2)

    self.window = screen