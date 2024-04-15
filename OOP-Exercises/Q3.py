class Vehicle:

    def __init__(self ,name, max_speed ,mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

about = Bus("The Yellow Bus", 210, 30)

print(f"Vehicle name = {about.name}, Max Speed = {about.max_speed}km/hr, Mileage = {about.mileage}MPG")