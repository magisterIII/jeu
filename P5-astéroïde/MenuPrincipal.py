import core
from pygame import Rect


def menu():
# fond
    if not core.memory("FondMenuPrincipal").ready:
        core.memory("FondMenuPrincipal").load()
    core.memory("FondMenuPrincipal").show()
# boutons cliquables

    core.Draw.text((255, 255, 255), "Nouvelle Partie", (core.memory("LARGEUR")/(1920/840), core.memory("HAUTEUR")/(1080/500)), 50)

    core.Draw.text((255, 255, 255), "quitter", (core.memory("LARGEUR")/(1920/915), core.memory("LARGEUR")/(1920/900)), 50)

    if core.getMouseLeftClick():
        r = Rect(core.memory("LARGEUR")/(1920/898), core.memory("HAUTEUR")/(1080/500), 190, 50)
        if r.collidepoint(core.getMouseLeftClick()[0], core.getMouseLeftClick()[1]):
            core.memory("etat", 0.2)

        q = Rect(core.memory("LARGEUR")/(1920/915), core.memory("LARGEUR")/(1920/900), 190, 50)
        if q.collidepoint(core.getMouseLeftClick()[0], core.getMouseLeftClick()[1]):
            exit()



