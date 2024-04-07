class Vehicle:

    def __init__(self ,max_speed ,mileage):
        self.max_speed = max_speed
        self.mileage = mileage

about = Vehicle(210, 30)

print(f"max_speed = {about.max_speed}km/hr, mileage = {about.mileage}MPG")