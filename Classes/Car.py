from Classes.Vehicle import Vehicle

# Kocsit megvalosito osztaly.
class Car(Vehicle):
    pass

    # A kocsi sebesseget adja vissza, ha van akadaly.
    def getSpeedDuringBarrier(self):
        return 75

    # A kocsi tipusat adja vissza.
    def getType(self):
        return "Car"
