from Classes.Vehicle import Vehicle
import random

# Kamiont megvalósító osztály.
class Truck(Vehicle):

    def __init__(self, name, speed, isBreakDownValue, breakDownHourCounter):
        super().__init__(name, speed)
        self.isBreakDownValue = isBreakDownValue
        self.breakDownHourCounter = breakDownHourCounter

    # Ha lerobbant akkor 1-el tér vissza különben 0-val.
    def isBreakDown(self):
        if random.random() <= 0.05 :
            return 1
        else:
            return 0

    # Visszaadja, hogy hanyadik órája van lerobbanva a kamion.
    def getBreakDownHourCounter(self):
        return self.breakDownHourCounter
    
    # Beállítja, hogy hanyadik órája van lerobbanva az adott kamion.
    def setBreakDownHourCounter(self, breakDownHourCounter):
        self.breakDownHourCounter = breakDownHourCounter

    # Visszaadja, hogy a kamion le van e robbanva.
    def getIsBreakDown(self):
        return self.isBreakDownValue

    # Beállítja, hogy le van e robbanva a kamion.
    def setIsBreakDown(self, value):
        self.isBreakDownValue = value
    
    # Visszadja a jármű tipusát.
    def getType(self):
        return "Truck"