# Programa principal
from gl import Renderer

width = 960
height = 540

rend = Renderer(width, height)

rend.glClearColor(0, 0.3, 0)
rend.glClear()

rend.glColor(0.2, 1, 1)

rend.glPoint(700, 350)

for i in range(200):
    rend.glPoint(i,i)

rend.glFinish("output.bmp")


