from Classes.Vehicle import Vehicle

# Kocsit megvalósító osztály.
class Car(Vehicle):
    pass

    # A kocsi sebességét adja vissza, ha van akadály.
    def getSpeedDuringBarrier(self):
        return 75

    # A kocsi tipusát adja vissza.
    def getType(self):
        return "Car"
