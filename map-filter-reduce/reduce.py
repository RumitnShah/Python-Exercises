from functools import reduce

# Problem 1
# using reduce to compute sum of list

numbers = [1,2,3,4]

add = reduce(lambda x,y:x+y, numbers)
print(add)


# Problem 2
# using reduce to compute maximum element from list

numbers = [3,3556,5432,26,3,2,7,2,147,5,5,544]

greater = reduce(lambda x,y:x if x>y else y, numbers)
print(greater)


# Problem 3
# Multiplying All Elements in a List

numbers = [1,2,3,4,5,6,7,8,9]

multiply = reduce(lambda x,y:x * y, numbers)
print(multiply)


# Problem 4
# Concatenating Strings in a List

list1 = ["Do","not","concatenate","the","strings","in","the","list"]

concatenated = reduce(lambda x,y:x + "" + y,list1)
print(concatenated)


# Problem 5
# Calculating Factorial of a Number

number = 7

factorial = reduce(lambda x,y: x*y, range(1,number+1))
print(factorial)


# Problem 6
# Checking if All Values Are True

def is_true(a,b):
    true = bool(a and b)
    return true

print(reduce(is_true,[1,1,1,1,1]))
print(reduce(is_true,[1,1,0,1,1]))


# Problem 7
# Use reduce function for flattening a 2D list

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] 

new_list = reduce(lambda x,y: x+y, matrix)
print(new_list)


#------------------------USING OPERATOR FUNCTIONS----------------------------
import operator

# Problem 8
# using reduce to compute sum of list using operator functions 

numbers = [1, 3, 5, 6, 2]

addition = reduce(operator.add, numbers)
print(addition)


# Problem 9
# using reduce to compute product using operator functions 

numbers = [1, 3, 5, 6, 2]

product = reduce(operator.mul, numbers)
print(product)


# Problem 10
# using reduce to concatenate list of string 

list1 = ["Please","leave","no","space","inbetween"]

concatenate = reduce(operator.add, list1)
print(concatenate)
