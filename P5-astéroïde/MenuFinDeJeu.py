import core
from pygame import Rect

def finDeJeu():
# fond
    if not core.memory("FondMenuPrincipal").ready:
        core.memory("FondMenuPrincipal").load()
    core.memory("FondMenuPrincipal").show()

    #core.Draw.rect((100, 100, 255), (870, 500, 190, 50), 4)
    core.Draw.text((255, 255, 255), "Rejouer", (core.memory("LARGEUR")/(1920/898), core.memory("HAUTEUR")/(1080/500)), 50)

    #core.Draw.rect((100, 100, 255), (870, 700, 190, 50), 4)
    core.Draw.text((255, 255, 255), "MenuPrincipal", (core.memory("LARGEUR")/(1920/870), core.memory("HAUTEUR")/(1080/700)), 50)

    #core.Draw.rect((100, 100, 255), (870, 900, 190, 50), 4)
    core.Draw.text((255, 255, 255), "quitter", (core.memory("LARGEUR")/(1920/915), core.memory("HAUTEUR")/(1080/900)), 50)

    if core.getMouseLeftClick():
        r = Rect(core.memory("LARGEUR")/(1920/898), core.memory("HAUTEUR")/(1080/500), 190, 50)
        if r.collidepoint(core.getMouseLeftClick()[0], core.getMouseLeftClick()[1]):
            core.memory("etat", 4)


        m = Rect(core.memory("LARGEUR")/(1920/870), core.memory("HAUTEUR")/(1080/700), 190, 50)
        if m.collidepoint(core.getMouseLeftClick()[0], core.getMouseLeftClick()[1]):
            core.memory("etat", 5)

        q = Rect(core.memory("LARGEUR")/(1920/915), core.memory("HAUTEUR")/(1080/900), 190, 50)
        if q.collidepoint(core.getMouseLeftClick()[0], core.getMouseLeftClick()[1]):
            exit()

