from Classes.Vehicle import Vehicle
import random

# Kamiont megvalosito osztaly.
class Truck(Vehicle):

    def __init__(self, name, speed, isBreakDownValue, breakDownHourCounter):
        super().__init__(name, speed)
        self.isBreakDownValue = isBreakDownValue
        self.breakDownHourCounter = breakDownHourCounter

    # Ha lerobbant akkor 1-el ter vissza kulonben 0-val.
    def isBreakDown(self):
        if random.random() <= 0.05 :
            return 1
        else:
            return 0

    # Visszaadja, hogy hanyadik oraja van lerobbanva a kamion.
    def getBreakDownHourCounter(self):
        return self.breakDownHourCounter
    
    # Beallitja, hogy hanyadik oraja van lerobbanva az adott kamion.
    def setBreakDownHourCounter(self, breakDownHourCounter):
        self.breakDownHourCounter = breakDownHourCounter

    # Visszaadja, hogy a kamion le van e robbanva.
    def getIsBreakDown(self):
        return self.isBreakDownValue

    # Beallitja, hogy le van e robbanva a kamion.
    def setIsBreakDown(self, value):
        self.isBreakDownValue = value
    
    # Visszadja a jarmu tipusat.
    def getType(self):
        return "Truck"