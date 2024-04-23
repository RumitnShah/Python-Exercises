"""Problem:
Create a class “Animal” with attribute “name” and a function “eat()”. 
Now, create another class “Dog”, which inherit the “Animal” class. 
The “Dog” class will have a method “Display()” to print “My name is $dog_name$”. 
The eat() method of “Animal” class will print a message “I can eat”. 
Now, demonstrate the inheritance by creating an object of class “Dog”, 
which will inherit the attribute “name” and method “eat” of “Animal” class.
"""

class Animal:
    def __init__(self,name):
        self.name = name

    def eat(self):
        print("I can eat")

class Dog(Animal):
    def display(self):
        print(f"My name is {self.name}")

name_dog = Dog("Cookie")

name_dog.eat()
name_dog.display()