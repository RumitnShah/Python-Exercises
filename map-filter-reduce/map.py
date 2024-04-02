import math

# Problem 1
# We double all numbers using map()

def double(number):
    twice = number + number
    return twice

numbers = (1,2,3,4,5)

print(list(map(double,numbers)))


# Problem 2
# Double all numbers using map and lambda

numbers = (1,2,3,4,5)

result = list(map(lambda x:x + x,numbers))
print(result)


# Problem 3
# Add two lists using map and lambda

numbers1 = [1,2,3,4,5]
numbers2 = [6,7,8,9,10]

result = list(map(lambda x,y:x + y,numbers1, numbers2))
print(result)


# Problem 4
# listify the list of strings individually

list1 = ['sat', 'bat', 'cat', 'mat']

result = list(map(list,list1))
print(result)


# Problem 5
# Define a function that doubles even numbers and leaves odd numbers as is

def even_numbers(number):
    if number%2 == 0:
        double = number + number
        return double
        
    else:
        return number

numbers = (1,2,3,4,5,6,7,8,9)

result = list(map(even_numbers,numbers))
print(result)


# Problem 6
# Squaring each number in a list

list1 = [1,2,3,4,5,6,7]

result = list(map(lambda x:x**2, list1))
print(result)


# Problem 7
# Converting strings to integers

list1 = ["1","2","3","4","5","6","7"]

result = list(map(int, list1))
print(result)


# Problem 8
# Calculating the area of circles with different radii

def area(radii):
    area_of_circle = math.pi * (radii ** 2)
    return area_of_circle

radii = (3,6,1,2,4,5)
result = list(map(area,radii))
print(result)


# Problem 9
# Using "pow" math function

list1 = [1,2,3,4]
list2 = [5,6,7]

result = list(map(math.pow, list1,list2))
print(result)


# Problem 10 ##
# Using Dictionary with Map(), adding an '_' to the end of each value

car_dict ={'a': 'Mercedes-Benz', 'b': 'BMW', 'c': 'Ferrari', 'd': 'Lamborghini', 'e': 'Jeep'}

result_dict = dict(map(lambda x:(x[0],x[1]+"_"), car_dict))
print(result_dict)


# Problem 11
# To find length of the given string elements

list1 = ["apple", "honey", "chocolate", "butter"]

result = list(map(len, list1))
print(result)


# Problem 12
# To square and cube a number simultaneously

def square(number):
    return number ** 2

def cube(number):
    return number ** 3

numbers = [1,3,5,7,2,4,6,8]
func = [square,cube]

for number in numbers:
    result = list(map(lambda x:x(number),func))
    print(result)