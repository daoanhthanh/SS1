class car:
    speed = 0
    acce = []
    brek = []
    def __init__ (self, year_model, __make, __speed):
        self.year = year_model
        self.make = __make
        self.speed = __speed

    def acclerate(self):
        
        return self.speed + 5
    def set_speed(self):
        self.speed = self.speed+5
    def _break(self):
        return self.speed - 5
    
    def get_speed(self):
        return self.speed
    def print(self):
        print(self)


a_new_car = car(2013, "Madza" , 60 )

while len(a_new_car.acce) != 5:
    a_new_car.acce.append(a_new_car.acclerate())
    a_new_car.set_speed

print(a_new_car.get_speed())
print(a_new_car.acce)
