# Programa principal
from gl import Renderer, V2, color
from numpy import sin, cos

import random


width = 1920
height = 1080

rend = Renderer(width, height)

rend.glLoadModel("models/model.obj",V2(width/2, height/2), V2(300,300))


rend.glFinish("output.bmp")


