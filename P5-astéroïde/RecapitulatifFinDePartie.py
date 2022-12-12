import core
from pygame import Rect
def recap():
    if not core.memory("FondMenuRecapitulatifFinDePartie").ready:
        core.memory("FondMenuRecapitulatifFinDePartie").load()
    core.memory("FondMenuRecapitulatifFinDePartie").show()



    core.Draw.text((255, 255, 255), "score : "+str(core.memory("score")), (core.memory("LARGEUR")/(1920/860), (core.memory("HAUTEUR")/(1080/400))), 50, '')

    core.Draw.text((255, 255, 255), "time : " + str(core.memory("timer")),(core.memory("LARGEUR") / (1920 / 860), (core.memory("HAUTEUR") / (1080 / 500))), 50, '')

    core.Draw.text((255, 255, 255), "peut mieux faire", (core.memory("LARGEUR")/(1920/800), core.memory("HAUTEUR")/(1080/900)), 50)

    core.Draw.rect((0, 0, 0), (core.memory("LARGEUR")/(1920/1600), core.memory("HAUTEUR")/(1080/900), 190, 50))
    core.Draw.text((255, 255, 255), "suite", (core.memory("LARGEUR")/(1920/1660), core.memory("HAUTEUR")/(1080/900)), 50)
    if core.getMouseLeftClick():
        v1 = Rect(core.memory("LARGEUR")/(1920/200), core.memory("HAUTEUR")/(1080/400), 100, 100)
        if v1.collidepoint(core.getMouseLeftClick()[0], core.getMouseLeftClick()[1]):
            core.Draw.rect((0, 0, 0), (core.memory("LARGEUR")/(1920/200), core.memory("HAUTEUR")/(1080/400), 100, 100), 4)
        core.memory('etat',3.1)

