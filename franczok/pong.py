#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import pygame, sys
from pygame.locals import *

pygame.init()

# Prędkość odświeżania (frame per seconds)
FPS = 50
fpsClock = pygame.time.Clock()

# Szerokość i wysokość okna gry
GAMEWINDOW_W = 800
GAMEWINDOW_H = 400

DISPLAYSURF = pygame.display.set_mode((GAMEWINDOW_W,GAMEWINDOW_H), 0, 32)
pygame.display.set_caption('Prosty Pong')

# Kolory
LT_BLUE = (230,255,255)
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)

# Szerokość, wysokość, pozycja paletek
PADDLE_W = 100
PADDLE_H = 20
PADDLE_1_POS = (350, 360) #tupla
PADDLE_2_POS = (350, 20)

# Prędkość poruszania się paletki sterowanej przez komputer (AI)
AI_SPEED = 3

# Liczniki punktów
PLAYER_1_SCORE = '0'
PLAYER_2_SCORE = '0'

# Szerokość, wysokość, prędkość (x,y) piłeczki
BALL_W = 20
BALL_H = 20
BALL_X_SPEED = 6
BALL_Y_SPEED = 6

# Inicjacja paletki1
paddle1_surf = pygame.Surface([PADDLE_W, PADDLE_H])
paddle1_surf.fill(BLUE)
paddle1_rect = paddle1_surf.get_rect()
paddle1_rect.x = PADDLE_1_POS[0]
paddle1_rect.y = PADDLE_1_POS[1]

# Inicjacja paletki2
paddle2_surf = pygame.Surface([PADDLE_W, PADDLE_H])
paddle2_surf.fill(RED)
paddle2_rect = paddle2_surf.get_rect()
paddle2_rect.x = PADDLE_2_POS[0]
paddle2_rect.y = PADDLE_2_POS[1]

# Inicjacja piłeczki
ball_surf = pygame.Surface([BALL_W, BALL_H], pygame.SRCALPHA, 32).convert_alpha()
pygame.draw.ellipse(ball_surf, GREEN, [0, 0, BALL_W, BALL_H])
ball_rect = ball_surf.get_rect()
ball_rect.x = GAMEWINDOW_W/2
ball_rect.y = GAMEWINDOW_H/2

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEMOTION:
            mouseX, mouseY = event.pos
            
            # zaktualizuj pozycję paletki gracza
            shift = mouseX-(PADDLE_W/2)
            # przesunięcie w prawo
            if shift > GAMEWINDOW_W-PADDLE_W:
                shift = GAMEWINDOW_W-PADDLE_W
            # przesunięcie w lewo
            if shift < 0:
                shift = 0
            paddle1_rect.x = shift
    
    #AI
    if ball_rect.centerx > paddle2_rect.centerx:
        paddle2_rect.x += AI_SPEED
    elif ball_rect.centerx < paddle2_rect.centerx:
        paddle2_rect.x -= AI_SPEED
    
    #Przesuwamy piłeczke
    ball_rect.x += BALL_X_SPEED
    ball_rect.y += BALL_Y_SPEED
    
    #Sprawdzamy kolizję piłeczki
    if ball_rect.right >= GAMEWINDOW_W:
        BALL_X_SPEED *= -1
    if ball_rect.left <= 0:
        BALL_X_SPEED *= -1
        
    #Piłka i paletki
    if ball_rect.colliderect(paddle1_rect):
        BALL_Y_SPEED *= -1
        ball_rect.bottom = paddle1_rect.top
    
    if ball_rect.colliderect(paddle2_rect):
        BALL_Y_SPEED *= -1
        ball_rect.bottom = paddle2_rect.top
    
    # Co jeżeli piłka wyjdze poza pole gry?
    #Piłka uciekła w górę
    if ball_rect.top <= 0:
        ball_rect.x = GAMEWINDOW_W/2
        ball_rect.y = GAMEWINDOW_H/2
        Player_1_SCORE = str(int(PLAYER_1_SCORE)+ 1)
        
    #Piłka uciekła w dół
    if ball_rect.bottom >= GAMEWINDOW_H:
        ball_rect.x = GAMEWINDOW_W/2
        ball_rect.y = GAMEWINDOW_H/2
        PLAYER_2_SCORE = str(int(PLAYER_2_SCORE)+ 1)
        
    #Rysowanie obiektów
    DISPLAYSURF.fill(LT_BLUE)
    #Narysowanie obiektów w pamięci obrazu !!!
    DISPLAYSURF.blit(paddle1_surf, paddle1_rect)
    DISPLAYSURF.blit(paddle2_surf, paddle2_rect)
    DISPLAYSURF.blit(ball_surf,ball_rect)
    #Zaktualizuj okno
    
    pygame.display.update()
    
    fpsClock.tick(FPS)
