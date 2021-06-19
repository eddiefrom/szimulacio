from Classes.Vehicle import Vehicle

import random

# Motort megvalosito osztaly.
class Motor(Vehicle):
    pass

    # Visszaadja a motor sebesseget eso eseten
    def getSpeedDuringRain(self):
        return 100 - random.randrange(5, 10)

    # Visszaadja a motor tipusat
    def getType(self):
        return "Motor"