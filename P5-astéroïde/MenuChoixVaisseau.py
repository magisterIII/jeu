import core
from pygame import Rect

def ChoixVaisseau():
    if not core.memory("FondChoixVaisseau").ready:
        core.memory("FondChoixVaisseau").load()
    core.memory("FondChoixVaisseau").show()


# textures vaisseaux
    if not core.memory("textureVaisseau1").ready:
        core.memory("textureVaisseau1").load()
    core.memory("textureVaisseau1").show()

    if not core.memory("textureVaisseau2").ready:
        core.memory("textureVaisseau2").load()
    core.memory("textureVaisseau2").show()

    if not core.memory("textureVaisseau3").ready:
        core.memory("textureVaisseau3").load()
    core.memory("textureVaisseau3").show()

    if not core.memory("textureVaisseau4").ready:
        core.memory("textureVaisseau4").load()
    core.memory("textureVaisseau4").show()

# boutons cliquables
    #core.Draw.rect((100, 100, 255), (1600, 900, 190, 50), 4)
    core.Draw.text((255, 255, 255), "jouer", (core.memory("LARGEUR")/(1920/1660), core.memory("HAUTEUR")/(1080/900)), 50)

    #core.Draw.rect((100, 100, 255), (170, 900, 190, 50), 4)
    core.Draw.text((255, 255, 255), "retour", (core.memory("LARGEUR")/(1920/220), core.memory("HAUTEUR")/(1080/900)), 50)

    if core.getMouseLeftClick():
        j = Rect(core.memory("LARGEUR")/(1920/1600), core.memory("HAUTEUR")/(1080/900), 190, 50)
        if j.collidepoint(core.getMouseLeftClick()[0], core.getMouseLeftClick()[1]):
            core.memory("etat", 1)

        r = Rect(core.memory("LARGEUR")/(1920/170), core.memory("HAUTEUR")/(1080/900), 190, 50)
        if r.collidepoint(core.getMouseLeftClick()[0], core.getMouseLeftClick()[1]):
            core.memory("etat", 0)

# boutons cliquables choix vaisseau
    if core.getMouseLeftClick():
        v1 = Rect(core.memory("LARGEUR")/(1920/200), core.memory("HAUTEUR")/(1080/400), 100, 100)
        if v1.collidepoint(core.getMouseLeftClick()[0], core.getMouseLeftClick()[1]):
            core.Draw.rect((100, 100, 255), (core.memory("LARGEUR")/(1920/200), core.memory("HAUTEUR")/(1080/400), 100, 100), 4)
            core.memory("choixV", 1)

        v2 = Rect(core.memory("LARGEUR")/(1920/650), core.memory("HAUTEUR")/(1080/400), 100, 100)
        if v2.collidepoint(core.getMouseLeftClick()[0], core.getMouseLeftClick()[1]):
            core.Draw.rect((100, 100, 255), (core.memory("LARGEUR")/(1920/650), core.memory("HAUTEUR")/(1080/400), 100, 100), 4)
            core.memory("choixV", 2)

        v3 = Rect(core.memory("LARGEUR")/(1920/1150), core.memory("HAUTEUR")/(1080/400), 100, 100)
        if v3.collidepoint(core.getMouseLeftClick()[0], core.getMouseLeftClick()[1]):
            core.Draw.rect((100, 100, 255), (core.memory("LARGEUR")/(1920/1150), core.memory("HAUTEUR")/(1080/400), 100, 100), 4)
            core.memory("choixV", 3)

        v4 = Rect(core.memory("LARGEUR")/(1920/1600), core.memory("HAUTEUR")/(1080/400), 100, 100)
        if v4.collidepoint(core.getMouseLeftClick()[0], core.getMouseLeftClick()[1]):
            core.Draw.rect((100, 100, 255), (core.memory("LARGEUR")/(1920/1600), core.memory("HAUTEUR")/(1080/400), 100, 100), 4)
            core.memory("choixV", 4)