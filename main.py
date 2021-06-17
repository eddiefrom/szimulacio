from Controller import Controller


def getRank(list):
    for i in list:
        return i.getHourSpeeds()

def main():

    controller = Controller()
    controller.start()

if __name__ == "__main__":
	main()
