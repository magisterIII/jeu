import core

def boucle():
    if core.memory("positionVaisseau").x < 0:
        core.memory("positionVaisseau").x = 1920

    if core.memory("positionVaisseau").x > 1920:
        core.memory("positionVaisseau").x = 0

    if core.memory("positionVaisseau").y < 0:
        core.memory("positionVaisseau").y = 1080

    if core.memory("positionVaisseau").y > 1080:
        core.memory("positionVaisseau").y = 0