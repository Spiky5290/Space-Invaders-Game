import pygame
import random
import math
from pygame import mixer

pygame.__init__
pygame.font.init()

screen = pygame.display.set_mode((800, 600))

# Icon and Caption
pygame.display.set_caption("My First Game")
icon = pygame.image.load('googlefit.png')
pygame.display.set_icon(icon)

# Font
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

text_X = 10
text_Y = 10

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (0, 255, 255))
    screen.blit(score, (x, y))

# Background
space = pygame.image.load('space.jpg')

# Spaceship
space_ship = pygame.image.load("spaceship.png")
spaceX = 300
spaceY = 450
space_cX = 0
space_cY = 0


def space_shipf(x, y):
    screen.blit(space_ship, (x, y))


# Enemy
enemy = pygame.image.load("enemy2.jpg")
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemy_cX = 2
enemy_cY = 7


def enemyf(x, y):
    screen.blit(enemy, (x, y))


# Bullet
bullet = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 0
bullet_cX = 0
bullet_cY = 3
bullet_state = "ready"



def bulletf(x, y):
    global bullet_state
    screen.blit(bullet, (x+5, y))

# Collision
def collisionf(xe, ye, xb, yb):
    distance = math.sqrt((math.pow((xe-xb), 2))+(math.pow((ye-yb), 2)))
    if distance < 30:
        return True
    else:
        return False

running = True
while running:

    screen.fill((0, 0, 0))
    screen.blit(space, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                space_cX = 2
            if event.key == pygame.K_LEFT:
                space_cX = -2
            if event.key == pygame.K_SPACE:
                bullet_state = "fire"

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                space_cX = 0

# Movement of Space Ship
    spaceX += space_cX
    if spaceX <= 0:
        spaceX = 0
    if spaceX >= 680:
        spaceX = 680


# Movement of Enemy
    enemyX += enemy_cX
    if enemyX <= 0:
        enemy_cX = 2
        enemyY += enemy_cY
    elif enemyX >= 701:
        enemy_cX = -2
        enemyY +=enemy_cY


# Movement of Bullet
    if bulletY <= 0:
        bulletY = 450
        bulletX = spaceX
        bullet_state = "ready"

    if bullet_state is "fire":
        bulletf(bulletX, bulletY)
        bulletY -= bullet_cY


    # Collision
    collision = collisionf(enemyX, enemyY, bulletX, bulletY)
    if collision == True:
        bulletY = spaceY
        bullet_state = "ready"
        score_value += 1
        enemyX = random.randint(0, 800)
        enemyY = random.randint(50, 150)


    bulletf(spaceX + 32, spaceY - 5)
    enemyf(enemyX, enemyY)
    space_shipf(spaceX, spaceY)
    show_score(text_X, text_Y)
    pygame.display.update()
