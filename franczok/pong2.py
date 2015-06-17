#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import pygame, sys
from pygame.locals import *

pygame.init()

# Prędkość odświeżania (frame per seconds)
FPS = 1000
fpsClock = pygame.time.Clock()

# Szerokość i wysokość okna gry
GAMEWINDOW_W = 1000
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
PADDLE_W = 20
PADDLE_H = 100
PADDLE_1_POS = (150, 950) #tupla
PADDLE_2_POS = (150, 40)

# Prędkość poruszania się paletki sterowanej przez komputer (AI)
AI_SPEED = 5

# Szerokość, wysokość, prędkość (x,y) piłeczki
BALL_W = 20
BALL_H = 20
BALL_X_SPEED = 3
BALL_Y_SPEED = 1

# Inicjacja paletki1
paddle1_surf = pygame.Surface([PADDLE_W, PADDLE_H])
paddle1_surf.fill(BLUE)
paddle1_rect = paddle1_surf.get_rect()
paddle1_rect.x = PADDLE_1_POS[1]
paddle1_rect.y = PADDLE_1_POS[0]

# Inicjacja paletki2
paddle2_surf = pygame.Surface([PADDLE_W, PADDLE_H])
paddle2_surf.fill(RED)
paddle2_rect = paddle2_surf.get_rect()
paddle2_rect.x = PADDLE_2_POS[1]
paddle2_rect.y = PADDLE_2_POS[0]

# Inicjacja piłeczki
ball_surf = pygame.Surface([BALL_W, BALL_H], pygame.SRCALPHA, 32).convert_alpha()
pygame.draw.ellipse(ball_surf, GREEN, [0, 0, BALL_W, BALL_H])
ball_rect = ball_surf.get_rect()
ball_rect.x = GAMEWINDOW_W/2
ball_rect.y = GAMEWINDOW_H/2

# Liczniki punktów
PLAYER_1_SCORE = '0'
PLAYER_2_SCORE = '0'
fontObj = pygame.font.Font('freesansbold.ttf', 64)

def drukuj_punkty_p1():
    tekst_obr1 = fontObj.render(PLAYER_1_SCORE, True, (0,0,0))
    tekst_prost1 = tekst_obr1.get_rect()
    tekst_prost1.center = (GAMEWINDOW_W/2, GAMEWINDOW_H*0.75)
    DISPLAYSURF.blit(tekst_obr1, tekst_prost1)

def drukuj_punkty_p2():
    tekst_obr2 = fontObj.render(PLAYER_2_SCORE, True, (0,0,0))
    tekst_prost2 = tekst_obr2.get_rect()
    tekst_prost2.center = (GAMEWINDOW_W/2, GAMEWINDOW_H/4)
    DISPLAYSURF.blit(tekst_obr2, tekst_prost2)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEMOTION:
            mouseX, mouseY = event.pos
            
            # zaktualizuj pozycję paletki gracza
            shift = mouseY-(PADDLE_H/2)
            # przesunięcie w prawo
            if shift > GAMEWINDOW_H-PADDLE_H:
                shift = GAMEWINDOW_H-PADDLE_H
            # przesunięcie w lewo
            if shift < 0:
                shift = 0
            paddle1_rect.y = shift
    
    #AI
    if ball_rect.centery > paddle2_rect.centery:
        paddle2_rect.y += AI_SPEED
    elif ball_rect.centery < paddle2_rect.centery:
        paddle2_rect.y -= AI_SPEED

    # Przesuwamy piłkę
    ball_rect.x += BALL_X_SPEED
    ball_rect.y += BALL_Y_SPEED

    # Sprawdzamy kolizje piłki z obiektami
    if ball_rect.bottom >= GAMEWINDOW_H:
        BALL_Y_SPEED *= -1
    if ball_rect.top <= 0:
        BALL_Y_SPEED *= -1
        
    # Piłka i paleteki
    if ball_rect.colliderect(paddle1_rect):
        BALL_X_SPEED *= -1
        ball_rect.right = paddle1_rect.left
        
    if ball_rect.colliderect(paddle2_rect):
        BALL_X_SPEED *= -1
        ball_rect.left = paddle2_rect.right
    
    # Co jeżeli piłka wyjdzie poza pole gry?
    # piłka uciekła w górę
    if ball_rect.left <= 0:
        ball_rect.x = GAMEWINDOW_W/2
        ball_rect.y = GAMEWINDOW_H/2
        PLAYER_1_SCORE = str(int(PLAYER_1_SCORE) + 1)
    # piłka uciekła w dół
    if ball_rect.right >= GAMEWINDOW_W:
        ball_rect.x = GAMEWINDOW_W/2
        ball_rect.y = GAMEWINDOW_H/2
        PLAYER_2_SCORE = str(int(PLAYER_2_SCORE) + 1)

    # Rysowanie obiektów
    DISPLAYSURF.fill(LT_BLUE)
    
    drukuj_punkty_p1()
    drukuj_punkty_p2()
    
    # Narysowanie obiektów w pamięci obrazu !!!
    DISPLAYSURF.blit(paddle1_surf,paddle1_rect)
    DISPLAYSURF.blit(paddle2_surf,paddle2_rect)
    DISPLAYSURF.blit(ball_surf,ball_rect)
    
    # Zaktualizuj okno
    pygame.display.update()
    
    fpsClock.tick(FPS)
