# Gegeven is pikachu die kan springen.

# Voeg de volgende dingen toe:

#   - Zorg dat pikachu niet meerdere keren achter elkaar kan springen (check of pikachu op de grond staat!)
#   - Laat pikachu naar rechts lopen met het rechter pijltje (je moet elke keer opnieuw klikken, hier hebben we het later over!)
#   - Laat pikachu naar links lopen met het linker pijltje
#   - Zorg dat pikachu niet uit het scherm kan lopen


# Slides: https://docs.google.com/presentation/d/1tbN7TAxkqwNQWe_fMOwF1KD4o2V5aJktcSooPF9WZaY/edit?usp=sharing

import pygame, sys
from pygame.locals import QUIT

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Keyboard')
clock = pygame.time.Clock()

background_surface = pygame.Surface((400, 300))
background_surface.fill("white")

pikachu_surface = pygame.image.load("graphics/pikachu.png").convert_alpha()
pikachu_rect = pikachu_surface.get_rect(topleft = (180, 20))

zwaartekracht = 0

while True:
  
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit() 
      
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        zwaartekracht = -20

  screen.blit(background_surface, (0, 0))
 
  zwaartekracht += 1
  pikachu_rect.y += zwaartekracht

  if pikachu_rect.bottom >= 300:
    pikachu_rect.bottom = 300
  
  screen.blit(pikachu_surface, pikachu_rect)

  pygame.display.update()
  clock.tick(60)