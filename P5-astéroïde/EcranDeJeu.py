
import core
from vaisseau import vaisseau
from TirVaisseau import tir
from asteroide import asteroide
from GestionDeLaVie import vie
from affichageTouches import touches
from BoucleSpatiale import boucle



def jeu():

    if not core.memory("FondJeu").ready:
        core.memory("FondJeu").load()
    core.memory("FondJeu").show()

# vaisseau (affichage, vitesse, position etc...)
    vaisseau()

# tir
    tir()

# boucle spatiale
    boucle()

# menu pause
    if core.getKeyPressList("ESCAPE"):
        core.memory('etat', 2)

# asteroides
    asteroide()

# gestion de la vie
    vie()

# score
    core.Draw.text((255, 255, 255), "score : "+str(core.memory("score")), (core.memory("LARGEUR")/(1920/860), (core.memory("HAUTEUR")/(1080/10))), 40, '')

#timer
    if core.memory('nombreDeCollision') !=3:
        core.memory("timer",core.memory("timer")+0.05)
        if 0 < core.memory("timer") % 30 < 0.1:
            if core.memory("timer") >1:
                core.memory("score", core.memory("score") + 5)
    core.Draw.text((255, 255, 255), "time : " + str(core.memory("timer")), (core.memory("LARGEUR") / (1920 / 1600), (core.memory("HAUTEUR") / (1080 / 10))), 40, '')

# touches utiles
    if core.memory('etat') == 2.1:
        touches()
