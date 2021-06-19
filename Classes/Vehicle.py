
# A jarmu alap tulajdonságait megvalosito osztaly
class Vehicle:

    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        self.hourSpeeds = 0

    def getSpeed(self):
        return self.speed

    def getName(self):
        return self.name

    def getHourSpeeds(self):
        return self.hourSpeeds

    def addHourSpeeds(self, value):
        self.hourSpeeds += value