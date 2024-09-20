# Gegeven is Pikachu die nu wel normaal kan lopen als je de pijltjes ingedrukt houdt!

# Gegeven is een variabele game_actief, deze is True, doe het volgende:

#   - Als game_actief True is moet alle code van de game werken, zet deze code dus in een if
#   - Als pikachu collide met de tekst "Dood!" maak game_actief dan False
#   - Als game_actief False is, maak het scherm dan zwart en zet pikachu weer in het midden van het scherm
#   - Als de speler dan op spatie drukt, start het spel dan opnieuw (game_actief = True)

# Slides: https://docs.google.com/presentation/d/1fzbS39wrbh226ts72wHhQzyjpxuYxhqV9pEE8XcwTPM/edit?usp=sharing

import pygame, sys
from pygame.locals import QUIT

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Keyboard en zwaartekracht')
font = pygame.font.Font(None, 50)
clock = pygame.time.Clock()

background_surface = pygame.Surface((400, 300))
background_surface.fill("white")

enemy_surface = font.render("Dood!", False, "red")
enemy_rect = enemy_surface.get_rect(center= (300, 200))

pikachu_surface = pygame.image.load("graphics/pikachu.png").convert_alpha()
pikachu_rect = pikachu_surface.get_rect(topleft = (180, 20))

zwaartekracht = 0
game_actief = True

while True:
  
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit() 
      
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE and pikachu_rect.bottom >= 300:
        zwaartekracht = -20

  screen.blit(background_surface, (0, 0))
  screen.blit(enemy_surface, enemy_rect)

  zwaartekracht += 1
  pikachu_rect.y += zwaartekracht

  if pikachu_rect.bottom >= 300:
    pikachu_rect.bottom = 300

  keys = pygame.key.get_pressed()
  if keys[pygame.K_RIGHT] and pikachu_rect.right + 6 <= 400:
    pikachu_rect.x += 6
  if keys[pygame.K_LEFT] and pikachu_rect.left - 6 >= 0:
    pikachu_rect.x -= 6
  
  screen.blit(pikachu_surface, pikachu_rect)

  pygame.display.update()
  clock.tick(60)
