import pygame as pg
import numpy as np

#initialize pg
pg.init()

#create scream 
screen = pg.display.set_mode((800,600))

#insert background-image
background = pg.image.load('./img/background.png')


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
enemy_x = np.random.uniform(0,800)
enemy_y = np.random.uniform(40, 200)

enemy_x_change:float = 4.0
enemy_y_change:float = 40.0

#bullet - bala proyectil
# ready -  you can´t  see the bullet on the screen
# fire - the bullet is currently moving
bullet_img = pg.image.load('./img/bullet.png')
bullet_x:float = 0.0
bullet_y:float = 400.0
bullet_x_change = 0
bullet_y_change = 10 
bullet_state = "ready"



def player(x, y):
  #Adding Images into Our Space Invader Game
  screen.blit(player_img,(x,y))


def enemy(x, y):
  #adding enemy into our space invader game
  screen.blit(enemy_img,(x,y))


def fire_bullet(x,y):
  global bullet_state 
  bullet_state = "fire"
  screen.blit(bullet_img,(x + 16, y + 10))


#game loop 
running = True
while running:
  
  #screen.fill((0,0,0))
  screen.blit(background, (0,0))
  
  for i in pg.event.get():
    if i.type == pg.QUIT:
      running = False
    
  #Movement Mechanics in Game Development 
  # if keystroke is pressed check whether its right or left
    if i.type == pg.KEYDOWN:
      print("anything keystroke")
      if i.key == pg.K_LEFT:
        print('arrow left is pressed')
        player_x_change = -4.0
      if i.key == pg.K_RIGHT:
        print('arrow right is pressed')
        player_x_change = 4.0
        
      if i.key == pg.K_SPACE:
        if bullet_state is "ready":
          # get the current x cordinate of the spaceship
          bullet_x = player_x
          fire_bullet(player_x, bullet_y)
          print('shoot')
        
    if i.type == pg.KEYUP:
      if i.key == pg.K_LEFT or i.key == pg.K_RIGHT:
        print("keystroke has benn released")
        player_x_change = 0.0
  
  
  player_x += player_x_change
  #Adding Boundaries to Our Game
  if player_x <= 0:
    player_x = 0.0
  elif player_x >= 736:
    player_x = 736.0
  
  enemy_x += enemy_x_change
  #Adding Boundaries to Our enemy
  #Movement Mechanics of the Enemy Space Invader
  if enemy_x <= 0:
    enemy_x_change = 3.0
    enemy_y += enemy_y_change
  elif enemy_x >= 736:
    enemy_x_change = -3.0
    #enemy_y -= enemy_y_change | bucle
  
  #multiple shoots 
  if bullet_y <= 0:
    bullet_y = 480.0
    bullet_state = "ready"
  
  # bullet movement 
  if bullet_state is "fire":
    fire_bullet(bullet_x, bullet_y)
    bullet_y -= bullet_y_change
  
  player(player_x, player_y)
  enemy(enemy_x, enemy_y)
  pg.display.update()
