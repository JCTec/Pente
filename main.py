# -*- coding: UTF-8 -*-
from Pente import Pente
from move import move
import pygame
from pygame.locals import *

pente = Pente()

while True:

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and not pente.finished:
            pente.didClickMouse()

        if event.type == pygame.KEYDOWN and not pente.finished:
            pente.didClickKey(event)

        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)


