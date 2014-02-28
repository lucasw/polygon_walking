import pygame

pygame.init()

size = width, height = 1280, 720

screen = pygame.display.set_mode(size)

black = 0,0,0
white = 255,255,255

while 1:
  
  screen.fill(white)
  pos = (int(width/2), int(height/2))
  radius = int(height/2.5)
  pygame.draw.circle(screen, black, pos, radius, 5)
  pygame.display.flip()
