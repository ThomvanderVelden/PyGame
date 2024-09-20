# Gegeven is onze pikachu game met een bijbehorende score!

# Fix de 2 dingen uit de slides:
#   - Zorg ervoor dat de score reset als de game opnieuw begint
#   - Zorg ervoor dat de score 1, 2, 3 etc is in plaats van in milliseconden!

# Slides:
# https://docs.google.com/presentation/d/1fypqkKR8hXHAcCNLEhVTnleWQov4aNpeM4in-MXKF1Q/edit?usp=sharing

import pygame, sys
from pygame.locals import QUIT

def score():
  time = pygame.time.get_ticks()
  score_surface = font.render(str(time), False, "orange")
  score_rect = score_surface.get_rect(center = (200, 100))
  screen.blit(score_surface, score_rect)

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Score')
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

    if game_actief:
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE and pikachu_rect.bottom >= 300:
          zwaartekracht = -20
    else:
      if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        game_actief = True
        
  if game_actief:
    screen.blit(background_surface, (0, 0))
    screen.blit(enemy_surface, enemy_rect)
    score()
  
    zwaartekracht += 1
    pikachu_rect.y += zwaartekracht
  
    if pikachu_rect.bottom >= 300:
      pikachu_rect.bottom = 300
  
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and pikachu_rect.right + 6 <= 400:
      pikachu_rect.x += 6
    if keys[pygame.K_LEFT] and pikachu_rect.left - 6 >= 0:
      pikachu_rect.x -= 6

    if pikachu_rect.colliderect(enemy_rect):
      game_actief = False
    
    screen.blit(pikachu_surface, pikachu_rect)
  else:
    screen.fill("black")
    pikachu_rect.topleft = (180, 20)

  pygame.display.update()
  clock.tick(60)