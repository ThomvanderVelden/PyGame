# Dit is een voorbeeld. Je kan dit voorbeeld gebruiken om geluid toe te voegen in je eigen game.

import pygame, sys
from pygame.locals import QUIT

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Animaties')
clock = pygame.time.Clock()

background_surface = pygame.Surface((400, 300))
background_surface.fill("white")

speler_stil1_surface = pygame.image.load(
    "graphics/speler_stil1.png").convert_alpha()
speler_stil2_surface = pygame.image.load(
    "graphics/speler_stil2.png").convert_alpha()
animaties = [speler_stil1_surface, speler_stil2_surface]
index = 0

speler_jump_surface = pygame.image.load(
    "graphics/speler_jump.png").convert_alpha()

speler_rect = speler_stil1_surface.get_rect(midbottom=(200, 300))

zwaartekracht = 0

pygame.mixer.init()

# Hier laden we het geluid naar een variabele
jump_sound = pygame.mixer.Sound("audio/jump.mp3")

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and speler_rect.bottom >= 300:
                zwaartekracht = -20
                # Zo spelen we het geluid af
                jump_sound.play()

    screen.blit(background_surface, (0, 0))

    zwaartekracht += 1
    speler_rect.y += zwaartekracht

    if speler_rect.bottom >= 300:
        speler_rect.bottom = 300

    index += 0.05

    if index > len(animaties):
        index = 0

    if speler_rect.bottom < 300:
        screen.blit(speler_jump_surface, speler_rect)
    else:
        screen.blit(animaties[int(index)], speler_rect)

    pygame.display.update()
    clock.tick(60)
