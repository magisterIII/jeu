import time

import pygame

import core
from CreationTir import CreationTir

def tir():

    # CLEAN
    for tir in core.memory('projectiles'):
        if time.time() - tir["startTime"] > 5:
            core.memory('projectiles').remove(tir)

    # TIR
    if core.getKeyPressList("SPACE"):
        if len(core.memory("projectiles")) == 0:
            CreationTir()
        else:
            if time.time() - core.memory("projectiles")[-1]["startTime"] > 0.5:
                CreationTir()

    # DEPLACEMENT
    for tir in core.memory("projectiles"):
        tir["positionVaisseau"] = tir["positionVaisseau"] + tir["vitesseVaisseau"]

    # DESSIN TIR
    for tir in core.memory("projectiles"):
        core.Draw.circle(tir["color"], tir["positionVaisseau"], tir["rayon"])