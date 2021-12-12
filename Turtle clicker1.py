import pygame
from pygame.constants import KEYDOWN
import time


pygame.init()
# SCREEN
width = 500
height = 700
run = True
fps = 60
clock = pygame.time.Clock()
pygame.display.set_caption("Turtle Circuit")
icon = pygame.image.load("bean.png")
pygame.display.set_icon(icon)

#level
lvl = 1

# Background
bg = pygame.transform.scale(pygame.image.load("bg1.jpg"), (500, 700))
bgX = 0
bgY = 0


# PLAYER
player = pygame.transform.scale(pygame.image.load("player.png"), (50, 50))
playerX = 300
playerY = 640
change = 10
changen = 4

#ENEMY
enemy = pygame.transform.scale(pygame.image.load("bot.png"), (50, 50))
enemyX = 150
enemyY = 640
enemyY_change = 1

#Text
text_win = pygame.font.Font("freesansbold.ttf", 64)
text_lose = pygame.font.Font("freesansbold.ttf", 64)


def text_to_win(x, y):
    over = text_win.render("YOU WIN!", True, (255, 255, 255))
    window.blit(over, (x, y))
def text_to_lose(x, y):
    loser = text_lose.render("YOU LOSE!", True, (255, 255, 255))
    window.blit(loser, (x, y))
#TIMER
sc = 0
def win():
    if playerY <= 100:
        text_to_win(80, 450)
def lose():
    if enemyY <= 100:
        text_to_lose(80, 450)



window = pygame.display.set_mode((width, height))

while run:
    clock.tick(fps)
    window.blit(bg, (bgX, bgY))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # keyboard control
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                playerY -= change
                
    if playerY <= 100:
        enemyY_change = 0
        change = 0
    if enemyY <= 100:
       change = 0
       enemyY_change = 0
    win()
    lose()

    enemyY -= enemyY_change
    window.blit(player, (playerX, playerY))
    window.blit(enemy, (enemyX, enemyY))

    pygame.display.update()
    
