# Programa principal
from gl import Renderer, V2, color
from numpy import sin, cos

import random


width = 1920
height = 1080

rend = Renderer(width, height)


#static
#for x in range(width):
#    for y in range(height):
#        if random.random() > 0.5:
#            rend.glPoint(x,y)

#color static
#for x in range(width):
#    for y in range(height):
#            rend.glPoint(x,y,color(random.random(),
#                                   random.random(),
#                                   random.random()))


# stars
#def star(x, y, size):
#    comp = random.random()
#    rend.glColor(comp,comp,comp)

#    if size == 1:
#        rend.glPoint(x,y)
#    elif size == 2:
#        rend.glPoint(x,y)
#        rend.glPoint(x+1,y)
#        rend.glPoint(x,y+1)
#        rend.glPoint(x+1,y+1)
#    elif size == 3:
#        rend.glPoint(x,y)
#        rend.glPoint(x+1,y)
#        rend.glPoint(x-1,y)
#        rend.glPoint(x,y+1)
#        rend.glPoint(x,y-1)

#for x in range(width):
#    for y in range(height):
#        if random.random() < 0.005:
#            star(x,y,random.randint(1,3))

for x in range(0, width, 40):
    rend.glLine(V2(0,0), V2(x,height))
    rend.glLine(V2(0,height), V2(x,0))

    rend.glLine(V2(width,0), V2(width - x,height))
    rend.glLine(V2(width,height), V2(width - x,0))







rend.glFinish("output.bmp")


