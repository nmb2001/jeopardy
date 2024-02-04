class Car:
    def __init__(self, seats, type, miles ):
        self.seats = seats
        self.type = type
        self.miles = miles

    def print(self):
        print("The car has ", self.seats, "seats. It is a ", self.type, " vehicle and has ", self.miles, " miles.")

if __name__ == '__main__':
    c = Car(5, "Luxury", 40000)
    c.print()
