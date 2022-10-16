import pygame as pg
#initialize pg
pg.init()

#create scream 
screen = pg.display.set_mode((800,600))

#Changing the Title, Logo and Background Color
pg.display.set_caption("Space Invaders")
icon = pg.image.load('./img/logo.png')
pg.display.set_icon(icon)

#player
player_img  = pg.image.load('./img/player.png')

player_x = 370
player_y = 500

def player():
  screen.blit(player_img,( player_x, player_y))


#game loop 
running = True
while running:
  
  screen.fill((255,0,0))
  
  for i in pg.event.get():
    if i.type == pg.QUIT:
      running = False
      
  player()
  pg.display.update()
