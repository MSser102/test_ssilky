import pygame
import sys
pygame.init()
screen=pygame.display.set_mode((1024,720))
while True:
    pygame.display.update
    for event in pygame.event.get():
        if event.type==pygame.QUIT: sys.exit()