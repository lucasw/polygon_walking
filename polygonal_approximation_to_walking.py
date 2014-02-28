import math
import pygame

def stick_person(screen, color, center, length, width, gait_angle, gait_pos):

  pygame.draw.line(screen, color, center, ( \
     center[0] + length * math.cos( gait_pos * gait_angle ), \
     center[1] + length * math.sin( gait_pos * gait_angle ) \
     ), width)

def radially_symmetric_polygon(screen, color, sides, center, radius, width, offset):

  arc = 2 * math.pi / sides
  point_list = []
  for i in range(sides):
    x = center[0] + radius * math.cos(i * arc + offset) 
    y = center[1] + radius * math.sin(i * arc + offset)
    point_list.append( (x,y))

  pygame.draw.polygon(screen, color, point_list, width)

pygame.init()

size = width, height = 720, 720

screen = pygame.display.set_mode(size)

black = 0,0,0
white = 255,255,255

rotation = 0
sides = 6
line_width = 5

while 1:
  
  screen.fill(white)
  pos = (int(width/2), int(height/2))
  radius = int(height/2.5)
  pygame.draw.circle(screen, (32,32,32), pos, radius, line_width)
  radially_symmetric_polygon(screen, (64,64,64), sides, pos, radius, line_width, rotation)

  gait_angle = (2.0 * math.pi) / sides
  stick_person(screen, black, pos, radius, line_width, gait_angle, rotation / gait_angle)
  pygame.display.flip()
  
  rotation += 0.001
