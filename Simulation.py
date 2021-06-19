from Classes.Car import Car
from Classes.Motor import Motor
from Classes.Truck import Truck
import random, time, requests

class Simulation:

    def __init__(self) :
        self.nameList = []
        self.vehicles = []
        self.chanceToRain = 0.3
        self.isThereBreakDown = 0


    # Beallitja a jarmu listat.
    def initializeList(self):
        request = requests.get("https://www.fantasynamegenerators.com/scripts/carNames.js?f")
        self.nameList = request.text[ request.text.index("[\"") + 1 : request.text.index("\"]") + 1 ].replace("\"", "").split(",")
        self.vehicles = []

        for i in range(0, 10):
            self.vehicles.append(Car(random.choice(self.nameList) + " " + random.choice(self.nameList), random.randrange(80, 110)))
            self.vehicles.append(Motor("Motor " + str(i + 1), 100))
            self.vehicles.append(Truck(str(random.randrange(1, 1000)), 100, 0, 0))



    # Feljegyzi a lerobbant kamiont.
    def setBreakDownToTruck(self):
        for i in self.vehicles:
                if i.getType() == "Truck" and  i.isBreakDown() and i.getBreakDownHourCounter() == 0 :
                    i.setIsBreakDown(1)
                    i.setBreakDownHourCounter(1)
                    if self.isThereBreakDown == 0:
                        self.isThereBreakDown = 1
                    break



    # Beallitja a kocsi sebesseget attol fuggoen, hogy van e lerobbant kamion vagy sem.
    def setSpeedsToCar(self):
         
        for i in self.vehicles:
            if i.getType() == "Car" and self.isThereBreakDown == 1 :
                i.addHourSpeeds(i.getSpeedDuringBarrier())

            if i.getType() == "Car" and self.isThereBreakDown == 0:
                i.addHourSpeeds(i.getSpeed())
                

     
    # Beallitja a kamion sebesseget attol fuggoen, hogy lerobbant vagy sem.
    def setSpeedsToTruck(self):

        for i in self.vehicles : 
            if i.getType() == "Truck" and i.getBreakDownHourCounter() == 0 :
                i.addHourSpeeds(i.getSpeed())

            if i.getType() == "Truck" and i.getBreakDownHourCounter() == 3 :
                i.addHourSpeeds(i.getSpeed())
                i.setBreakDownHourCounter(0)
                i.setIsBreakDown(0)

            if i.getType() == "Truck" and i.getBreakDownHourCounter() < 3 and i.getBreakDownHourCounter() > 0 :
                i.addHourSpeeds(0)
                i.setBreakDownHourCounter(i.getBreakDownHourCounter() + 1)
            

            

    # Beallitja a motor sebesseget attól fuggoen, hogy esos az ido vagy sem.
    def setSpeedsToMotor(self):

        if random.random() < self.chanceToRain :
            for i in self.vehicles:
                if i.getType() == "Motor" :
                    i.addHourSpeeds(i.getSpeedDuringRain())
        else:
            for i in self.vehicles:
                if i.getType() == "Motor" :
                    i.addHourSpeeds(i.getSpeed())
    


    # A szimulacioban az orankent vizsgalt szempontokat valositja meg.
    def simulation(self):

        hourCounter = 1
        while(hourCounter < 6):        
        
            print("\n------------------- " + str(hourCounter) + ". ora -------------------\n")

            self.setBreakDownToTruck()
            self.setSpeedsToCar()
            self.setSpeedsToTruck()
            self.setSpeedsToMotor()
            self.sortAndPrintResults()
        
            time.sleep(3600)
            hourCounter += 1



    # Az eddigi megtett ut alapjan rendezi és kiirja a jarmuveket.
    def sortAndPrintResults(self): 
        
        shortedList = sorted(self.vehicles, key= lambda x: x.hourSpeeds, reverse = True)

        for i, value in enumerate(shortedList) :
            print(str(i + 1) + ". " + value.getName() + " " + str(value.getHourSpeeds()) + " km " + value.getType())



    # A szimulacio itt fut le.
    def start(self):

        self.initializeList()        
        self.simulation()
        print("\n------------------- VEGEREDMENY -------------------\n")
        self.sortAndPrintResults()
