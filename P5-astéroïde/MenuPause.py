import core
from pygame import Rect

def pause():

    #core.Draw.rect((100, 100, 255), (870, 300, 190, 50), 4)
    core.Draw.text((100, 100, 255), " Reprendre", (core.memory("LARGEUR")/(1920/900), core.memory("HAUTEUR")/(1080/300)), 50)

    #core.Draw.rect((100, 100, 255), (870, 500, 190, 50), 4)
    core.Draw.text((100, 100, 255), "guide des touches", (core.memory("LARGEUR")/(1920/860), core.memory("HAUTEUR")/(1080/500)), 50)

    #core.Draw.rect((100, 100, 255), (870, 700, 190, 50), 4)
    core.Draw.text((100, 100, 255), "Menu Principal", (core.memory("LARGEUR")/(1920/900), core.memory("HAUTEUR")/(1080/700)), 50)

    #core.Draw.rect((100, 100, 255), (870, 900, 190, 50), 4)
    core.Draw.text((100, 100, 255), "    quitter", (core.memory("LARGEUR")/(1920/900), core.memory("HAUTEUR")/(1080/900)), 50)

    if core.getMouseLeftClick():
        r = Rect(core.memory("LARGEUR")/(1920/870), core.memory("HAUTEUR")/(1080/300), 190, 50)
        if r.collidepoint(core.getMouseLeftClick()[0], core.getMouseLeftClick()[1]):
            core.memory("etat", 1)

        g = Rect(core.memory("LARGEUR")/(1920/870), core.memory("HAUTEUR")/(1080/500), 190, 50)
        if g.collidepoint(core.getMouseLeftClick()[0], core.getMouseLeftClick()[1]):
            core.memory("etat", 2.1)

        m = Rect(core.memory("LARGEUR")/(1920/870), core.memory("HAUTEUR")/(1080/700), 190, 50)
        if m.collidepoint(core.getMouseLeftClick()[0], core.getMouseLeftClick()[1]):
            core.memory("etat", 5)

        q = Rect(core.memory("LARGEUR")/(1920/870), core.memory("HAUTEUR")/(1080/900), 190, 50)
        if q.collidepoint(core.getMouseLeftClick()[0], core.getMouseLeftClick()[1]):
            exit()
