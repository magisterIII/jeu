import core
from pygame.math import Vector2
import random
from pygame import Rect
from MenuPrincipal import menu
from EcranDeJeu import jeu
from MenuFinDeJeu import finDeJeu
from MenuPause import pause
from MenuChoixVaisseau import ChoixVaisseau
from affichageTouches import touches
from RecapitulatifFinDePartie import recap
import pygame

def setup(etat):
    print("setup START---------")

# info écran
    pygame.init()
    info = pygame.display.Info()
    core.memory("LARGEUR", info.current_w)
    core.memory("HAUTEUR", info.current_h)


# definition fenêtre
    core.fps = 60
    core.WINDOW_SIZE = [core.memory("LARGEUR"), core.memory("HAUTEUR")]
    print("setup END-----------")
    core.memory("etat", etat)


# vaisseau
    core.memory("vitesseVaisseau", Vector2(0, -1.88))
    core.memory("positionVaisseau", Vector2(core.memory("LARGEUR")/2, core.memory("HAUTEUR")/2))
    core.memory("rotationV",Vector2(core.memory("positionVaisseau").x,core.memory("positionVaisseau").y))
    core.memory("couleurVaisseau", (0, 0, 255))
    core.memory("choixV",2)

# projectiles
    core.memory("projectiles", [])


# astéroïdes
    core.memory("Asteroide1", [])
    core.memory("vitesseAsteroide1", Vector2((random.randint(3, 10)), (random.randint(3, 10))))
    core.memory("shapeAsteroide1", Vector2(random.randint(0, core.memory("LARGEUR")-100), random.randint(0, core.memory("HAUTEUR")-100)))
    core.memory("shapeAsteroide2",  Rect(core.memory("shapeAsteroide1").x,core.memory("shapeAsteroide1").y,90,90))

# timer
    core.memory("timer", 0)

# score
    core.memory("score", 0)


# etat vie + etat collision astéroide
    core.memory("endommagement", 0)
    core.memory('nombreDeCollision', 0)


# TEXTURES
# texture vaisseaux
    core.memory("textureVaisseau1", core.Texture("./vaisseau1.png", Vector2(core.memory("LARGEUR")/(1920/200), core.memory("HAUTEUR")/(1080/400))))
    core.memory("textureVaisseau2", core.Texture("./vaisseau2.png", Vector2(core.memory("LARGEUR")/(1920/650), core.memory("HAUTEUR")/(1080/400))))
    core.memory("textureVaisseau3", core.Texture("./vaisseau3.png", Vector2(core.memory("LARGEUR")/(1920/1150), core.memory("HAUTEUR")/(1080/400))))
    core.memory("textureVaisseau4", core.Texture("./vaisseau4.png", Vector2(core.memory("LARGEUR")/(1920/1600), core.memory("HAUTEUR")/(1080/400))))

# texture vie
    core.memory("textureCoeur1", core.Texture("./coeur1.png", Vector2(core.memory("LARGEUR")/(1920/35), core.memory("HAUTEUR")/(1080/35))))
    core.memory("textureCoeur2", core.Texture("./coeur2.png", Vector2(core.memory("LARGEUR")/(1920/35), core.memory("HAUTEUR")/(1080/70))))
    core.memory("textureCoeur3", core.Texture("./coeur3.png", Vector2(core.memory("LARGEUR")/(1920/35), core.memory("HAUTEUR")/(1080/105))))

# Fonds d'écran
    core.memory("FondJeu", core.Texture("./FondEcranJeu.jpg", (1, 1), 0, (core.memory("LARGEUR"), core.memory("HAUTEUR"))))
    core.memory("FondChoixVaisseau", core.Texture("./FondJoli.png", (1, 1), 0, (core.memory("LARGEUR"), core.memory("HAUTEUR"))))
    core.memory("FondMenuPrincipal", core.Texture("./FondMenuPrincipal.png", (1, 1), 0, (core.memory("LARGEUR"), core.memory("HAUTEUR"))))
    core.memory("FondMenuRecapitulatifFinDePartie", core.Texture("./FondJoli.png", (1, 1), 0, (core.memory("LARGEUR"), core.memory("HAUTEUR"))))

#texture astéroide
    core.memory("textureAsteroide", core.Texture("./asteroide.png", core.memory("shapeAsteroide1")))



def run():

# etats
    core.cleanScreen()
    if core.memory("etat") == 0:
        menu()

# menu choix de vaisseau
    if core.memory("etat") == 0.2:
        ChoixVaisseau()

# ecran de jeu
    if core.memory("etat") == 1:
        jeu()

# menu pause
    if core.memory("etat") == 2:
        pause()

# guide des touches
    if core.memory("etat") == 2.1:
        touches()

# recapitulatif fin de jeu
    if core.memory("etat") == 3:
        recap()

# menu de fin de jeu
    if core.memory("etat") == 3.1:
        finDeJeu()

# menu choix de vaisseau
    if core.memory("etat") == 4:
        setup(0.2)

# Menu principal
    if core.memory("etat") == 5:
        setup(0)

core.main(setup(0), run)

