from Classes.Vehicle import Vehicle

import random

# Motort megvalósító osztály.
class Motor(Vehicle):
    pass

    # Visszaadja a motor sebességét eső esetén
    def getSpeedDuringRain(self):
        return 100 - random.randrange(5, 10)

    # Visszaadja a motor tipusát
    def getType(self):
        return "Motor"