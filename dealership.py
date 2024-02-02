"""
Prompt the user to choose from different categories of vehicle to compare for purchase.
Display an error if the user enters invalid data and asks the user again for a selection.
When the user enters valid data, print each vehicle within that collection of their choosing.
Ask the user if they would like to add a vehicle to compare.
If yes, the user will make a selection and that vehicle will be placed in a collection containing for them to later “compare”.
If not, give the user the option to look at more vehicles in other categories or go ahead and “compare vehicles”.
The user will receive a detailed list of all chosen vehicles, listing their make, miles,
 and price. Each vehicle should also “make noise” as the program iterates through the list.

"""

class vehicle:
    def __init__(self, make, miles, price):
        self.make = make
        self.miles = miles
        self.price = price
        self.engine_on = False

    def start_engine(self):
        print("starting engine")
        self.engine_on = True
        return ""

    def make_noise(self):
        print("Beep Beep")
        return ""


class truck(vehicle):
    def __init__(self, make, miles, price):
        vehicle.__init__(self, make, miles, price)
        self.cargo_property = False

    def load_cargo(self):
        print("loading the truck bed")
        self.cargo_property = True


class motorcycle(vehicle):
    def __init__(self, make, miles, price,top_speed):
        vehicle.__init__(self, make, miles, price)
        self.top = top_speed

    def top_speed(self):
        print(self)

    def make_noise(self):
        return "vroom vroom"


