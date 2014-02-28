import math
import pygame

def get_foot_pos(gait_angle, gait_pos, center, length):
  offset = gait_angle
  gait_pos -= int(gait_pos) 
  angle = gait_pos * gait_angle + offset
  return (center[0] + length * math.cos( angle ), \
          center[1] + length * math.sin( angle ) )

def stick_person(screen, color, center, length, width, gait_angle, gait_pos):

  foot_pos = get_foot_pos(gait_angle, gait_pos, center, length)
  pygame.draw.line(screen, color, center, foot_pos, width)

  # TODO make draw_leg function
  gait_pos = 1.0 - (gait_pos - int(gait_pos))
  foot_pos = get_foot_pos(gait_angle, gait_pos, center, length)
  pygame.draw.line(screen, color, center, foot_pos, width)
  
def radially_symmetric_polygon(screen, color, sides, center, radius, width, offset):

  arc = 2 * math.pi / sides
  offset -= arc
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
  
  gait_angle = (2.0 * math.pi) / sides
  gait_pos = rotation / gait_angle
 
  # get offset from ground
  foot_pos1 = get_foot_pos(gait_angle, gait_pos, pos, radius)
  #print pos[1], foot_pos1[1]
  offset_y = pos[1] + radius - foot_pos1[1]
  center = (pos[0], int(pos[1] + offset_y))

  pygame.draw.circle(screen, (230,230,230), center, radius, line_width)
  radially_symmetric_polygon(screen, (200,200,200), sides, center, radius, line_width, rotation)

  # ground
  pygame.draw.line(screen, (128,128,128), \
    (0, pos[1] + radius), (width, pos[1] + radius), line_width)
  
  stick_person(screen, black, center, radius, line_width * 2, gait_angle, gait_pos)
  pygame.display.flip()
  
  rotation += 0.004
  pygame.time.wait(10)
