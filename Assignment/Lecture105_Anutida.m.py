class Vehicle:
    licenseCode = "" 
    serialCode = ""
    def turnAirConditioner(self):
        print("Turn on: Air Conditionar")

class Car(Vehicle):
    pass

class PickUp(Vehicle):
    pass

class Van(Vehicle):
    pass

car1 = Car()
car1.turnAirConditioner()
pickUp1 = PickUp()
pickUp1.turnAirConditioner()
van1 = Van()
van1.turnAirConditioner()