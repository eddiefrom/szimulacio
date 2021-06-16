from Classes.Vehicle import Vehicle

import random

class Truck(Vehicle):

    def __init__(self, name, speed):
        super().__init__(name, speed)
        self.isBreakDownValue = 0

    def isBreakDown(self):
        if random.random() < 0.05 :
            return 1
        else:
            return 0

    def getIsBreakDown(self):
        return self.isBreakDownValue

    def setIsBreakDown(self, value):
        self.isBreakDownValue = value
    
    def getType(self):
        return "Truck"