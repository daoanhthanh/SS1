class car:
    def __init__(self,f,c):
        self.color = "red"
        f.name = "Dao Anh Thanh"
        c.age = 20
    def a_real_car(self):
        print("Car color: ", self.color, ". License plate: ", self.plate)

ob = car()
ob.a_real_car()
