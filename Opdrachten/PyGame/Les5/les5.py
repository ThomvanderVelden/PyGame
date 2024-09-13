'''
Gegeven is een oefenprogramma. Beantwoord de volgende vragen:

  - Wat gebeurt er als je met je muis over het stukje tekst heen gaat?
  - Wat gebeurt er als je op het stukje tekst klikt?
  - Wat gebeurt er als je het stukje tekst loslaat na inklikken?
  - Wat gebeurt er als je je muis stil laat staan op het stukje tekst? (MOUSEMOTION)

Doe nu zelf het volgende:

  - Verwijder de prints, deze maken je programma traag
  - Zorg dat het stukje tekst telkens een klein stukje naar rechts verschuift als je erop klikt
  - Maak een nieuwe tekst surface met de tekst: Gewonnen!
  - Als het stukje tekst de rechterkant van het scherm haalt blit dan dit nieuwe stukje tekst "Gewonnen!" naar het scherm
  - Je hebt nu je eerste speelbare mini-game gemaakt!

EXTRA:

Maak het spel leuker door mooie achtergronden en plaatjes te gebruiken. Zo wordt het een echt spel!

Slides: https://docs.google.com/presentation/d/1tnd7la5uNy5jzyHuBGmD2M-jPWfoy2RBY6XqtKHJ1zY/edit?usp=sharing
'''


import pygame, sys
from pygame.locals import QUIT

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Rects en de muis')
test_font = pygame.font.Font(None, 50)
clock = pygame.time.Clock()

background_surface = pygame.Surface((400, 300))
background_surface.fill("white")

tekst_surface = test_font.render("Stukje tekst!", False, "green")
tekst_rect = tekst_surface.get_rect(center = (200, 150))

while True:
  
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit() 
      
    if event.type == pygame.MOUSEMOTION:
      if tekst_rect.collidepoint(event.pos):
        print("Collision")
    if event.type == pygame.MOUSEBUTTONDOWN:
      if tekst_rect.collidepoint(event.pos):
        print("Tekst ingedrukt")
    if event.type == pygame.MOUSEBUTTONUP:
      if tekst_rect.collidepoint(event.pos):
        print("Tekst losgelaten")

  screen.blit(background_surface, (0, 0))
  screen.blit(tekst_surface, tekst_rect)

  pygame.display.update()
  clock.tick(60)