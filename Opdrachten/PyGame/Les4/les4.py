import pygame

pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Auto rijden!')
clock = pygame.time.Clock()
running = True

background_surface = pygame.Surface((800, 400))
background_surface.fill("white")

weg_surface = pygame.image.load("graphics/weg.png").convert()

auto_surface = pygame.image.load("graphics/auto.png").convert_alpha()
auto_rect = auto_surface.get_rect(bottom = 350)

obstakel_surface = pygame.image.load("graphics/obstakel.png").convert_alpha()
obstakel_rect = obstakel_surface.get_rect(bottomleft = (625, 280))

while running:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  screen.blit(background_surface, (0, 0))
  screen.blit(weg_surface, (0, 75))
  screen.blit(obstakel_surface, obstakel_rect)
  
  auto_rect.left += 2
  if auto_rect.left > 800:
    auto_rect.right = 0
  screen.blit(auto_surface, auto_rect)

  pygame.display.update()
  clock.tick(60)
