# Create file with current Date-Time

from datetime import datetime

current = datetime.now()       # get current date and time

file_name = current.strftime('%d-%m-%Y.txt')       # Format of new file as a name day-month-year
with open(file_name, 'w') as f1:
    print('created', file_name)

#------------------------ OR -------------------------

file_name_2 = current.strftime('%d-%m-%Y-%H-%M-%S.txt')        # Format as day-month-year-hours-minutes-seconds
with open(file_name_2, 'w') as f2:
    print('created', file_name_2)

#------------------------ OR --------------------------
    
# at specified directory
file_name_3 = r"C:\Users\Administrator\Documents\GitHub\Python-Exercises\File-Handling" + current.strftime('%d-%m-%Y-%H-%M-%S.txt')
with open(file_name_3, 'w') as f3:
    print('created', file_name_3)