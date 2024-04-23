"""Problem:
Concept of multiple Inheritance with suitable example.
"""

class Mammal:
    def mammal_info(self):
        print("Mammals can give direct birth.")

class WingedAnimal:
    def winged_animal_info(self):
        print("Winged animals can flap.")

class Bat(Mammal, WingedAnimal):
    pass

clas = Bat()

clas.mammal_info()
clas.winged_animal_info()