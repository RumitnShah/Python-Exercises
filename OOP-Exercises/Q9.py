"""Problem:
Create two classes “Cat” and “Dog” with two attributes “name” and “age”. Both classes share a similar structure and have the same method names info() and make_sound(). 

When a make_sound() is called using dog object it should print “Bark”, and when called using cat object, it should print “Meow”. 

Similarly, when info() is called using dog object it should print “I am a dog. My name is $dog_name$. I am $dog_age$ years old.
"""

class cat:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")
    
    def make_sound(self):
        print("meow")

class dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")
    
    def make_sound(self):
        print("bark")

animal = {cat("Tom", 3),
           dog("Sheperd", 1.5)
}

for every_animal in animal:
    every_animal.info()
    every_animal.make_sound()
