keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

numbers = dict(zip(keys, values))

print(numbers)

#----------------------OR---------------------------

numbers = {}

for i in range(len(keys)):
    numbers.update({keys[i]: values[i]})
    
print(numbers)