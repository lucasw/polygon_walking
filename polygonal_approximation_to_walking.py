import math
import pygame

def get_foot_pos(gait_angle, gait_pos, center, length, offset):
  gait_pos -= int(gait_pos) 
  angle = gait_pos * gait_angle + offset
  return (center[0] + length * math.cos( angle ), \
          center[1] + length * math.sin( angle ) )

def stick_person(screen, color, center, length, width, gait_angle, gait_pos, offset):

  foot_pos = get_foot_pos(gait_angle, gait_pos, center, length, offset)
  pygame.draw.line(screen, color, center, foot_pos, width)

  # TODO make draw_leg function
  gait_pos2 = 1.0 - (gait_pos - int(gait_pos))
  foot_pos = get_foot_pos(gait_angle, gait_pos2, center, length, offset)
  pygame.draw.line(screen, color, center, foot_pos, width)
 
  # upper body
  fr = 0.6
  torso_length = length * fr
  head_radius = length * (1.0 - fr) * 0.5
  neck = (center[0], center[1] - torso_length)
  head_center = (center[0], int(center[1] - (torso_length + head_radius)))
  pygame.draw.line(screen, color, center, neck, width)
  pygame.draw.circle(screen, color, head_center, int(head_radius), width)
  
  # arms
  gait_angle *= 1.3
  shoulder_center = (center[0], center[1] - (torso_length * 0.8))
  arm_length = length * 0.7
  hand_pos = get_foot_pos(gait_angle, gait_pos, shoulder_center, arm_length, offset)
  pygame.draw.line(screen, color, shoulder_center, hand_pos, width)
  hand_pos = get_foot_pos(gait_angle, gait_pos2, shoulder_center, arm_length, offset)
  pygame.draw.line(screen, color, shoulder_center, hand_pos, width)
  
def radially_symmetric_polygon(screen, color, sides, center, radius, width, rot, offset):

  arc = 2 * math.pi / sides
  point_list = []
  for i in range(sides):
    x = center[0] + radius * math.cos(i * arc + (rot + offset)) 
    y = center[1] + radius * math.sin(i * arc + (rot + offset))
    point_list.append( (x,y))

  pygame.draw.polygon(screen, color, point_list, width)

pygame.init()

size = width, height = 720, 720

screen = pygame.display.set_mode(size)

black = 0,0,0
white = 255,255,255

rotation = 0
sides = 5
line_width = 5
gait_angle = (2.0 * math.pi) / sides
offset = math.pi/2.0 - gait_angle/2

while 1:
  
  screen.fill(white)
 
  pos = (int(width/2), int(height/2))
  radius = int(height/2.5)
  
  gait_pos = rotation / gait_angle
 
  # get offset from ground
  foot_pos1 = get_foot_pos(gait_angle, gait_pos, pos, radius, offset)
  #print pos[1], foot_pos1[1]
  offset_y = pos[1] + radius - foot_pos1[1]
  center = (pos[0], int(pos[1] + offset_y))

  pygame.draw.circle(screen, (230,230,230), center, radius, line_width)
  radially_symmetric_polygon(screen, (200,200,200), sides, center, radius, line_width, rotation, offset)

  # ground
  pygame.draw.line(screen, (148,148,148), \
    (0, pos[1] + radius), (width, pos[1] + radius), line_width)
  
  stick_person(screen, black, center, radius, line_width * 2, gait_angle, gait_pos, offset)
  pygame.display.flip()
  
  rotation += gait_angle / 128
  pygame.time.wait(10)
