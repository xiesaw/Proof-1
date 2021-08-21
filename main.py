"""
    Authors: Simon Zhang, Alex Xie
    
    Date: Aug 20, 2021
    
    Description: 8-Ball Battle Game!
"""

import pygame
import pySprites

def main():
  
  # Initialize pygame
  pygame.init()

  # Display
  screen = pygame.display.set_mode((640, 480))
  pygame.display.set_caption("8-Ball Battle")

  # Entities
  background = pygame.image.load('background.jpg')
  background = background.convert()
  screen.blit(background, (0, 0))

  # Background music
  player_hit = pygame.mixer.Sound('hit.wav')
  
  # Sound Effects

  # Sprites
  ball = pySprites.Ball(screen)
  allSprites = pygame.sprite.OrderedUpdates(ball)

  # Clock
  clock = pygame.time.Clock()
  keepGoing = True

  # Game loop
  while keepGoing:

    # Time
    clock.tick(30)

    # Event Handling

    # Refresh Screen
    allSprites.clear(screen, background)
    allSprites.update()
    allSprites.draw(screen)

    pygame.display.flip()


main()
