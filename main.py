import pygame
#initialize pygame
pygame.init()

#create scream 
screen = pygame.display.set_mode((800,600))

#Changing the Title, Logo and Background Color
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('./img/logo.png')
pygame.display.set_icon(icon)

#game loop 
running = True
while running:
  for i in pygame.event.get():
    if i.type == pygame.QUIT:
      running = False
      
  screen.fill((255,0,0))
  pygame.display.update()
