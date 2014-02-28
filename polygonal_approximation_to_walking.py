import math
import pygame

def radially_symmetric_polygon(screen, color, sides, center, radius, width, offset):

  arc = 2 * math.pi / sides
  point_list = []
  for i in range(sides):
    x = center[0] + radius * math.cos(i * arc + offset) 
    y = center[1] + radius * math.sin(i * arc + offset)
    point_list.append( (x,y))

  pygame.draw.polygon(screen, color, point_list, width)

pygame.init()

size = width, height = 1280, 720

screen = pygame.display.set_mode(size)

black = 0,0,0
white = 255,255,255

rotation = 0

while 1:
  
  screen.fill(white)
  pos = (int(width/2), int(height/2))
  radius = int(height/2.5)
  pygame.draw.circle(screen, black, pos, radius, 5)
  radially_symmetric_polygon(screen, (128,128,128), 6, pos, radius, 5, rotation)
  pygame.display.flip()
  
  rotation += 0.001
