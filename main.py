import pygame as pg
import random as rd
import math as mt

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

player_x = 370
player_y = 500

player_x_change = 0

#multiple enemies 
enemy_img = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
num_of_enemies = 6

#enemy
for i in range(num_of_enemies):
  enemy_img.append(pg.image.load('./img/enemy.png'))
  enemy_x.append(rd.randint(0,735))
  enemy_y.append(rd.randint(50, 150))

  enemy_x_change.append(4)
  enemy_y_change.append(40)

#bullet - bala proyectil
# ready -  you can´t  see the bullet on the screen
# fire - the bullet is currently moving
bullet_img = pg.image.load('./img/bullet.png')
bullet_x = 0
bullet_y = 400 
bullet_x_change = 0
bullet_y_change = 10 
bullet_state = "ready"

#score 
score_value  = 0
#https://www.dafont.com
font = pg.font.Font('freesansbold.ttf', 32)

text_x = 10
text_y = 10

#show score in the screen
def show_score(x, y):
  score = font.render("Score: " + str(score_value), True, (0,255,0))
  screen.blit(score, (x, y))


def player(x, y):
  #Adding Images into Our Space Invader Game
  screen.blit(player_img,(x,y))


def enemy(x, y, i):
  #adding enemy into our space invader game
  screen.blit(enemy_img[i],(x,y))


def fire_bullet(x,y):
  global bullet_state 
  bullet_state = "fire"
  screen.blit(bullet_img,(x + 16, y + 10))


def isCollision(enemy_x, enemy_y, bullet_x, bullet_y):
  #form math distance 
  distance = mt.sqrt(mt.pow(enemy_x - bullet_x, 2) + (mt.pow(enemy_y -bullet_y, 2)))
  #print(distance)
  if distance < 27:
    return True
  else:
    return False


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
      #print("anything keystroke")
      if i.key == pg.K_LEFT:
        #print('arrow left is pressed')
        player_x_change = -4
      if i.key == pg.K_RIGHT:
        #print('arrow right is pressed')
        player_x_change = 4
        
      if i.key == pg.K_SPACE:
        if bullet_state is "ready":
          # get the current x cordinate of the spaceship
          bullet_x = player_x
          fire_bullet(player_x, bullet_y)
          #print('shoot')
        
    if i.type == pg.KEYUP:
      if i.key == pg.K_LEFT or i.key == pg.K_RIGHT:
        #print("keystroke has benn released")
        player_x_change = 0
  
  
  player_x += player_x_change
  #Adding Boundaries to Our Game
  if player_x <= 0:
    player_x = 0
  elif player_x >= 736:
    player_x = 736
  
  for i in range(num_of_enemies):
    enemy_x[i] += enemy_x_change[i]
    #Adding Boundaries to Our enemy
    #Movement Mechanics of the Enemy Space Invader
    if enemy_x[i] <= 0:
      enemy_x_change[i] = 3
      enemy_y[i] += enemy_y_change[i]
    elif enemy_x[i] >= 736:
      enemy_x_change[i] = -3
      #enemy_y -= enemy_y_change | bucle
    
    #collision 
    collision = isCollision(enemy_x[i], enemy_y[i], bullet_x, bullet_y)
    
    if collision is True:
      bullet_y = 480
      bullet_state = "ready"
      score_value += 1
      enemy_x[i] = rd.randint(0,735)
      enemy_y[i] = rd.randint(50, 150)
      #print(score_value) 
    
    enemy(enemy_x[i], enemy_y[i], i)

  #multiple shoots 
  if bullet_y <= 0:
    bullet_y = 480
    bullet_state = "ready"
  
  # bullet movement 
  if bullet_state is "fire":
    fire_bullet(bullet_x, bullet_y)
    bullet_y -= bullet_y_change
  
  player(player_x, player_y)
  show_score(text_x, text_y)
  pg.display.update()
