# Problem 1
# To find numbers greater than a particular number

def greater_than_7(number):
    return number >= 7

numbers = [1,3,5,80,5,3,78,54,3,8,1,35,8,78,3,79]

numbers_greater = list(filter(greater_than_7, numbers))
print(numbers_greater)


# Problem 2
# Filtering a list of numbers to get only even numbers

numbers = [1,3,5,80,5,3,78,54,3,8,1,35,8,78,3,79]

even_numbers = list(filter(lambda x:x % 2 == 0, numbers))
print(even_numbers)


# Problem 3
# Filtering a list of strings to get only strings with length greater than 5

words = ["apple","python","pen","perplexia","dymentia"]

greater_than_5 = list(filter(lambda x:len(x)>5 , words))
print(greater_than_5)


# Problem 4
# Filtering a list of dictionaries to get only dictionaries with a specific key-value pair

people = [
    {'name': 'Alice', 'age': 25, 'city': 'New York'},
    {'name': 'Bob', 'age': 30, 'city': 'Chicago'},
    {'name': 'Charlie', 'age': 35, 'city': 'New York'},
    {'name': 'David', 'age': 40, 'city': 'Los Angeles'}
]

new_yorkers = list(filter(lambda person:person["city"] == "New York", people))
print(new_yorkers)


# Problem 5
# Filtering a list of tuples to get only tuples where the second element is greater than 10

list1 = [(1,2),(3,4),(11,4),(7,23),(12,34),(10,10)]

greater_than_10 = list(filter(lambda x:x[1]>10 ,list1))
print(greater_than_10)
