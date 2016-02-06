#Module created by Ankith Kumar
#Event/Action Listener used by main.py

import pygame, sys
import random
import randomShapes
def listen(screen): #Event listener method, loops while program is running
    randomShapes.generate(700, screen)#display first artpiece
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # if close button
                sys.exit()#close window
            elif event.type == pygame.KEYDOWN: #Any button clicked --> change the art on screen 
                screen.fill([random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)])
                randomShapes.generate(700, screen)#display 700 new shapes on a new artpiece
                pygame.display.flip() #render the new art
