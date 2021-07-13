# Programa principal
from gl import Renderer, V2, color
from numpy import sin, cos


width = 960
height = 540

rend = Renderer(width, height)

#rend.glViewport
#rend.glLine(V2(2, 5), V2(900, 420), color(1,0,0))
#rend.glLine(V2(0, 0), V2(40, 500), color(0,1,0))
#rend.glLine(V2(900, 500), V2(600, 100), color(0,0,1))
#rend.glLine(V2(200, 400), V2( 500, 400), color(0.2,0.2,0.2))

for x in range(width):
    x0 = x 
    x1 = x + 1

    y0 = sin(x0 * 0.1) * 50 + height/2
    y1 = sin(x1 * 0.1) * 50 + height/2

    rend.glLine(V2(int(x0), int(y0)), V2(int(x1), int(y1)))

rend.glFinish("output.bmp")


