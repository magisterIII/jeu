import time
import core
from pygame import Rect
from pygame.math import Vector2

def CreationTir():

    sp = Vector2(core.memory("positionVaisseau"))
    v = Vector2(core.memory("vitesseVaisseau"))
    v.scale_to_length(core.memory("vitesseVaisseau").length() + 10)
    r = 5
    c = (255, 100, 100)
    startTime = time.time()

    tir = {"positionVaisseau": sp, "vitesseVaisseau": v, "rayon": r, 'startTime': startTime, "color": c}
    core.memory("projectiles").append(tir)