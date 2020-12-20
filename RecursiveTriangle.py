'''
'''

import pygame
import random

def main():
    width = int(1000)
    height = int(1000)
    window = pygame.display.set_mode((width,height))
    pygame.display.set_caption("Recursive Triangles")

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
    multiTriangles(window, int(width/2), int(20), int(width-20), int(height-20), int(20), int(height-20))

def multiTriangles(window, x1, y1, x2, y2, x3, y3):
    if x2-x3 < 5:
        pass
    else:
        randcolor = pygame.Color(random.randrange(256),random.randrange(256),random.randrange(256))
        pygame.draw.line(window,randcolor, (x1,y1), (x2,y2), 1)
        pygame.display.flip()
        randcolor = pygame.Color(random.randrange(256),random.randrange(256),random.randrange(256))
        pygame.draw.line(window,randcolor, (x2,y2), (x3,y3), 1)
        pygame.display.flip()
        randcolor = pygame.Color(random.randrange(256),random.randrange(256),random.randrange(256))
        pygame.draw.line(window,randcolor, (x3,y3), (x1,y1), 1)
        pygame.display.flip()
        multiTriangles(window, x1, y1, (x2+x1)/2, (y2+y1)/2, (x1+x3)/2, (y1+y3)/2)
        multiTriangles(window, (x2+x1)/2, (y2+y1)/2, x2, y2, (x2+x3)/2, (y2+y3)/2)
        multiTriangles(window, (x1+x3)/2, (y1+y2)/2, (x2+x3)/2, (y2+y3)/2, x3, y3)
main()
