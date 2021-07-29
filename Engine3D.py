# Programa principal
from gl import Renderer, V2, color

import random

width = 1920
height = 1080

rend = Renderer(width, height)

rend.glLoadModel("models/model.obj",V2(width/2, height/2), V2(300,300))

#rend.glTriangle(V2(10, 70),  V2(50, 160), V2(70, 80), color(random.random(), random.random(),random.random()))
#rend.glTriangle(V2(180, 50), V2(150, 1),  V2(70, 180), color(random.random(), random.random(),random.random()))
#rend.glTriangle(V2(180, 150), V2(120, 160), V2(130, 180), color(random.random(), random.random(),random.random()))

rend.glFinish("output.bmp")


