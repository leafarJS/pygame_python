import pygame
#initialize pygame
pygame.init()

#create scream 
scream = pygame.display.set_mode((800,600))

#game loop 
running = True
while running:
  for i in pygame.event.get():
    if i.type == pygame.QUIT:
      running = False