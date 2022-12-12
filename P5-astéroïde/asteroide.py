import core
import random
from pygame import Rect
from pygame.math import Vector2

def asteroide():

# dessin astéroïdes
    core.memory("textureAsteroide", core.Texture("./asteroide.png", core.memory('shapeAsteroide1')))

    if not core.memory("textureAsteroide").ready:
        core.memory("textureAsteroide").load()
    core.memory("textureAsteroide").show()

# collision
    for tir in core.memory("projectiles"):
        if core.memory('shapeAsteroide2').collidepoint(tir["positionVaisseau"].x, tir["positionVaisseau"].y):
            core.memory("projectiles").remove(tir)
            core.memory('score', core.memory('score')+1)
            core.memory("shapeAsteroide1", Vector2(random.randint(0, core.memory("LARGEUR") - 100), random.randint(0, core.memory("HAUTEUR") - 100)))
            core.memory("vitesseAsteroide1", Vector2((random.randint(3, 10)), (random.randint(3, 10))))
            core.memory("textureAsteroide", core.Texture("./asteroide.png", core.memory('shapeAsteroide1')))
            core.memory("shapeAsteroide2",Rect(core.memory("shapeAsteroide1").x, core.memory("shapeAsteroide1").y, 90, 90))

# déplacement

    core.memory("shapeAsteroide1", core.memory("shapeAsteroide1") + core.memory("vitesseAsteroide1"))
    core.memory("shapeAsteroide2", Rect(core.memory("shapeAsteroide1").x, core.memory("shapeAsteroide1").y, 90, 90))



# boucle
    if core.memory("shapeAsteroide1").x < 0:
        core.memory("shapeAsteroide1").x = 1920

    if core.memory("shapeAsteroide1").x > 1920:
        core.memory("shapeAsteroide1").x = 0

    if core.memory("shapeAsteroide1").y < 0:
        core.memory("shapeAsteroide1").y = 1080

    if core.memory("shapeAsteroide1").y > 1080:
        core.memory("shapeAsteroide1").y = 0