class Airplane:
    def __init__(self, make, model, year, max_speed):
        self.make = make
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self.odometer = 0
        self.is_flying = False

    def take_off(self):
        self.is_flying = True
        return f'Самолет {self.make} {self.model} взлетел.'



    def fly(self, distance):
        self.distance = distance
        self.odometer += distance
        return f'Самолет {self.make} {self.model} в полете. ' \
               f'Показатель одометра равен {self.odometer} км.'


    def land(self):
        self.is_flying = False
        return f'Самолет {self.make} {self.model} приземлился.'


plane_1 = Airplane('Boeing', '777X', '2018', 965)
print(plane_1.take_off())
print(plane_1.fly(4000))
print(plane_1.land())

