from Classes.Car import Car
from Classes.Motor import Motor
from Classes.Truck import Truck
import random, time, requests


def getRank(list):
    for i in list:
        return i.getHourSpeeds()

def main():
    
    request = requests.get("https://www.fantasynamegenerators.com/scripts/carNames.js?f")
    nameList = request.text[ request.text.index("[\"") + 1 : request.text.index("\"]") + 1 ].replace("\"", "").split(",")
    vehicles = []

    for i in range(0, 10):
        vehicles.append(Car(random.choice(nameList) + " " + random.choice(nameList), random.randrange( 80, 110)))
        vehicles.append(Motor("Motor " + str(i + 1), 100))
        vehicles.append(Truck(str(random.randrange(0, 1000)), 100))

    chanceToRain = 0.3

    moto = Motor("M", 100)
    truk = Truck(str(random.randrange(0, 1000)), 100)
    car = Car(random.choice(nameList) + " " + random.choice(nameList), random.randrange(80, 110))

    breakDownCounter = 0
    hourCounter = 1
    while(hourCounter < 6):        
        
        print(str(hourCounter) + ". óra")

        if breakDownCounter == 3:
            breakDownCounter = 0

        for i in vehicles:
            if i.getType() == "Truck" and  i.isBreakDown() and breakDownCounter == 0 :
                breakDownCounter = 1
                i.setIsBreakDown(1)
                print("lerobbant ", breakDownCounter, i.getName())
                break

        if breakDownCounter > 0 and breakDownCounter < 3:
            for i in vehicles:
                if i.getType() == "Car" :
                    i.addHourSpeeds(i.getSpeedDuringBarrier())
            
                if i.getType() == "Truck" and i.getIsBreakDown() == 1 :
                    i.addHourSpeeds(0)
                    print("Lerobannás ennél ", i.getName())

                if i.getType() == "Truck" and i.getIsBreakDown() == 0 :
                    i.addHourSpeeds(i.getSpeed())
                    print("Lerobannás nincs ennél ", i.getName())

            print("tart a lerobbanas ", breakDownCounter)
            breakDownCounter += 1         
        else:
            for i in vehicles:
                if i.getType() == "Car" :
                    i.addHourSpeeds(i.getSpeed())
            
                if i.getType() == "Truck" :
                    i.addHourSpeeds(i.getSpeed())
                    i.setIsBreakDown(0) 

        if random.random() < chanceToRain :
            for i in vehicles:
                if i.getType() == "Motor" :
                    i.addHourSpeeds(i.getSpeedDuringRain())
            print("Esik ")
        else:
            print("Nem esik")
            for i in vehicles:
                if i.getType() == "Motor" :
                    i.addHourSpeeds(i.getSpeed())
    
        time.sleep(2)
        hourCounter += 1

    shortedList = sorted(vehicles, key= lambda x: x.hourSpeeds, reverse = True)

    for i, value in enumerate(shortedList) :
        print(str(i + 1) + ". " + value.getName() + " " + str(value.getHourSpeeds()) + " km " + value.getType())

    
    # Minden órában 30% esély az esőre
    # Kocsi: Lerobban kamionnál 75km/h az adott órában
    # Motor: Ha esik akkor 5-10 km/h a sebbesség
    # Kamion: 5% esély hogy lerobban
    # Óránként vizsgálni a versenyt!!

if __name__ == "__main__":
	main()
