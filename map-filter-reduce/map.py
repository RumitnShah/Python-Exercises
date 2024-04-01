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