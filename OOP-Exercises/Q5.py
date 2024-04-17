class Vehicle:
    color = "white"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

vehicle_1 = Bus("School Volvo", 180, 12)
vehicle_2 = Car("Mustang GT", 240, 18)

print(f"Color = {vehicle_1.color}, Vehicle name = {vehicle_1.name}, Max Speed = {vehicle_1.max_speed}km/hr, Mileage = {vehicle_1.mileage}MPG")
print(f"Color = {vehicle_2.color}, Vehicle name = {vehicle_2.name}, Max Speed = {vehicle_2.max_speed}km/hr, Mileage = {vehicle_2.mileage}MPG")