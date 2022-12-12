import core

from pygame.math import Vector2
from pygame import Rect
import random

def vie():
    if core.memory('shapeAsteroide2').collidepoint(core.memory("positionVaisseau")):
        core.memory('nombreDeCollision', core.memory('nombreDeCollision')+1)
        core.memory("shapeAsteroide1", Vector2(random.randint(0, core.memory("LARGEUR") - 100), random.randint(0, core.memory("HAUTEUR") - 100)))
        core.memory("shapeAsteroide2", Rect(core.memory("shapeAsteroide1").x, core.memory("shapeAsteroide1").y, 90, 90))

# 3 vies restantes
    if core.memory('nombreDeCollision') == 0:
        if not core.memory("textureCoeur1").ready:
            core.memory("textureCoeur1").load()
        core.memory("textureCoeur1").show()

        if not core.memory("textureCoeur2").ready:
            core.memory("textureCoeur2").load()
        core.memory("textureCoeur2").show()

        if not core.memory("textureCoeur3").ready:
            core.memory("textureCoeur3").load()
        core.memory("textureCoeur3").show()

# 2 vies restantes
    if core.memory('nombreDeCollision') == 1:
        core.memory("couleurVaisseau", (100, 100, 255))

        if not core.memory("textureCoeur1").ready:
            core.memory("textureCoeur1").load()
        core.memory("textureCoeur1").show()

        if not core.memory("textureCoeur2").ready:
            core.memory("textureCoeur2").load()
        core.memory("textureCoeur2").show()

# 1 vies restantes
    if core.memory('nombreDeCollision') == 2:
        core.memory("couleurVaisseau", (255, 100, 100))

        if not core.memory("textureCoeur1").ready:
            core.memory("textureCoeur1").load()
        core.memory("textureCoeur1").show()

# 0 vies restantes // fin de jeu
    if core.memory('nombreDeCollision') == 3:
        core.memory('etat', 3)

