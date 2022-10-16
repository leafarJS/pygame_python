import pygame as pg
import random as rd 

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

player_x:float = 370.0
player_y:float = 500.0

player_x_change:float = 0.0

#enemy
enemy_img = pg.image.load('./img/enemy.png')
enemy_x:int = rd.randint(0, 736)
enemy_y:int = rd.randint(50, 200)

enemy_x_change:int = 0




def player(x, y):
  #Adding Images into Our Space Invader Game
  screen.blit(player_img,(x,y))


def enemy(x, y):
  #adding enemy into our space invader game
  screen.blit(enemy_img,(x,y))
  

#game loop 
running = True
while running:
  
  screen.fill((255,150,0))
  
  for i in pg.event.get():
    if i.type == pg.QUIT:
      running = False
    
  #Movement Mechanics in Game Development 
  # if keystroke is pressed check whether its right or left
    if i.type == pg.KEYDOWN:
      print("anything keystroke")
      if i.key == pg.K_LEFT:
        print('arrow left is pressed')
        player_x_change = -0.4
      if i.key == pg.K_RIGHT:
        print('arrow right is pressed')
        player_x_change = 0.4
    if i.type == pg.KEYUP:
      if i.key == pg.K_LEFT or i.key == pg.K_RIGHT:
        print("keystroke has benn released")
        player_x_change = 0.0
  
  
  player_x += player_x_change
  #Adding Boundaries to Our Game
  if player_x <= 0:
    player_x = 0
  elif player_x >= 736:
    player_x = 736
  
      
  player(player_x, player_y)
  enemy(enemy_x, enemy_y)
  pg.display.update()
