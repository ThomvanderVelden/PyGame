'''
Voeg de volgende 2 dingen aan de game toe:

  - Laat de auto aan de linkerkant van het scherm terugkomen als de auto aan de rechterkant van het scherm af rijdt HINT: Gebruik een ```if``` met daarin de ```x_pos```
  - Laat een aantal regendruppels van de bovenkant van het scherm naar beneden vallen

Slides: https://docs.google.com/presentation/d/16rz2C4Pqhx4YNCokEU_5mc3rtQXXNEoi7gFAGzv9s_A/edit?usp=sharing
'''

import pygame

pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Auto rijden!')
clock = pygame.time.Clock()
running = True

background_surface = pygame.Surface((800, 400))
background_surface.fill("white")

auto_surface = pygame.image.load("graphics/auto.png").convert_alpha()
auto_x_pos = 200

while running:

    for event in pygame.event.get():
     if event.type == pygame.QUIT:
      running = False

    screen.blit(background_surface, (0, 0))

    auto_x_pos += 1
    screen.blit(auto_surface, (auto_x_pos, 200))

    pygame.display.update()
    clock.tick(60)