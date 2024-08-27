import pygame

pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Voetbal game!')
clock = pygame.time.Clock()
test_font = pygame.font.Font("fonts/horror.ttf", 50)

voetbal_surface = pygame.image.load("graphics/voetbal.png")
tekst_surface = test_font.render("Voetbal game", False, "green")

while True:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  screen.blit(tekst_surface, (200, 100))
  screen.blit(voetbal_surface, (200, 200))
  
  pygame.display.update()
  clock.tick(60)