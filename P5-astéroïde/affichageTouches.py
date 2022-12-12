import core
from pygame import Rect


def touches():
# touches
    core.Draw.text((100, 100, 100), "  déplacements   ===>  z; q;s; d", (core.memory("LARGEUR")/(1920/870), core.memory("HAUTEUR")/(1080/300)), 25)
    core.Draw.text((100, 100, 100), "      tirs       ===>   espace", (core.memory("LARGEUR")/(1920/870), core.memory("HAUTEUR")/(1080/500)), 25)
    core.Draw.text((100, 100, 100), "rotation précise ===> clic droit", (core.memory("LARGEUR")/(1920/870), core.memory("HAUTEUR")/(1080/700)), 25)

# boutons cliquables

    #core.Draw.rect((100, 100, 255), (170, 900, 190, 50), 4)
    core.Draw.text((100, 100, 255), "retour", (core.memory("LARGEUR")/(1920/220), core.memory("HAUTEUR")/(1080/900)), 50)

    if core.getMouseLeftClick():
        m = Rect(core.memory("LARGEUR")/(1920/170), core.memory("HAUTEUR")/(1080/900), 190, 50)
        if m.collidepoint(core.getMouseLeftClick()[0], core.getMouseLeftClick()[1]):
            core.memory("etat", 2)