from Classes.Vehicle import Vehicle

import random

class Motor(Vehicle):
    pass

    def getSpeedDuringRain(self):
        return 100 - random.randrange(5, 10)

    def getType(self):
        return "Motor"