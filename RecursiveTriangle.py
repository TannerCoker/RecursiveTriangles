'''
'''

import pygame
import random

def main():
    width = int(700)
    height = int(700)
    window = pygame.display.set_mode((width,height))
    pygame.draw.line(window, (255,255,255), (300,20), (500,500), 1)
    pygame.display.flip()



    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


#Creates the initial Triangle and then calls the recursive triangle func
def makeTriangles(width,height):
    pass

main()
