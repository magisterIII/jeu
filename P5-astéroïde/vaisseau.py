from pygame.math import Vector2
import core

def vaisseau():

# position/vitesse du vaisseau
    vectP1 = core.memory("vitesseVaisseau")
    vectP1 = vectP1.rotate(90)
    vectP1.scale_to_length(10)
    P1 = core.memory("positionVaisseau") + vectP1

    vectP2 = Vector2(core.memory("vitesseVaisseau"))
    vectP2.scale_to_length(40)
    P2 = core.memory("positionVaisseau") + vectP2

    vectP3 = core.memory("vitesseVaisseau")
    vectP3 = vectP3.rotate(-90)
    vectP3.scale_to_length(10)
    P3 = core.memory("positionVaisseau") + vectP3


# dessin du vaisseau
    core.memory("couleurVaisseau") == (0,0,255)
    core.Draw.polygon(core.memory("couleurVaisseau"), (P1, P2, P3))
    P4 = Vector2(core.memory("positionVaisseau").x-50,core.memory("positionVaisseau").y-50)

    if core.memory("choixV") == 1:
        core.memory("textureVaisseau", core.Texture("./vaisseau1.png", P4))
        if not core.memory("textureVaisseau").ready:
            core.memory("textureVaisseau").load()
        core.memory("textureVaisseau").show()

    if core.memory("choixV") == 2:
        core.memory("textureVaisseau", core.Texture("./vaisseau2.png", P4))
        if not core.memory("textureVaisseau").ready:
            core.memory("textureVaisseau").load()
        core.memory("textureVaisseau").show()

    if core.memory("choixV") == 3:
        core.memory("textureVaisseau", core.Texture("./vaisseau3.png", P4))
        if not core.memory("textureVaisseau").ready:
            core.memory("textureVaisseau").load()
        core.memory("textureVaisseau").show()

    if core.memory("choixV") == 4:
        core.memory("textureVaisseau", core.Texture("./vaisseau4.png", P4))
        if not core.memory("textureVaisseau").ready:
            core.memory("textureVaisseau").load()
        core.memory("textureVaisseau").show()

# control du vaisseau
    core.memory("positionVaisseau", core.memory("positionVaisseau") + core.memory("vitesseVaisseau"))

    if core.getKeyPressList("z"):
        if 15 > core.memory('vitesseVaisseau').length() > 0:
            core.memory('vitesseVaisseau').scale_to_length(core.memory('vitesseVaisseau').length() + 0.2)
    if core.getKeyPressList("s"):
        if core.memory('vitesseVaisseau').length() > 0.2:
            core.memory('vitesseVaisseau').scale_to_length(core.memory('vitesseVaisseau').length() - 0.2)


# rotation précise
    if core.getMouseRightClick():
        if core.getKeyPressList('d'):
            core.memory("vitesseVaisseau", core.memory('vitesseVaisseau').rotate(1.5))

        if core.getKeyPressList('q'):
            core.memory("vitesseVaisseau", core.memory('vitesseVaisseau').rotate(-1.5))

    else:
        if core.getKeyPressList('d'):
            core.memory("vitesseVaisseau", core.memory('vitesseVaisseau').rotate(5))

        if core.getKeyPressList('q'):
            core.memory("vitesseVaisseau", core.memory('vitesseVaisseau').rotate(-5))

