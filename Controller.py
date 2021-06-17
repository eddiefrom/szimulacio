from Classes.Car import Car
from Classes.Motor import Motor
from Classes.Truck import Truck
import random, time, requests

class Controller:

    def __init__(self) :
        self.nameList = []
        self.vehicles = []
        self.chanceToRain = 0.3

    def initialize(self):
        request = requests.get("https://www.fantasynamegenerators.com/scripts/carNames.js?f")
        self.nameList = request.text[ request.text.index("[\"") + 1 : request.text.index("\"]") + 1 ].replace("\"", "").split(",")
        self.vehicles = []

        for i in range(0, 10):
            self.vehicles.append(Car(random.choice(self.nameList) + " " + random.choice(self.nameList), random.randrange( 80, 110)))
            self.vehicles.append(Motor("Motor " + str(i + 1), 100))
            self.vehicles.append(Truck(str(random.randrange(0, 1000)), 100))

    def simulation(self):
        breakDownCounter = 0
        hourCounter = 1
        while(hourCounter < 6):        
        
            print(str(hourCounter) + ". óra")

            if breakDownCounter == 3:
                breakDownCounter = 0

            for i in self.vehicles:
                if i.getType() == "Truck" and  i.isBreakDown() and breakDownCounter == 0 :
                    breakDownCounter = 1
                    i.setIsBreakDown(1)
                    break

            if breakDownCounter > 0 and breakDownCounter < 3:
                for i in self.vehicles:
                    if i.getType() == "Car" :
                        i.addHourSpeeds(i.getSpeedDuringBarrier())
                
                    if i.getType() == "Truck" and i.getIsBreakDown() == 1 :
                        i.addHourSpeeds(0)

                    if i.getType() == "Truck" and i.getIsBreakDown() == 0 :
                        i.addHourSpeeds(i.getSpeed())

                breakDownCounter += 1         
            else:
                for i in self.vehicles:
                    if i.getType() == "Car" :
                        i.addHourSpeeds(i.getSpeed())
                
                    if i.getType() == "Truck" :
                        i.addHourSpeeds(i.getSpeed())
                        i.setIsBreakDown(0) 

            if random.random() < self.chanceToRain :
                for i in self.vehicles:
                    if i.getType() == "Motor" :
                        i.addHourSpeeds(i.getSpeedDuringRain())
                print("Esik ")
            else:
                print("Nem esik")
                for i in self.vehicles:
                    if i.getType() == "Motor" :
                        i.addHourSpeeds(i.getSpeed())
        
            time.sleep(2)
            hourCounter += 1

        shortedList = sorted(self.vehicles, key= lambda x: x.hourSpeeds, reverse = True)

        for i, value in enumerate(shortedList) :
            print(str(i + 1) + ". " + value.getName() + " " + str(value.getHourSpeeds()) + " km " + value.getType())


    def start(self):

        self.initialize()        
        self.simulation()
