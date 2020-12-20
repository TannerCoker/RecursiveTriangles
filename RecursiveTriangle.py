'''
'''

import pygame
import random

def main():
    width = int(700)
    height = int(700)
    window = pygame.display.set_mode((width,height))

    pygame.display.flip()
    makeTriangles(window,width,height)


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


#Creates the initial Triangle and then calls the recursive triangle func
def makeTriangles(window,width,height):
    randcolor = pygame.Color(random.randrange(256),random.randrange(256),random.randrange(256))
    pygame.draw.line(window, randcolor, (width/2,20), (width-20,height-20), 1)
    randcolor = pygame.Color(random.randrange(256),random.randrange(256),random.randrange(256))
    pygame.draw.line(window, randcolor, (width-20,height-20), (20,height-20), 1)
    randcolor = pygame.Color(random.randrange(256),random.randrange(256),random.randrange(256))
    pygame.draw.line(window, randcolor, (20,height-20), (width/2,20), 1)
    pygame.display.flip()

main()
