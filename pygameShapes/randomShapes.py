#Module created by Ankith Kumar
#The random shapes generator used by eventListener and main.py
import pygame, sys
import random
import math
def generate(numberOfShapes, screen): # Random shapes generator method
    for i in range(numberOfShapes): #Generates many shapes depending on parameter fed
        width = random.randint(8, 300) #random shape width
        height = random.randint(8,300) #random shape height
        top = random.randint(8, 1500) #random shape location
        left = random.randint(8, 1500)#random shape width
        red = random.randint(0, 255)#random shape color red value
        green = random.randint(0, 255)#random shape color green value
        blue = random.randint(0, 255)#random shape color blue value
        color = [red, green, blue]#color value in [r, g, b] layout
        start_angle = 10*random.random() #Random arc angle start
        while start_angle > (2*math.pi): #Makes sure the arc angle is in between 0 and 2pi
            start_angle = 10*random.random()
        stop_angle = 10*random.random()
        while stop_angle > (2*math.pi):#Makes sure the arc angle is in between 0 and 2pi
            stop_angle = 10*random.random()
        line_chances = random.randint(0,1)
        if line_chances == 0: #If the shape will be colored outline and white inside
            line_width = random.randint(1, 3)
        else:#If the shape will be colored outline and colored inside
            line_width = 0

        shapeValue = random.randint(1, 21) #What type of shape will be displayed
        if shapeValue >= 1 and shapeValue <= 5: #If a rect will be drawn
            pygame.draw.rect(screen, color, [left, top, width, height], line_width)
        elif shapeValue >= 6 and shapeValue <= 10:#...circle...
            pygame.draw.circle(screen, color, [left, top], int(height/2), line_width)
        elif shapeValue >= 11 and shapeValue <= 15:#ellipse...
            pygame.draw.ellipse(screen, color, [left, top, width, height], random.randint(0,1))
        elif shapeValue >= 16 and shapeValue <= 20:#arc with angles
            pygame.draw.arc(screen, color, [left, top, width, height], start_angle, stop_angle, 1)
        elif shapeValue == 21:#a triangle (I know it says polygon but there is no triangle method)
            pygame.draw.polygon(screen, color, [[random.randint(0, 1780), random.randint(0, 960)], [random.randint(0, 1780), random.randint(0, 960)], [random.randint(0, 1780), random.randint(0, 960)]], random.randint(1, 3))
    pygame.display.flip() #render the shapes
