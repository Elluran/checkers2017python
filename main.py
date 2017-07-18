import pygame, sys, game
from button import button

pygame.init()



size = width, height = 1000, 800

screen = pygame.display.set_mode(size)
pygame.display.set_caption("checker2017py")

surface = pygame.display.get_surface()
surface.fill(pygame.Color("white"))
pygame.display.flip()
butplay = button(150,300, 1)
butexit = button(150,340, 0)
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousepos = pygame.mouse.get_pos()
            if butexit.collision(mousepos[0], mousepos[1]): sys.exit()
            elif butplay.collision(mousepos[0], mousepos[1]): game.game()
        elif event.type == pygame.QUIT: sys.exit()

